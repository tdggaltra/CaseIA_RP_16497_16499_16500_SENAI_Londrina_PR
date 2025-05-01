# prediction/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PredictionForm
from .models import Prediction
import joblib
import pandas as pd
import os
import json
from django.conf import settings

# Carregar os modelos
MODEL_DIR = os.path.join(settings.BASE_DIR, '..', 'models')
BEST_MODELS_INFO = json.load(open(os.path.join(MODEL_DIR, 'best_models_info.json')))

preprocessor = joblib.load(os.path.join(MODEL_DIR, BEST_MODELS_INFO['preprocessor']))
heating_model = joblib.load(os.path.join(MODEL_DIR, 'best_heating_model.pkl'))
cooling_model = joblib.load(os.path.join(MODEL_DIR, 'best_cooling_model.pkl'))

@login_required
def dashboard(request):
    predictions = Prediction.objects.filter(user=request.user).order_by('-date_created')[:5]
    total_predictions = Prediction.objects.filter(user=request.user).count()
    
    context = {
        'predictions': predictions,
        'total_predictions': total_predictions
    }
    
    return render(request, 'prediction/dashboard.html', context)

@login_required
def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Salvar o formulário sem commit para adicionar o usuário
            prediction = form.save(commit=False)
            prediction.user = request.user
            
            # Preparar os dados para o modelo
            features_dict = {
                'Relative_Compactness': prediction.relative_compactness,
                'Surface_Area': prediction.surface_area,
                'Wall_Area': prediction.wall_area,
                'Roof_Area': prediction.roof_area,
                'Overall_Height': prediction.overall_height,
                'Orientation': prediction.orientation,
                'Glazing_Area': prediction.glazing_area,
                'Glazing_Area_Distribution': prediction.glazing_area_distribution
            }
            
            # Transformar em DataFrame
            features_df = pd.DataFrame([features_dict])
            
            # Aplicar o preprocessador
            features_preprocessed = preprocessor.transform(features_df)
            
            # Fazer as previsões
            prediction.heating_load = float(heating_model.predict(features_preprocessed)[0])
            prediction.cooling_load = float(cooling_model.predict(features_preprocessed)[0])
            
            # Salvar a predição
            prediction.save()
            
            messages.success(request, f'Predição realizada com sucesso!')
            return redirect('prediction_detail', pk=prediction.pk)
    else:
        form = PredictionForm()
    
    return render(request, 'prediction/predict.html', {'form': form})

@login_required
def prediction_list(request):
    predictions = Prediction.objects.filter(user=request.user).order_by('-date_created')
    return render(request, 'prediction/prediction_list.html', {'predictions': predictions})

@login_required
def prediction_detail(request, pk):
    prediction = get_object_or_404(Prediction, pk=pk)
    return render(request, 'prediction/prediction_detail.html', {'prediction': prediction})

@login_required
def prediction_delete(request, pk):
    prediction = get_object_or_404(Prediction, pk=pk)
    
    if request.method == 'POST':
        prediction.delete()
        messages.success(request, f'Predição excluída!')
        return redirect('prediction_list')
    
    return render(request, 'prediction/prediction_confirm_delete.html', {'prediction': prediction})

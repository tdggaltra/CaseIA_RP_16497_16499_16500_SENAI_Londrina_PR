# prediction/utils.py
import pandas as pd
import joblib
import os
import json
from django.conf import settings

def load_models():
    """Carrega os modelos de predição."""
    model_dir = os.path.join(settings.BASE_DIR, '..', '..', 'models')
    
    try:
        # Carregar informações dos melhores modelos
        with open(os.path.join(model_dir, 'best_models_info.json'), 'r') as f:
            best_models_info = json.load(f)
        
        # Carregar o preprocessador
        preprocessor = joblib.load(os.path.join(model_dir, best_models_info['preprocessor']))
        
        # Carregar os modelos
        heating_model = joblib.load(os.path.join(model_dir, 'best_heating_model.pkl'))
        cooling_model = joblib.load(os.path.join(model_dir, 'best_cooling_model.pkl'))
        
        return preprocessor, heating_model, cooling_model
    
    except Exception as e:
        print(f"Erro ao carregar os modelos: {e}")
        return None, None, None

def predict_energy_loads(features_dict):
    """
    Realiza a predição das cargas de aquecimento e resfriamento.
    
    Args:
        features_dict (dict): Dicionário com os valores das features
            {
                'relative_compactness': float,
                'surface_area': float,
                'wall_area': float,
                'roof_area': float,
                'overall_height': float,
                'orientation': str,
                'glazing_area': float,
                'glazing_area_distribution': str
            }
    
    Returns:
        dict: Dicionário com as previsões de Heating Load e Cooling Load
            {
                'heating_load': float,
                'cooling_load': float
            }
    """
    # Carregar os modelos
    preprocessor, heating_model, cooling_model = load_models()
    
    if not all([preprocessor, heating_model, cooling_model]):
        return {'error': 'Falha ao carregar os modelos'}
    
    # Preparar os dados para o modelo
    features_renamed = {
        'Relative_Compactness': features_dict['relative_compactness'],
        'Surface_Area': features_dict['surface_area'],
        'Wall_Area': features_dict['wall_area'],
        'Roof_Area': features_dict['roof_area'],
        'Overall_Height': features_dict['overall_height'],
        'Orientation': features_dict['orientation'],
        'Glazing_Area': features_dict['glazing_area'],
        'Glazing_Area_Distribution': features_dict['glazing_area_distribution']
    }
    
    # Transformar em DataFrame
    features_df = pd.DataFrame([features_renamed])
    
    try:
        # Aplicar o preprocessador
        features_preprocessed = preprocessor.transform(features_df)
        
        # Fazer as previsões
        heating_load = float(heating_model.predict(features_preprocessed)[0])
        cooling_load = float(cooling_model.predict(features_preprocessed)[0])
        
        return {
            'heating_load': heating_load,
            'cooling_load': cooling_load
        }
    
    except Exception as e:
        print(f"Erro ao fazer predição: {e}")
        return {'error': str(e)}
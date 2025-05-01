# prediction/forms.py
from django import forms
from .models import Prediction

class PredictionForm(forms.ModelForm):
    ORIENTATION_CHOICES = [
        ('North', 'Norte'),
        ('South', 'Sul'),
        ('East', 'Leste'),
        ('West', 'Oeste'),
    ]
    
    GLAZING_DISTRIBUTION_CHOICES = [
        ('Uniform', 'Uniforme'),
        ('North', 'Norte'),
        ('South', 'Sul'),
        ('East', 'Leste'),
        ('West', 'Oeste'),
    ]
    
    orientation = forms.ChoiceField(choices=ORIENTATION_CHOICES)
    glazing_area_distribution = forms.ChoiceField(choices=GLAZING_DISTRIBUTION_CHOICES)
    
    class Meta:
        model = Prediction
        fields = [
            'relative_compactness', 'surface_area', 'wall_area', 
            'roof_area', 'overall_height', 'orientation', 
            'glazing_area', 'glazing_area_distribution'
        ]
        labels = {
            'relative_compactness': 'Compacidade Relativa',
            'surface_area': 'Área da Superfície',
            'wall_area': 'Área da Parede',
            'roof_area': 'Área do Telhado',
            'overall_height': 'Altura Total',
            'orientation': 'Orientação',
            'glazing_area': 'Área Envidraçada',
            'glazing_area_distribution': 'Distribuição da Área Envidraçada',
        }
        widgets = {
            'relative_compactness': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.5', 'max': '1.0'}),
            'surface_area': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '500', 'max': '900'}),
            'wall_area': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '200', 'max': '500'}),
            'roof_area': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '100', 'max': '250'}),
            'overall_height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '3', 'max': '8'}),
            'glazing_area': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '0.5'}),
        }
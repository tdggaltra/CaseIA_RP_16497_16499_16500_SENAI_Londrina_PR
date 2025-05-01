# prediction/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Prediction
import json

class PredictionTests(TestCase):
    def setUp(self):
        # Criar um usuário para testes
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        
        # Criar um cliente para testes
        self.client = Client()
        
        # Fazer login
        self.client.login(username='testuser', password='testpassword123')
        
        # Criar uma predição para testes
        self.prediction = Prediction.objects.create(
            user=self.user,
            relative_compactness=0.75,
            surface_area=650.0,
            wall_area=318.5,
            roof_area=183.8,
            overall_height=5.25,
            orientation='North',
            glazing_area=0.25,
            glazing_area_distribution='Uniform',
            heating_load=20.0,
            cooling_load=25.0
        )
    
    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prediction/dashboard.html')
    
    def test_predict_view_get(self):
        response = self.client.get(reverse('predict'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prediction/predict.html')
    
    def test_prediction_list_view(self):
        response = self.client.get(reverse('prediction_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prediction/prediction_list.html')
        self.assertContains(response, self.prediction.relative_compactness)
    
    def test_prediction_detail_view(self):
        response = self.client.get(reverse('prediction_detail', args=[self.prediction.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prediction/prediction_detail.html')
        self.assertContains(response, self.prediction.heating_load)
        self.assertContains(response, self.prediction.cooling_load)
    
    def test_prediction_delete_view(self):
        response = self.client.post(reverse('prediction_delete', args=[self.prediction.id]))
        self.assertRedirects(response, reverse('prediction_list'))
        self.assertEqual(Prediction.objects.count(), 0)

# prediction/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    
    # Inputs
    relative_compactness = models.FloatField()
    surface_area = models.FloatField()
    wall_area = models.FloatField()
    roof_area = models.FloatField()
    overall_height = models.FloatField()
    orientation = models.CharField(max_length=20)
    glazing_area = models.FloatField()
    glazing_area_distribution = models.CharField(max_length=20)
    
    # Outputs
    heating_load = models.FloatField()
    cooling_load = models.FloatField()
    
    def __str__(self):
        return f'Prediction by {self.user.username} on {self.date_created.strftime("%Y-%m-%d %H:%M")}'

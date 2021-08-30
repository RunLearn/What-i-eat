from django.db import models
from mainapp.apps import get_foodname

# Create your models here.
class MainPage(models.Model):
    
    content = models.TextField(null = False, default=get_foodname())
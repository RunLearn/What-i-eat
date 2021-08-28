from django.db import models

# Create your models here.
class MainPage(models.Model):
    
    content = models.TextField(null = False)
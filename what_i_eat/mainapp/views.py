from django.db import models
from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import MainPage



# Create your views here.
class MainPageListView(ListView):
    model = MainPage
    template_name = 'mainapp/main.html'
from mainapp.views import MainPageListView
from django.urls import path, include

urlpatterns = [
    path('',MainPageListView.as_view(), name='main')
]
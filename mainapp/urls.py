from mainapp.views import MainPageView
from django.urls import path, include

urlpatterns = [
    # path('',MainPageView.as_view(), name='main')
    path('', MainPageView, name='MainPage')
]
from django.shortcuts import render
from mainapp.models import MainPage

def MainPageView(request):
    model = MainPage
    context = {'foodname': model}
    return render(request, 'mainapp/main.html', context)
from django.forms import ModelForm
from mainapp.models import MainPage


class MainPageCreationForm(ModelForm):
    class Meta:
        model = MainPage
        fields = ("content")

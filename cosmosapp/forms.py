#from turtle import distance
#from django.core import validators
from django import forms
from .models import Planets

class PlanetsData(forms.ModelForm):
    class Meta:
        model = Planets
        fields = ['name', 'distance', 'stars']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'distance': forms.TextInput(attrs={'class':'form-control'}),
            'stars': forms.TextInput(attrs={'class':'form-control'}),

        }
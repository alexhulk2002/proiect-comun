from django import forms
from django.forms import ModelForm
from .models import Cazare

class newform(ModelForm):
    class Meta:
        model= Cazare
        fields = "__all__"
        labels={
            'title': 'Titlu',
            'description': 'Descriere',
            'author': 'Autor',
            'adresa': 'Adresa',
            'photos': 'Poza',
        }
        widgets ={
            'title': forms.TextInput(attrs={'class':'new', 'required':''}),
            'description': forms.TextInput(attrs={'class':'new', 'required':''}),
            'author':forms.TextInput(attrs={'class':'new', 'required':''}),
            'adresa':forms.TextInput(attrs={'class':'new', 'required':''}),
        }
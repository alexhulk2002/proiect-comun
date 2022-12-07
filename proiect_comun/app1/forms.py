from django import forms
from django.forms import ModelForm
from .models import Cazare

class newform(ModelForm):
    class Meta:
        model= Cazare
        fields = "__all__"
from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import *

class Urlcreation_form(ModelForm):
    class Meta:
        model = Urlmodel
        fields = ['long_url']
        widgets = {'long_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Long URL'})}
        labels = {'long_url': _('')}
# Django imports
from django import forms
# Local imports
from .models import Ubication


class UbicationForm(forms.ModelForm):
    class Meta:
        model = Ubication
        fields = ['city', 'province', 'poblation']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'poblation': forms.NumberInput(attrs={'class': 'form-control'})
        }
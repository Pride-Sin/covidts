# Django imports
from django import forms
# Local imports
from .models import Pacient
from users.models import User



class PacientForm(forms.ModelForm):

    class Meta:
        model = Pacient
        fields = ['dni', 'first_name', 'last_name', 'birth', 'risk', 'status', 'ubication', 'supervisor']
        widgets = {
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth': forms.DateInput(attrs={'class': 'form-control'}),
            'risk': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'ubication': forms.Select(attrs={'class': 'form-select'}),
            'supervisor': forms.Select(attrs={'class': 'form-select'})
        }
# Local imports
import django_filters
from .models import Patient

class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = {
            'dni': ['exact'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'risk': ['exact'],
            'status': ['exact'],
            'ubication': ['exact'],
            'supervisor': ['exact'],
        }
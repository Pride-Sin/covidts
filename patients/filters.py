# Django-filter imports
import django_filters
# Local imports
from .models import Patient
from ubications.models import Ubication
from users.models import User

class PatientFilter(django_filters.FilterSet):
    ubication = django_filters.ModelChoiceFilter(
        queryset=Ubication.objects.all(),
        empty_label="Ubication",
    )
    status = django_filters.ChoiceFilter(
        choices=Patient.STATUS_CHOICES, empty_label="Status"
    )
    supervisor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        empty_label="Supervisor",
    )
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
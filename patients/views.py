# Django imports
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
# Local imports
from .models import Patient
from .forms import PatientForm

class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')


class PatientListView(ListView):
    model = Patient

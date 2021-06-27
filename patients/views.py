# Django imports
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Local imports
from .models import Patient
from .forms import PatientForm
# Tables2 imports
from django_tables2.views import SingleTableMixin
# Filters import
from django_filters.views import FilterView
from .filters import PatientFilter
from .tables import PatientTable

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('patients')

    def get_success_url(self):
        messages.success(self.request, 'Patient added')
        return self.success_url


class PatientEditView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('patients')

    def get_success_url(self):
        messages.success(self.request, 'Patient updated')
        return self.success_url

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    form_class = PatientForm
    context_object_name = 'patient'
    redirect_authenticated_user = True
    success_url = reverse_lazy('patients')

    def get_success_url(self):
        messages.success(self.request, 'Patient deleted')
        return self.success_url

class PatientListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    model = Patient
    table_class = PatientTable
    context_object_name = 'patients'
    filterset_class = PatientFilter
    
    # Context
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['infected'] = Patient.objects.filter(status='infected').count
        context['recovered'] = Patient.objects.filter(status='recuperated').count
        context['vaccinated'] = Patient.objects.filter(status='vaccinated').count
        context['risk'] = Patient.objects.filter(risk=True).count
        context['uci'] = Patient.objects.filter(status='uci').count

        return context

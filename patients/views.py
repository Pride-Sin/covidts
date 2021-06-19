# Django imports
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
# Local imports
from .models import Patient
from .forms import PatientForm
# Tables2 imports
from django_tables2.views import SingleTableMixin
# Filters import
from django_filters.views import FilterView
from .filters import PatientFilter
from .tables import PatientTable

class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('patients')


class PatientEditView(UpdateView):
    model = Patient
    form_class = PatientForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('patients')


class PatientListView(SingleTableMixin, FilterView):
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
        context['risk'] = Patient.objects.filter(status=True).count
        context['uci'] = Patient.objects.filter(status='uci').count

        return context

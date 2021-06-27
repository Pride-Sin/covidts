# Django imports
from django.contrib.messages.api import success
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Local imports
from .models import Ubication
from .forms import UbicationForm
from ubications.tables import UbicationTable
# Tables2 imports
from django_tables2.views import SingleTableMixin
# Filters import
from django_filters.views import FilterView
from .filters import UbicationFilter


class UbicationCreateView(LoginRequiredMixin, CreateView):
    model = Ubication
    form_class = UbicationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('ubications')

    def get_success_url(self):
        messages.success(self.request, 'Ubication created')
        return self.success_url


class UbicationEditView(LoginRequiredMixin, UpdateView):
    model = Ubication
    form_class = UbicationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('ubications')

    def get_success_url(self):
        messages.success(self.request, 'Ubication updated')
        return self.success_url

class UbicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Ubication
    form_class = UbicationForm
    context_object_name = 'ubication'
    redirect_authenticated_user = True
    success_url = reverse_lazy('ubications')

    def get_success_url(self):
        messages.success(self.request, 'Ubication deleted')
        return self.success_url


class UbicationListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    model = Ubication
    table_class = UbicationTable
    context_object_name = 'ubications'
    filterset_class = UbicationFilter


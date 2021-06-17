# Django imports
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# Local imports
from .models import Ubication
from .forms import UbicationForm
from ubications.tables import UbicationTable
# Tables2 imports
from django_tables2.views import SingleTableMixin
# Filters import
from django_filters.views import FilterView
from .filters import UbicationFilter


class UbicationCreateView(CreateView):
    model = Ubication
    form_class = UbicationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')


class UbicationListView(SingleTableMixin, FilterView):
    model = Ubication
    table_class = UbicationTable
    context_object_name = 'ubications'
    filterset_class = UbicationFilter


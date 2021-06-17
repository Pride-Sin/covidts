# Django imports
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# Local imports
from .models import Ubication
from .forms import UbicationForm
from django_tables2.views import SingleTableView
from ubications.tables import UbicationTable

class UbicationCreateView(CreateView):
    model = Ubication
    form_class = UbicationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')


class UbicationListView(SingleTableView):
    model = Ubication
    table_class = UbicationTable
    context_object_name = 'ubications'


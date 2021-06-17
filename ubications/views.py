# Django imports
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
# Local imports
from .models import Ubication
from .forms import UbicationForm

class UbicationCreateView(CreateView):
    model = Ubication
    form_class = UbicationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')


class UbicationListView(ListView):
    model = Ubication

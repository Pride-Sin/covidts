# Django imports
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# Local imports
from .models import Pacient
from .forms import PacientForm

class PacientCreateView(CreateView):
    model = Pacient
    form_class = PacientForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

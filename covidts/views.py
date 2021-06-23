# Django imports
from django.views.generic import ListView
# Local imports
from patients.models import Patient
from ubications.models import Ubication
from .utils import *

class Index(ListView):
    template_name = 'home.html'
    context_object_name = 'index'  
    queryset = Patient.objects.all()  

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context['ubication'] = Ubication.objects.all()

        # Status amount
        vaccinated_amount = Patient.objects.filter(status='vaccinated').count()
        infected_amount = Patient.objects.filter(status='infected').count()
        uci_amount = Patient.objects.filter(status='uci').count()
        recuperated_amount = Patient.objects.filter(status='recuperated').count()

        total_amount = vaccinated_amount + infected_amount +  uci_amount + recuperated_amount 

        context['vaccinated'] = vaccinated_amount
        context['infected'] = infected_amount
        context['uci'] = uci_amount
        context['recuperated'] = recuperated_amount

        context['total'] = total_amount

        # Status porcentages
        porcentages = chart_porcentage(vaccinated_amount, infected_amount, uci_amount, recuperated_amount)
        vaccinated_porcentage = porcentages[0]
        uci_porcentage = porcentages[2]
        infected_porcentage = porcentages[1]


        context['vaccinated_porcentage'] = vaccinated_porcentage
        context['infected_porcentage'] = infected_porcentage
        context['uci_porcentage'] = uci_porcentage
        

        return context
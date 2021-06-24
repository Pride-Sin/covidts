# Django imports
from django.views.generic import ListView
from django.db.models import Count
# Local imports
from patients.models import Patient
from ubications.models import Ubication
from .utils import *

class Index(ListView):
    template_name = 'home.html'
    context_object_name = 'index'  
    queryset = Patient.objects.all()  
    
    #? Context
    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        #?---------------------- Status chart ----------------------?#
        #? Status amount
        # Get the amount of patients in each status with .count()
        vaccinated_amount = Patient.objects.filter(status='vaccinated').count()
        infected_amount = Patient.objects.filter(status='infected').count()
        uci_amount = Patient.objects.filter(status='uci').count()
        recuperated_amount = Patient.objects.filter(status='recuperated').count()

        # Sum all the patients in each status to get the total
        total_amount = vaccinated_amount + infected_amount +  uci_amount + recuperated_amount 

        # Pass the amounts through context
        context['vaccinated'] = vaccinated_amount
        context['infected'] = infected_amount
        context['uci'] = uci_amount
        context['recuperated'] = recuperated_amount
        context['total'] = total_amount

        #? Status porcentages
        # Calculate the porcentage for each amount using the helper function chart_porcentage 
        # (wich saves it in a list)
        porcentages = chart_porcentage(vaccinated_amount, infected_amount, uci_amount, recuperated_amount)
        vaccinated_porcentage = porcentages[0]
        infected_porcentage = porcentages[1]
        uci_porcentage = porcentages[2]

        # Pass the porcentages through context
        context['vaccinated_porcentage'] = vaccinated_porcentage
        context['infected_porcentage'] = infected_porcentage
        context['uci_porcentage'] = uci_porcentage
        #?-----------------------------------------------------------?#
         
        #?---------------------- Infected chart ----------------------?#
        #? Infected amount
        # Get the queryset with patients amounts grouped by ubication and
        # ordered from highest to lowest
        infected_by_ubication_raw = (Patient.objects.filter(status='infected').values('ubication')
                                 .annotate(ubication_count=Count('ubication'))
                                 .order_by('-ubication_count')                        
                          )

        # Loop through the first 6 values in the queryset (3 ubications and 3 amounts)
        # and append the values in a list
        infected_by_ubication = []
        for ubication in infected_by_ubication_raw:
                infected_by_ubication.append(Ubication.objects.get(id=ubication['ubication']))
                infected_by_ubication.append(ubication['ubication_count'])
                if len(infected_by_ubication) == 6:
                    break

        # Calculate the rest of the infected (total - top 3)
        other_infected = infected_amount - infected_by_ubication[1] - infected_by_ubication[3] - infected_by_ubication[5]

        # Pass the list generated and the rest of infected through context
        context['infected_by_ubication'] = infected_by_ubication
        context['other_infected'] = other_infected

        #? Infected porcentages
        # Calculate the porcentage for each amount using the helper function chart_porcentage 
        # (wich saves it in a list)
        porcentages = chart_porcentage(infected_by_ubication[1], infected_by_ubication[3], infected_by_ubication[5], other_infected)
        infected_one_porcentage = porcentages[0]
        infected_two_porcentage = porcentages[1]
        infected_three_porcentage = porcentages[2]

        # Pass the porcentages through context
        context['infected_one_porcentage'] = infected_one_porcentage
        context['infected_two_porcentage'] = infected_two_porcentage
        context['infected_three_porcentage'] = infected_three_porcentage
        #?-----------------------------------------------------------?#

        return context
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

        #?---------------------- Ubication table ----------------------?#
        #? Ubication not infected amounts
        not_infected_1 = (infected_by_ubication[0].poblation) - (infected_by_ubication[1])
        not_infected_2 = (infected_by_ubication[2].poblation) - (infected_by_ubication[3])
        not_infected_3 = (infected_by_ubication[4].poblation) - (infected_by_ubication[5])

        #? Ubication infected porcentages
        # Calculate the porcentage for each amount using the helper function chart_porcentage 
        # (wich saves it in a list)

        porcentages_1 = chart_porcentage(infected_by_ubication[1], not_infected_1, decimals=2)
        infected_u_1 = porcentages_1[0]
        porcentages_2 = chart_porcentage(infected_by_ubication[3], not_infected_2, decimals=2)
        infected_u_2 = porcentages_2[0]
        porcentages_3 = chart_porcentage(infected_by_ubication[5], not_infected_3, decimals=2)
        infected_u_3 = porcentages_3[0]

        #? Vaccinated amount
        vaccinated_1 = (Patient.objects.filter(status='vaccinated', ubication=infected_by_ubication[0]).count())
        vaccinated_2 = (Patient.objects.filter(status='vaccinated', ubication=infected_by_ubication[2]).count())
        vaccinated_3 = (Patient.objects.filter(status='vaccinated', ubication=infected_by_ubication[4]).count())

        #? Not vaccinated amount
        not_vaccinated_1 = (infected_by_ubication[0].poblation) - (Patient.objects.filter(status='vaccinated', ubication=infected_by_ubication[0]).count())
        not_vaccinated_2 = (infected_by_ubication[2].poblation) - (Patient.objects.filter(status='vaccinated', ubication=infected_by_ubication[2]).count())
        not_vaccinated_3 = (infected_by_ubication[4].poblation) - (Patient.objects.filter(status='vaccinated', ubication=infected_by_ubication[4]).count())

        #? Ubication vaccinated porcentages
        # Calculate the porcentage for each amount using the helper function chart_porcentage 
        # (wich saves it in a list)

        porcentages_4 = chart_porcentage(vaccinated_1, not_vaccinated_1, decimals=2)
        print(vaccinated_1)
        print(not_vaccinated_1)
        vaccinated_u_1 = porcentages_4[0]
        porcentages_5 = chart_porcentage(vaccinated_2, not_vaccinated_2, decimals=2)
        vaccinated_u_2 = porcentages_5[0]
        porcentages_6 = chart_porcentage(vaccinated_3, not_vaccinated_3, decimals=2)
        vaccinated_u_3 = porcentages_6[0]

        # Pass the porcentages through context
        context['infected_u_1'] = infected_u_1
        context['infected_u_2'] = infected_u_2
        context['infected_u_3'] = infected_u_3
        context['vaccinated_u_1'] = vaccinated_u_1
        context['vaccinated_u_2'] = vaccinated_u_2
        context['vaccinated_u_3'] = vaccinated_u_3
        #?-----------------------------------------------------------?#


        return context
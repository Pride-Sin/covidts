# Django imports
from django.db import models
# Local imports
from ubications.models import Ubication
from users.models import User

# Create your models here.
class Patient(models.Model):
    dni = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birth = models.DateField(max_length=8)
    risk = models.BooleanField(default=False)
    STATUS_CHOICES = (
    ('vaccinated','Vaccinated'),
    ('infected', 'Infected'),
    ('uci','UCI'),
    ('recuperated','Recuperated'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    ubication = models.ForeignKey(Ubication, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.dni

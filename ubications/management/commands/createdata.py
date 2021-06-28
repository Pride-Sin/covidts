# Django imports
from ubications.models import Ubication
from django.core.management.base import BaseCommand
import random
# Faker imports
from faker import Faker
import faker.providers
# Local imports
from patients.models import Patient
from users.models import User

STATUS_CHOICES = [
    "vaccinated",
    "infected",
    "uci",
    "recuperated",
]

UBICATIONS_LIST = [5,7,8,9,11]

class Provider(faker.providers.BaseProvider):
    
    def status(self):
        return self.random_element(STATUS_CHOICES)

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        
        fake = Faker(["es_ES"])
        fake.add_provider(Provider)

        #!print(fake.status())

        for _ in range(300):
            dni = random.randint(15000000, 50000000)
            first_name = fake.first_name()
            last_name = fake.last_name()
            birth = fake.date_of_birth()
            risk = fake.pybool()
            status = fake.status()
            ubication = Ubication.objects.get(id=random.choice(UBICATIONS_LIST))
            supervisor = User.objects.get(id=random.randint(3, 6))

            Patient.objects.create(dni=dni, first_name=first_name, last_name=last_name, birth=birth, 
                                   risk=risk, status=status, ubication=ubication, supervisor=supervisor)
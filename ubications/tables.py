# Local imports
import django_tables2 as tables
from .models import Ubication


class UbicationTable(tables.Table):
    class Meta:
        model = Ubication
        fields = ("id", "city", "province", "poblation")
        attrs = {
                 'class': 'table',
                 'thead' : {'class': 'thead-dark'}
                }
        
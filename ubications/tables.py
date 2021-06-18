# Tables2 imports
import django_tables2 as tables
from django_tables2.utils import A
# Local imports
from .models import Ubication


class UbicationTable(tables.Table):
    T1     = '''<a type="button" href="{% url 'delete-ubication' record.pk %}" class="btn btn-danger">Edit</a>'''
    T2     = '''<a type="button" href="{% url 'delete-ubication' record.pk %}" class="btn btn-danger">Delete</a>'''
    edit   = tables.TemplateColumn(T1, orderable=False)
    delete = tables.TemplateColumn(T2, orderable=False)
    class Meta:
        model = Ubication
        fields = ("id", "city", "province", "poblation")
        attrs = {
                 'class': 'table',
                 'thead' : {'class': 'thead-dark'}
                }
        
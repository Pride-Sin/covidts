# Tables2 imports
import django_tables2 as tables
from django_tables2.tables import Table
from django_tables2.utils import A
# Local imports
from .models import Patient


class PatientTable(tables.Table):
    T1     = '''<a type="button" href="{% url 'edit-patient' record.pk %}" class="btn btn-danger">Edit</a>'''
    T2     = '''<a type="button" href="{% url 'delete-patient' record.pk %}" class="btn btn-danger">Delete</a>'''
    edit   = tables.TemplateColumn(T1, orderable=False)
    delete = tables.TemplateColumn(T2, orderable=False)

    class Meta:
        model = Patient
        fields = ("id", "dni", "first_name", "last_name", "risk", "status", "ubication", "supervisor")
        attrs = {
                 'class': 'table',
                 'thead' : {'class': 'thead-dark'}
                }
        
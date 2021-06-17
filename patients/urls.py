# Django imports
from django.urls import path
# Local imports
from .views import PatientCreateView, PatientListView

urlpatterns = [
    path('patient/add', PatientCreateView.as_view(), name='add-patient'),
    path('patients', PatientListView.as_view(), name='patients'),
]

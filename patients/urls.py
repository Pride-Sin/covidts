# Django imports
from django.urls import path
# Local imports
from .views import PatientCreateView

urlpatterns = [
    path('patient/add', PatientCreateView.as_view(), name='add-patient'),
]

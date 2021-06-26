# Django imports
from django.urls import path
# Local imports
from .views import PatientCreateView, PatientListView, PatientEditView, PatientDeleteView

urlpatterns = [
    path('patient/add', PatientCreateView.as_view(), name='add-patient'),
    path('patient/<int:pk>/delete', PatientDeleteView.as_view(), name='delete-patient'),
    path('patient/<int:pk>/edit', PatientEditView.as_view(), name='edit-patient'),
    path('patients', PatientListView.as_view(), name='patients'),
]

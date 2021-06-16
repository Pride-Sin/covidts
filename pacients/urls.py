# Django imports
from django.urls import path
# Local imports
from .views import PacientCreateView

urlpatterns = [
    path('pacient/add', PacientCreateView.as_view(), name='add-pacient'),
]

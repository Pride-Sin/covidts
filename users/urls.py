# Django imports
from django.urls import path
# Local imports
from .models import AuthView

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
]

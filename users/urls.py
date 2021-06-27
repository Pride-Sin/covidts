# Django imports
from django.urls import path
# Local imports
from .views import AuthView

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
]

# Django imports
from django.urls import path
# Local imports
from ubications.views import UbicationCreateView

urlpatterns = [
    path('ubication/add', UbicationCreateView.as_view(), name='add-ubication'),
]

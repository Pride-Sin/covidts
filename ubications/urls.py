# Django imports
from django.urls import path
# Local imports
from .views import UbicationCreateView, UbicationListView

urlpatterns = [
    path('ubication/add', UbicationCreateView.as_view(), name='add-ubication'),
    path('ubications', UbicationListView.as_view(), name='ubications'),
]

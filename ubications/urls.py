# Django imports
from django.urls import path
# Local imports
from .views import UbicationCreateView, UbicationListView, UbicationDeleteView

urlpatterns = [
    path('ubication/add', UbicationCreateView.as_view(), name='add-ubication'),
    path('ubication/<int:pk>/delete', UbicationDeleteView.as_view(), name='delete-ubication'),
    path('ubications', UbicationListView.as_view(), name='ubications'),
]

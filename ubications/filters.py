# Local imports
import django_filters
from .models import Ubication

class UbicationFilter(django_filters.FilterSet):
    #id = django_filters.CharFilter(field_name='id', lookup_expr='exact')
    #city = django_filters.CharFilter(field_name='city', lookup_expr='iexact')
    #province = django_filters.NumberFilter(field_name='province', lookup_expr='iexact')
    #poblation = django_filters.NumberFilter(field_name='poblation', lookup_expr='exact')
    class Meta:
        model = Ubication
        fields = {
            'id': ['exact'],
            'city': ['icontains'],
            'province': ['icontains'],
            'poblation': ['icontains'],
        }
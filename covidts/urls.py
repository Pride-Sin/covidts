# Django imports
from django.contrib import admin
from django.urls import path, include
# Local imports
from .views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    #path('', include('users.urls')),
    path('', include('patients.urls')),
    path('', include('ubications.urls')),
]

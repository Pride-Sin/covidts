# src/users/admin.py
# Django imports
from django.contrib import admin
# Local imports
from .models import Pacient

admin.site.register(Pacient)
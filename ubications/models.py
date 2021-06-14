# Django imports
from django.db import models


class Ubication(models.Model):
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=30)
    poblation = models.CharField(max_length=30)

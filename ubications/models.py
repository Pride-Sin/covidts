# Django imports
from django.db import models


class Ubication(models.Model):
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=30)
    poblation = models.IntegerField()


    def __str__(self):
        ubication = self.city + ", " + self.province
        return ubication

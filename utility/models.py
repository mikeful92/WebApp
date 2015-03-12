__author__ = 'Mike'

from django.db import models


class ElectricConsumption(models.Model):
    service_address = models.CharField(max_length=200)
    service_city = models.CharField(max_length=50)
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    kwh_consumption = models.IntegerField(null=True)
    location = models.CharField(max_length=200)

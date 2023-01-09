from django.db import models

# Create your models here.


class Cctv (models.Model):
    latitude = models.CharField(null=True, max_length=100)
    longtitude = models.CharField(null=True, max_length=100)
    address = models.CharField(null=True, max_length=200)

class PoliceOffice (models.Model):
    name = models.CharField(null=True, max_length=50)
    latitude = models.CharField(null=True, max_length=100)
    longtitude = models.CharField(null=True, max_length=100)
    address = models.CharField(null=True, max_length=200)
    category = models.CharField(null=True, max_length=50)
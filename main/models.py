from django.db import models


class city(models.Model):
    region = models.CharField(max_length=250)
    name = models.CharField(max_length=250)


from django.db import models

# Create your models here.

class familia (models.Model):
    name = models.CharField(max_length=100)
    age = models.FloatField()
    married = models.BooleanField()
    birth = models.DateField()
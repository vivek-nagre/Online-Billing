from django.db import models
from django.contrib import admin
# Create your models here.
...
class Cust_Detals(models.Model):
    id = models.AutoField(primary_key=True,)
    SR_No = models.CharField(max_length=255)
    Date = models.DateTimeField(unique=True, max_length=255)
    Cust_name = models.CharField(max_length=50)
    Mobile  = models.CharField(max_length=10)
    WeightK = models.CharField(max_length=6)
    WeightG = models.CharField(max_length=4)


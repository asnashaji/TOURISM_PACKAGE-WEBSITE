
from django.db import models
# Create your models here.
class categorydb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    discription = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="photos", null=True, blank=True)

class packagedb(models.Model):
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    hotel= models.CharField(max_length=50, null=True, blank=True)
    rate= models.IntegerField( null=True, blank=True)
    activitie = models.IntegerField( null=True, blank=True)
    disp = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="photos", null=True, blank=True)

class daysdb(models.Model):
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    days = models.IntegerField(null=True, blank=True)
    activity1=models.CharField(max_length=50, null=True, blank=True)
    disp1=models.CharField(max_length=50, null=True, blank=True)
    # activity2 = models.CharField(max_length=50, null=True, blank=True)
    # disp2 = models.CharField(max_length=50, null=True, blank=True)
    # activity1 = models.CharField(max_length=50, null=True, blank=True)
    # disp1 = models.CharField(max_length=50, null=True, blank=True)


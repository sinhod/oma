from django.db import models
from django.utils import timezone
from django import forms

# Sarjan merkitsemistä varten
class Series(models.Model):
    seriesname=models.CharField(max_length=50, unique=True)

# Teosten tiedot
class Work(models.Model):
    inseries=models.ForeignKey(Series, on_delete=models.PROTECT, null=True, blank=True)# ei saa poistaa sarjoja, joissa on jokin teos
    name=models.CharField(max_length=50, default="")
    year=models.IntegerField(default=0)
    media=models.CharField(max_length=100, default="", null=True, blank=True)
    size=models.CharField(max_length=50, default="", null=True, blank=True)
    installation=models.BooleanField(default=False)
    imagelink1=models.CharField(max_length=2090, default="", null=True, blank=True)
    imagelink2=models.CharField(max_length=2090, default="", null=True, blank=True)
    imagelink3=models.CharField(max_length=2090, default="", null=True, blank=True)
    videolink=models.CharField(max_length=2090, default="", null=True, blank=True)
    instagramlink=models.CharField(max_length=2090, default="", null=True, blank=True)
    collaboration=models.CharField(max_length=100, default="", null=True, blank=True)
    timestamp=models.DateTimeField(default=timezone.now, null=True, blank=True)
    def __str__(self):
        return f"{self.name} {self.year}"
    

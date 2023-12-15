from django.db import models
from django.utils import timezone
from django import forms

# Sarjan merkitsemistä varten
class Series(models.Model):
    seriesname=models.CharField(max_length=50, unique=True)

# Teosten tiedot
class Work(models.Model):
    inseries=models.ForeignKey(Series, on_delete=models.PROTECT, null=True, blank=True)# ei saa poistaa sarjoja, joissa on jokin teos
    name=models.CharField(max_length=50, default="") #pakollinen
    year=models.IntegerField(default=0) #pakollinen
    media=models.CharField(max_length=100, default="", null=True, blank=True)
    size=models.CharField(max_length=50, default="", null=True, blank=True)
    installation=models.BooleanField(default=False) #pakollinen
    imagelink1=models.CharField(max_length=200, default="") #pakollinen
    imagelink2=models.CharField(max_length=200, default="", null=True, blank=True)
    imagelink3=models.CharField(max_length=200, default="", null=True, blank=True)
    videolink=models.CharField(max_length=200, default="", null=True, blank=True)
    instagramlink=models.CharField(max_length=200, default="", null=True, blank=True)
    collaboration=models.CharField(max_length=100, default="", null=True, blank=True)
    ownedby=models.CharField(max_length=100, default="", null=True, blank=True)
    photographer=models.CharField(max_length=100, default="", null=True, blank=True)
    timestamp=models.DateTimeField(default=timezone.now, null=True, blank=True)
    showonline=models.BooleanField(default=True) #Pakollinen
    def __str__(self): #Django administration sivua varten
        return f"{self.name} {self.year}"
    
class About(models.Model):
    name=models.CharField(max_length=20, default="Esittelyteksti") #pakollinen
    text=models.CharField(max_length=2500, default="Työnalla...") #pakollinen
    def __str__(self): #Django administration sivua varten
        return f"{self.name}"
    

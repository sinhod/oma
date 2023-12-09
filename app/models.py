from django.db import models
from django.utils import timezone

# Teosten tiedot
class Work(models.Model):
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

class Contact(models.Model):
    # Yhteydenottajan tiedot ja viestin sisältö
    sendersName=models.CharField(max_length=50, default="lähettäjän nimi")
    sendersMessage=models.CharField(max_length=1000, default="lähettäjän viesti")
    sendersEmail=models.CharField(max_length=50, default="lähettäjän email")
    sendersPhonenumber=models.CharField(max_length=50, default="lähettäjän puh.nro")
    # Kuittausviesti yhteydenottajalle
    messageForSender=models.CharField(max_length=1000, default="")
    # Ilmoitus tulleesta viestistä
    message=models.CharField(max_length=1000, default="")
    # Oma email
    email=models.CharField(max_length=50, default="vastaanottajan email")
    timestamp=models.DateTimeField(default=timezone.now, null=True, blank=True)
    def __str__(self):
        return f"{self.sendersName}"
    
class Series(models.Model):
    seriesName=models.CharField(max_length=50, default="sarjan nimi")
from django.db import models

# Teosten tiedot
class Work(models.Model):
    name=models.CharField(max_length=50, default="teoksen nimi")
    year=models.IntegerField(default=0)
    media=models.CharField(max_length=100, default="tekniikka", null=True, blank=True)
    installation=models.BooleanField(default=False)
    imageLink_1=models.CharField(max_length=2090, default="", null=True, blank=True)
    imageLink_2=models.CharField(max_length=2090, default="", null=True, blank=True)
    imageLink_3=models.CharField(max_length=2090, default="", null=True, blank=True)
    imageLink_4=models.CharField(max_length=2090, default="", null=True, blank=True)
    videoLink=models.CharField(max_length=2090, default="", null=True, blank=True)
    instagramLink=models.CharField(max_length=2090, default="", null=True, blank=True)
    collaboration=models.CharField(max_length=100, default="", null=True, blank=True)
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
    def __str__(self):
        return f"{self.sendersName}"
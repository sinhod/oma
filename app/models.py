from django.db import models

# Teosten tiedot
class work(models.Model):
    name=models.CharField(max_length=50, default="teoksen nimi")
    year=models.IntegerField(default=0)
    media=models.CharField(max_length=100, default="tekniikka")
    imageLink_1=models.CharField(max_length=2090, default="kuvalinkki")

# Installaatioiden tiedot
class Installation(models.Model):
    installationName=models.CharField(max_length=50, default="installaation nimi")
    collaboration=models.CharField(max_length=100, default="")
    year=models.IntegerField(default=0)
    media=models.CharField(max_length=100, default="tekniikka")
    imageLink_1=models.CharField(max_length=2090, default="")
    imageLink_2=models.CharField(max_length=2090, default="")
    imageLink_3=models.CharField(max_length=2090, default="")
    imageLink_4=models.CharField(max_length=2090, default="")
    videoLink=models.CharField(max_length=2090, default="")
    instagramLink=models.CharField(max_length=2090, default="")

class contact(models.Model):
    # Yhteydenottajan tiedot ja viestin sisältö
    sendersName=models.CharField(max_length=50, default="lähettäjän nimi")
    sendersMessage=models.CharField(max_length=1000, default="lähettäjän viesti")
    sendersEmail=models.CharField(max_length=50, default="lähettäjän email")
    sendersPhonenumber=models.IntegerField(default="lähettäjän puh.nro")
    # Kuittausviesti yhteydenottajalle
    messageForSender=models.CharField(max_length=1000, default="")
    # Ilmoitus tulleesta viestistä
    messageForRecipient=models.CharField(max_length=1000, default="")
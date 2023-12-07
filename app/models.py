from django.db import models

# Maalaukset, kollaasit, piirustukset yms.
class work(models.Model):
    name=models.CharField(max_length=50, default="")
    year=models.IntegerField(default=0)
    media=models.CharField(max_length=100, default="")
    imageLink_1=models.CharField(max_length=2090, default="")

# Installaatiot
class Installation(models.Model):
    installationName=models.CharField(max_length=50, default="")
    year=models.IntegerField(default=0)
    media=models.CharField(max_length=100, default="")
    collaboration=models.CharField(max_length=100, default="")
    imageLink_1=models.CharField(max_length=2090, default="")
    imageLink_2=models.CharField(max_length=2090, default="")
    imageLink_3=models.CharField(max_length=2090, default="")
    imageLink_4=models.CharField(max_length=2090, default="")
    videoLink=models.CharField(max_length=2090, default="")
    instagramLink=models.CharField(max_length=2090, default="")

class contact(models.Model):
    # Yhteydenottajan tiedot ja viestin sisältö
    sendersMessage=models.CharField(max_length=1000, default="")
    sendersName=models.CharField(max_length=50, default="")
    sendersEmail=models.CharField(max_length=50, default="")
    sendersPhonenumber=models.IntegerField(max_length=20, default="")
    # Kuittausviesti yhteydenottajalle
    messageForSender=models.CharField(max_length=1000, default="")
    # Ilmoitus tulleesta viestistä
    messageForRecipient=models.CharField(max_length=1000, default="")
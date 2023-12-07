from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

def landingview(request):
    variable = "Tämä on merkkijono"
    context = {'x': variable}
    return render(request, 'landingpage.html', context)

def workview(request):
    variable_name = "Tämä on merkkijono"
    variable_year = "Tämä on numerojono"
    variable_media = "Tämä on merkkijono"
    variable_imageLink = "Tämä on merkkijono"
    context = {'a': variable_name, 'b':variable_year, 'c':variable_media, 'd':variable_imageLink}
    return render(request, 'workpage.html', context)

def installationview(request):
    variable_name = "Tämä on merkkijono"
    variable_collaboration = "Tämä on merkkijono"
    variable_year = "Tämä on numerojono"
    variable_media = "Tämä on merkkijono"
    variable_imageLink = "Tämä on merkkijono"
    context = {'a': variable_name, 'b':variable_collaboration, 'c':variable_year, 'd':variable_media, 'e':variable_imageLink}
    return render(request, 'installationpage.html', context)

def aboutview(request):
    return render(request, 'aboutpage.html')

def contactview(request):
    variable_sendersName = "Tämä on merkkijono"
    variable_sendersMessage = "Tämä on merkkijono"
    variable_sendersEmail = "Tämä on merkkijono"
    variable_sendersPhonenumber = "Tämä on numerojono"
    variable_sendersMessage = "Tämä on merkkijono"
    variable_messageForSender = "Tämä on merkkijono"
    variable_messageForMe = "Tämä on merkkijono"
    context = {'a': variable_sendersName, 'b':variable_sendersMessage, 'c':variable_sendersEmail, 'd':variable_sendersMessage, 'e':variable_messageForSender, 'f':variable_messageForMe}
    return render(request, 'contactpage.html', context)

def cvview(request):
    variable = "Tämä on merkkijono"
    context = {'a': variable}
    return render(request, 'cvpage.html', context)

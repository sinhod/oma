from django.shortcuts import render
from django.http import HttpResponse

from .models import Work, Contact, Series

def index(request):
    return render(request, "index.html")

def landingview(request):
    variable = "Tämä on merkkijono"
    context = {'x': variable}
    return render(request, 'landingpage.html', context)

def workview(request):
    w = Work.objects.all().order_by('-year')
    context = { 'works': w }
    return render(request, 'workpage.html', context)

def installationview(request):
    i = Work.objects.all().order_by('-year')
    context = { 'installations': i }
    return render(request, 'installationpage.html', context)

def aboutview(request):
    return render(request, 'aboutpage.html')

def contactview(request):
    sendersName = "Tämä on merkkijono"
    sendersMessage = "Tämä on merkkijono"
    sendersEmail = "Tämä on merkkijono"
    sendersPhonenumber = "Tämä on numerojono"
    sendersMessage = "Tämä on merkkijono"
    messageForSender = "Tämä on merkkijono"
    messageForMe = "Tämä on merkkijono"
    context = {'a':sendersName, 'b':sendersMessage, 'c':sendersEmail, 'd':sendersMessage, 'e':messageForSender, 'f':messageForMe}
    return render(request, 'contactpage.html', context)

def cvview(request):
    variable = "Tämä on merkkijono"
    context = {'a': variable}
    return render(request, 'cvpage.html', context)

def modifyingview(request):
    w = Work.objects.all().order_by('-year')
    context = { 'works': w }
    return render(request, 'modifyingpage.html', context)





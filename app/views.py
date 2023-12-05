from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the app index.")

def index(request):
    return render(request, "index.html")
def landingview(request):
    return render(request, 'landingpage.html')
def aboutview(request):
    return render(request, 'aboutpage.html')
def contactview(request):
    return render(request, 'contactpage.html')
def cvview(request):
    return render(request, 'cvpage.html')
def installationview(request):
    return render(request, 'installationpage.html')
def workview(request):
    return render(request, 'workpage.html')

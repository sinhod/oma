from django.shortcuts import render, redirect
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

def addview(request):
    a = request.POST['name']
    b = request.POST['year']
    c = request.POST['media']
    if c == "":
        c = None
    d = request.POST['size']
    if d == "":
        d = None
    e = request.POST['installation']
    f = request.POST['imagelink1']
    if f == "":
        f = None
    g = request.POST['imagelink2']
    if g == "":
        g = None
    h = request.POST['imagelink3']
    if h == "":
        h = None
    i = request.POST['videolink']
    if i == "":
        i = None
    j = request.POST['instagramlink']
    if j == "":
        j = None
    k = request.POST['collaboration']
    if k == "":
        k = None
    Work(name = a, year = b, media = c, size = d, installation = e,
         imagelink1 = f, imagelink2 = g, imagelink3 = h, videolink = i, instagramlink = j, collaboration = k).save()
    return redirect(request.META['HTTP_REFERER'])

# Teoksen poistamista varten
def confirmdeletework(request, id):
    work=Work.objects.get(id=id)
    context={'w': work}
    return render(request,"confirmdeletework.html", context)
def deletework(request, id):
    Work.objects.get(id=id).delete()
    return redirect(modifyingview)

# Teoksen tietojen muokkaamista varten
def edit_work_get(request, id):
    work=Work.objects.get(id=id)
    context={'w': work}
    return render(request,"edit_work.html", context)
def edit_work_post(request, id):
    work=Work.objects.get(id=id)
    work.name=request.POST['name']
    work.year=request.POST['year']
    work.media=request.POST['media']
    work.size=request.POST['size']
    work.installation=request.POST['installation']
    work.imagelink1=request.POST['imagelink1']
    work.imagelink2=request.POST['imagelink2']
    work.imagelink3=request.POST['imagelink3']
    work.videolink=request.POST['videolink']
    work.instagramlink=request.POST['instagramlink']
    work.collaboration=request.POST['collaboration']
    work.save()
    return redirect(modifyingview)







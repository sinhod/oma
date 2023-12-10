from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Work, Series

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

def cvview(request):
    variable = "Tämä on merkkijono"
    context = {'a': variable}
    return render(request, 'cvpage.html', context)

def contactview(request):
    return render(request, 'contactpage.html')

def modifyingview(request):
    if not request.user.is_authenticated: 
         return render(request, 'loginpage.html')
    else:
        w = Work.objects.all().order_by('-year')
        s = Series.objects.all()
        context = { 'works': w , 'series': s }
        return render(request, 'modifyingpage.html', context)

def addview(request):
    if not request.user.is_authenticated: 
         return render(request, 'loginpage.html')
    else:
        a = request.POST['name']
        ab = request.POST['seriesname']
        if ab == "":
            ab = None
        else:
            ab = Series.objects.filter(seriesname=ab).first()
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
        Work(name = a, inseries = ab, year = b, media = c, size = d, installation = e,
            imagelink1 = f, imagelink2 = g, imagelink3 = h, videolink = i, instagramlink = j, collaboration = k).save()
        return redirect(modifyingview)

def addseriesview(request):
    print('addseriesview')
    if not request.user.is_authenticated: 
         return render(request, 'loginpage.html')
    else:
        sname = request.POST['seriesname']
        Series(seriesname=sname).save()
        return redirect(modifyingview)

# Teoksen poistamista varten
def confirmdeletework(request, id):
    if not request.user.is_authenticated: 
         return render(request, 'loginpage.html')
    else:
        work=Work.objects.get(id=id)
        context={'w': work}
        return render(request,"confirmdeletework.html", context)
def deletework(request, id):
    if not request.user.is_authenticated: 
         return render(request, 'loginpage.html')
    else:
        Work.objects.get(id=id).delete()
        return redirect(modifyingview)

# Teoksen tietojen muokkaamista varten
def edit_work_get(request, id):
    if not request.user.is_authenticated: 
         return render(request, 'loginpage.html')
    else:
        work=Work.objects.get(id=id)
        context={'w': work}
        return render(request,"edit_work.html", context)
def edit_work_post(request, id):
        if not request.user.is_authenticated: 
         return render(request, 'loginpage.html')
        else:
            work=Work.objects.get(id=id)
            work.name=request.POST['name']
            work.year=request.POST['year']
            work.installation=request.POST['installation']

            # Tallennetaan "tyhjä arvo "tietokantaan None arvona. (None=Pythonin muuttuja, jolla ei ole sisältöä)
            # Web-lomake antaa tyhjänä string:inä, jos käyttäjä ei anna arvoa.
            # Muutetaan siis tyhjä string None:ksi
            instalink = request.POST['instagramlink']
            if instalink == "":
                instalink = None

            med=request.POST['media']
            if med == "":
                med = None

            siz=request.POST['size']
            if siz == "":
                siz = None

            imglink1=request.POST['imagelink1']
            if imglink1 == "":
                imglink1 = None

            imglink2=request.POST['imagelink2']
            if imglink2 == "":
                imglink2 = None

            imglink3=request.POST['imagelink3']
            if imglink3 == "":
                imglink3 = None

            vlink=request.POST['videolink']
            if vlink == "":
                vlink = None

            coll=request.POST['collaboration']
            if coll == "":
                coll = None

            work.instagramlink=instalink
            work.media=med
            work.size=siz
            work.imagelink1=imglink1
            work.imagelink2=imglink2
            work.imagelink3=imglink3
            work.videolink=vlink
            work.collaboration=coll
            
            work.save()
            return redirect(modifyingview)

# Login toimintoa varten

# def landingview(request):
#     return render(request, 'landingpage.html')


def loginview(request):
     return render (request, "loginpage.html")

def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää? Käytetään djangon omaa authenticate-metodia
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Kutsutaan suoraan landingview.html
        w = Work.objects.all().order_by('-year')
        context = { 'works': w }
        return render(request, 'modifyingpage.html', context)
    
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')

# Logout action. Käytetään jangon omaa logout-metodia, jotka poistaa kirjautumistiedon systeemistä
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')
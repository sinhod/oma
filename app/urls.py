from django.urls import path

from . import views

from .views import landingview, aboutview, contactview,cvview, installationview, workview, modifyingview

urlpatterns = [
    path("", landingview),
    path("about/", aboutview),
    path("contact/", contactview),
    path("cv/", cvview),
    path("installation/", installationview),
    path("work/", workview),
    path("modify/", modifyingview)
]
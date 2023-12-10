from django.urls import path

from . import views

from .views import landingview, aboutview, cvview, installationview, workview, \
      modifyingview, addview, deletework, confirmdeletework, edit_work_get, edit_work_post, \
      loginview, login_action, logout_action, contactview

urlpatterns = [
    path("", landingview),
    path("about/", aboutview),
    path("cv/", cvview),
    path("installation/", installationview),
    path("work/", workview),
    path("modify/", modifyingview),
    path('add/', addview),
    path('deletework/<int:id>/', deletework),
    path('confirm-deletework/<int:id>/', confirmdeletework),
    path('edit-work-get/<int:id>/', edit_work_get),
    path('edit-work-post/<int:id>/', edit_work_post),

    # Kirjautumistoimintoa varten
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    # Yhteydenottoa varten
    path('contact/', contactview)

]
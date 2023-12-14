from django.contrib import admin
from app.models import Work, Series, About

# Register your models here.

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass
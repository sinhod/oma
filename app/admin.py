from django.contrib import admin
from app.models import Work

# Register your models here.

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass
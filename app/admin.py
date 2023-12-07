from django.contrib import admin
from app.models import Work, Installation, Contact

# Register your models here.

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass

@admin.register(Installation)
class InstallationAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
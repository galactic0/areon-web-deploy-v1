from django.contrib import admin
from .models import Contact, trackingapi
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']

class trackingapiAdmin(admin.ModelAdmin):
    list_display = ['id','distance','date_time']

admin.site.register(Contact,ContactAdmin)

admin.site.register(trackingapi)
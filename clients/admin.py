from django.contrib import admin

from clients.models import Client

# Register your models here.

class Clients(admin.ModelAdmin):
    list_display = ("id", 'name', "cpf", 'rg', "phone", "active")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("active",)
    list_editable = ("active",)
    list_per_page = 10
    ordering = ('name',)
    
    
admin.site.register(Client, Clients)

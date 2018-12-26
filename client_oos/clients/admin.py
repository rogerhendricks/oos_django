from django.contrib import admin

# Register your models here.
from .models import Client, Oos

admin.site.register(Client)
admin.site.register(Oos)

admin.site.site_header = "Super Hero Clinic Admin"
admin.site.site_title = "Super Hero Admin Portal"
admin.site.index_title = "Welcome to Super Chero Client Portal"

class OosInLine(admin.TabularInline):
	model = Oos 

class ClientAdmin(admin.ModelAdmin):
	inlines = [OosInLine,]
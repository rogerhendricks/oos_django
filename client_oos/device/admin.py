from django.contrib import admin

# Register your models here.
from .models import Device, Lead

admin.site.site_header = "Super Hero Clinic Admin"
admin.site.site_title = "Super Hero Admin Portal"
admin.site.index_title = "Welcome to Super Hero Client Portal"

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    model = Lead


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_type', 'device_man', 'device_name']
    search_fields = ['device_type', 'device_man', 'device_name']

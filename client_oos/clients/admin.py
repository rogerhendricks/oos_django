from django.contrib import admin

# Register your models here.
from .models import Client, Oos, Doc


admin.site.register(Oos)

admin.site.site_header = "Super Hero Clinic Admin"
admin.site.site_title = "Super Hero Admin Portal"
admin.site.index_title = "Welcome to Super Hero Client Portal"


class OosInLine(admin.StackedInline):
    model = Oos
    ordering = ('-oos_date',)
    extra = 0

@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [
        OosInLine,
    ]
    list_display = ['record_number', 'first_name', 'last_name']
    search_fields = ['last_name', 'record_number']

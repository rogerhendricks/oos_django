from django import forms
from .models import Client, Oos


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('record_number','first_name', 'last_name', 'dob', 'device_man', 'device_name', 'implant_date', 'device_serial')


class OosForm(forms.ModelForm):
   class Meta:
        model = Oos
        fields = ('content', 'oos_type', 'batt_volt', 'oos_date')


class SearchForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('last_name',)

class Big():
    pass
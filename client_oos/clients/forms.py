from django import forms
from .models import Client, Oos, Doc


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields= ['record_number','first_name', 'last_name', 'dob', 'device_man', 'device_name', 'implant_date', 'device_serial', 'bol_voltage','eri_voltage']


class OosForm(forms.ModelForm):
   class Meta:
        #model = Oos
        #fields = ('client','content', 'oos_type', 'batt_volt', 'oos_date')
        model = Oos
        fields = [
                    'client',
                    'oos_type',
                    'oos_date',
                    'batt_volt',
                    'content',
                    ]
        labels = {
            'oos_type': 'Service Type',
            'oos_date': 'Service Date',
            'batt_volt': 'Battery Voltage',
            'content': 'Comments',
            }
        widgets = {
            'client': forms.HiddenInput()
            }
        


class SearchForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('last_name',)


class DocForm(forms.ModelForm):
    class Meta: 
        model = Doc
        fields = ('first_name','last_name','address','phone_1','phone_2')
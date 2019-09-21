from django import forms
from .models import Client, Oos, Doc, Procedure


    
class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields= ['record_number','first_name', 'last_name','dob', 'device_man', 'device_name', 'implant_date', 'device_serial', 'bol_voltage','eri_voltage','doctors']
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker', 'type':'date'}),
            'implant_date': forms.DateInput(attrs={'class': 'datepicker', 'type':'date'}),
            'doctors': forms.CheckboxSelectMultiple()
            }
    


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
                    'batt_chg_time',
                    'paced_percent_ra',
                    'paced_percent_rv',
                    'paced_percent_lv',
                    'intra_amp_ra',
                    'pace_imp_ra',
                    'pace_thr_ra',
                    'pace_thr_pw_ra',
                    'intra_amp_rv',
                    'pace_imp_rv',
                    'pace_thr_rv',
                    'pace_thr_pw_rv',
                    'shock_imp_rv',
                    'shock_imp_svc',
                    'content',
                    ]
        labels = {
            'oos_type': 'Service Type',
            'oos_date': 'Service Date',
            'batt_volt': 'Battery Voltage',
            'batt_chg_time': 'Battery Charge Time',
            'paced_percent_ra': 'RA Pacing Percentage',
            'paced_percent_rv': 'RV Pacing Percentage',
            'paced_percent_lv': 'LV Pacing Percentage',
            'intra_amp_ra':'RA Sensing Amplitude',
            'pace_imp_ra':'RA Pacing Impedance',
            'pace_thr_ra':'RA Pacing Theshold',
            'pace_thr_pw_ra':'RA Pacing Pulse Width',
            'intra_amp_rv':'RV Sensing Amplitude',
            'pace_imp_rv':'RV Pacing Impedance',
            'pace_thr_rv':'RV Pacing Theshold',
            'pace_thr_pw_rv':'RV Pacing Pulse Width',
            'shock_imp_rv':'RV Shock Pacing Impedance',
            'shock_imp_svc':'SVC Shock Pacing Impedance',
            'content': 'Comments',
            }
        widgets = {
            'client': forms.HiddenInput(),
            'oos_date': forms.DateInput(attrs={'class': 'datepicker', 'type':'date'})
            }
        

class SearchForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('last_name',)


class DocForm(forms.ModelForm):
    class Meta: 
        model = Doc
        fields = ('doc_type','first_name','last_name','str_address','ct_address','pc_address','st_address','phone_1','phone_2', 'email')
        labels = {
            'doc_type': 'Doctor Type',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'str_address': 'Street',
            'ct_address': 'City',
            'pc_address':'Post Code',
            'st_address': 'State',
            'phone_1': 'Phone 1',
            'phone_2': 'Phone 2',
            'email': 'Email'
            }

class ProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = {'client','procedure_date','procedure_type','content'}
        labels = {
            'procedure_type':'Procedure Type',
            'procedure_date': 'Procedure Date',
            'content': 'Comments'
        }
        widgets = {
            'client': forms.HiddenInput()
            }
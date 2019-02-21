from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView, View
from django.views.generic.detail import SingleObjectMixin
from .models import Client, Oos, Doc
from django.http import HttpResponse
from .utils import render_to_pdf
from django.shortcuts import redirect
from .forms import SearchForm, ClientForm, OosForm, DocForm
from django.contrib import messages
from django.urls import	reverse_lazy, reverse
from django.db.models import Q
from django.utils import timezone
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .utils import render_to_pdf
from django_weasyprint import WeasyTemplateResponseMixin
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
#from crispy_forms.helper import FormHelper





# Clients
class ClientView(ListView):
    template_name = 'clients/index.html'
    context_object_name = 'all_clients'
    paginate_by = 10

    def get_queryset(self):
        return Client.objects.all()


class ClientDetailView(DetailView, DeleteView, CreateView):
    model = Client
    template_name = 'clients/detail.html'
    success_url = reverse_lazy('client:index')
    #fields= ['record_number','first_name', 'last_name', 'dob', 'device_man', 'device_name', 'implant_date', 'device_serial', 'bol_voltage','eri_voltage']
    form_class = ClientForm
  
  

class ClientCreate(CreateView):
    model = Client
    form_class = ClientForm


class ClientUpdate(UpdateView):
    model = Client
    #fields= ['record_number','first_name', 'last_name', 'dob', 'device_man', 'device_name', 'implant_date', 'device_serial', 'bol_voltage','eri_voltage']
    form_class = ClientForm
    template_name_suffix = '_update_form'


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client:index')


class SearchList(ListView):
    template_name = 'clients/client_search.html'
    model = Client
    context_object_name = 'results_list'

    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = Client.objects.filter(Q(last_name__icontains=search)|Q(first_name__icontains=search)|Q(record_number__icontains=search))
        return queryset







# Services
class OosView(SingleObjectMixin, ListView):
    template_name = 'clients/services_index.html'
    context_object_name = 'all_services'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Client.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['client'] = self.object
        return context

    def get_queryset(self):
        return self.object.oos_set.all()


class OosDetailView(DetailView):
    template_name = 'clients/oos_detail.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Oos.objects.filter(id=self.kwargs.get('pk')).prefetch_related('client')
        return queryset


class OosCreate(CreateView):
    template_name = 'clients/oos_create.html'
    model = Oos
    fields = ['client','oos_date', 'oos_type', 'batt_volt','content', ]
    #form_class = OosForm


class OosUpdateView(UpdateView):
    model = Oos
    fields = ['oos_date','oos_type', 'batt_volt', 'content']
    template_name_suffix = '_update_form'


class OosDelete(DeleteView):
    model = Oos
    success_url = reverse_lazy('client:index')


# search services from OosListView
class OosSearchList():
    template_name = ''
    model = Oos
    context_object_name = ''

    def get_queryset(self):
        pass


# adding service render to pdf xhtmltopdf2
class GeneratePdf(View):

    def get(self, request, *args, **kwargs):
        queryset = Oos.objects.filter(id=self.kwargs.get('pk')).values()[0]
        pdf = render_to_pdf('clients/pdf/service_render.html', queryset)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "service_%s.pdf" %(datetime.datetime.now())
            content = "inline; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class OosDetailPdf(DetailView):
    template_name = 'clients/pdf/pdf_detail.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Oos.objects.filter(id=self.kwargs.get('pk')).select_related('client').prefetch_related('client__doctors')

        #queryset = Oos.objects.filter(id=self.kwargs.get('pk')).prefetch_related('client')
        return queryset


class OosCreateNew(CreateView):
    template_name = 'clients/oos_create.html'
    form_class = OosForm

    def get_initial(self, **kwargs):
        initial = super(OosCreateNew, self).get_initial()
        initial['client'] = self.kwargs.get('pk')
        return initial










# Doctors

class DoctorCreate(CreateView):
    #model = Doc
    template_name = 'clients/doctors/doctor_new.html'
    form_class = DocForm
    success_url = reverse_lazy('client:index')


class DoctorView(ListView):
    template_name = 'clients/doctors/doctor_index.html'
    context_object_name = 'all_doctors'
    paginate_by = 10

    def get_queryset(self):
        return Doc.objects.all()



class DoctorDetailView(DetailView, DeleteView, CreateView):
    model = Doc
    template_name = 'clients/doctors/doctor_detail.html'
    success_url = reverse_lazy('client:doctor_index')
    #fields= ['record_number','first_name', 'last_name', 'dob', 'device_man', 'device_name', 'implant_date', 'device_serial', 'bol_voltage','eri_voltage']
    form_class = DocForm

class DoctorDelete(DeleteView):
    model = Doc
    success_url = reverse_lazy('client:doctor_index')

class DoctorUpdate(UpdateView):
    model = Doc
    #fields= ['record_number','first_name', 'last_name', 'dob', 'device_man', 'device_name', 'implant_date', 'device_serial', 'bol_voltage','eri_voltage']
    form_class = DocForm

class DoctorSearchList(ListView):
    template_name = 'clients/doctors/doctor_search.html'
    model = Doc
    context_object_name = 'results_list'

    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = Doc.objects.filter(Q(last_name__icontains=search)|Q(first_name__icontains=search))
        return queryset


#def send_email(request):
#    subject = request.POST.get('subject', '')
#    message = request.POST.get('message', '')
#    from_email = request.POST.get('from_email', '')
#    if subject and message and from_email:
#        try:
#            send_mail(subject, message, from_email, ['admin@example.com'])
#        except BadHeaderError:
#            return HttpResponse('Invalid header found.')
#        return HttpResponseRedirect('/contact/thanks/')
#    else:
#        # In reality we'd use a form class
#        # to get proper validation errors.
#        return HttpResponse('Make sure all fields are entered and valid.')
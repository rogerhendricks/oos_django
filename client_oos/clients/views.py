from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView, View
from django.views.generic.detail import SingleObjectMixin
from .models import Client, Oos
from django.shortcuts import redirect
from .forms import SearchForm, ClientForm, OosForm
from django.contrib import messages
from django.urls import	reverse_lazy, reverse
from django.db.models import Q
from django.utils import timezone
import datetime
from django.http import HttpResponse
from .utils import render_to_pdf

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
    fields= ['record_number','first_name', 'last_name', 'dob', 'device_man', 'device_name', 'implant_date', 'device_serial']



class ClientCreate(CreateView):
    model = Client
    fields= ['record_number','first_name', 'last_name', 'dob', 'device_man', 'device_name', 'implant_date', 'device_serial']


class ClientUpdate(UpdateView):
    model = Client
    fields= ['record_number','first_name', 'last_name', 'dob', 'device_man', 'device_name', 'implant_date', 'device_serial']
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
        queryset = Oos.objects.filter(id=self.kwargs.get('pk'))
        return queryset


class OosCreate(CreateView):
    template_name = 'clients/oos_create.html'
    model = Oos
    fields = ['client','content', 'oos_type', 'batt_volt', 'oos_date' ]


class OosUpdateView(UpdateView):
    model = Oos
    fields = ['content', 'oos_type', 'batt_volt', 'oos_date']
    template_name_suffix = '_update_form'


class OosDelete(DeleteView):
    model = Oos
    success_url = reverse_lazy('client:index')


#search services from OosListView
class OosSearchList():
    template_name = ''
    model = Oos
    context_object_name = ''

    def get_queryset(self):
        pass


# adding service render to pdf
class GeneratePdf(View):

    def get(self, request, *args, **kwargs):
        queryset = Oos.objects.filter(id=self.kwargs.get('pk')).values('oos_type', 'batt_volt')
        data = {
            'oos_type' : Oos.oos_type, 
            'batt' : Oos.batt_volt,
        }
        pdf = render_to_pdf('clients/pdf/service_render.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Client, Oos
from django.shortcuts import redirect
from .forms import SearchForm, ClientForm
from django.contrib import messages
from django.urls import	reverse_lazy
from django.db.models import Q 



# Clients
class ClientView(ListView):
    template_name = 'clients/index.html'
    context_object_name = 'all_clients'
    
    def get_queryset(self):
        return Client.objects.all()


class DetailView(DetailView):
    model = Client
    template_name = 'clients/detail.html'


class ClientCreate(CreateView):
    model = Client
    fields= ['record_number','first_name', 'last_name', 'dob']


class ClientUpdate(UpdateView):
    model = Client
    fields= ['record_number', 'first_name', 'last_name', 'dob']
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
		queryset = Client.objects.filter(Q(last_name__icontains = search)|Q(first_name__icontains = search))
		return queryset


# Services 		

class OosView(ListView):
    template_name = 'clients/services_index.html'
    context_object_name = 'all_services'

    def get_queryset(self):
        return Oos.objects.all()

		
class OosDetailView(DetailView):
    template_name = ''
    model = Oos 


class OosCreate(CreateView):
    model = Oos 
    feilds = []


class OosUpdateView(UpdateView):
    model = Oos 
    fields = []
    template_name_suffix = ''


class OosDelete(DeleteView):
    model = Oos 
    success_url = reverse_lazy("")


class OosSearchList():
    template_name = ''
    model = Oos 
    context_object_name = ''

    def get_queryset(self):
        pass

		












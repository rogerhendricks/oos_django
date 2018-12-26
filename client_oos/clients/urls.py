from django.urls import path, re_path
from django.conf.urls import url
from . import views
from clients.views import ClientView, DetailView, ClientCreate, ClientDelete, ClientUpdate, SearchList, OosView

app_name = 'client'


urlpatterns = [
    path('', ClientView.as_view(), name='index'),
    path('<int:pk>/detail/', DetailView.as_view(), name='detail'),

    # /clients/add/
    path('client/new/', ClientCreate.as_view(), name='client_add'),
    path('client/<int:pk>/delete', ClientDelete.as_view(), name='client_delete'),
    path('client/<int:pk>/update', ClientUpdate.as_view(), name='client_update'),
    path('client/<int:pk>/details', DetailView.as_view(), name='client_detail'),
    path('client/search', SearchList.as_view(), name='search'),
    path('client/service', OosView.as_view(), name='service'),
]




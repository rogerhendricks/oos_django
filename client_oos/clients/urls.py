from django.urls import path, re_path
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from clients.views import ClientView, ClientDetailView, ClientCreate, ClientDelete, ClientUpdate, SearchList, OosView, OosDetailView, OosCreate, OosUpdateView, OosDelete, GeneratePdf, MyModelPrintView 
from django.conf import settings


app_name = 'client'


urlpatterns = [
    path('', ClientView.as_view(), name='index'),
    path('<int:pk>/detail/', ClientDetailView.as_view(), name='detail'),

    # /clients/add-delete-update-search
    path('client/new/', ClientCreate.as_view(), name='client_add'),
    path('client/<int:pk>/delete', ClientDelete.as_view(), name='client_delete'),
    path('client/<int:pk>/update', ClientUpdate.as_view(), name='client_update'),
    path('client/<int:pk>/details', ClientDetailView.as_view(), name='client_detail'),
    path('client/search', SearchList.as_view(), name='search'),
    #/services
    path('client/<int:pk>/service', OosView.as_view(), name='service'),
    path('client/<int:client.pk>/service/<int:pk>/detail', OosDetailView.as_view(), name='service_detail'),
    path('client/<int:client.pk>/service/<int:pk>/detail/pdf/', GeneratePdf.as_view(), name='service_pdf'),
    path('client/service/add', OosCreate.as_view(), name='service_add'),
    path('client/<int:client.pk>/service/<int:pk>/update', OosUpdateView.as_view(), name='service_update'),
    path('client/<int:pk>/service/<int:oos.pk>/delete', OosDelete.as_view(), name='service_delete'),
    path('client/<int:client.pk>/service/<int:pk>/detail/pdf/', MyModelPrintView.as_view(), name='weasyservice_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

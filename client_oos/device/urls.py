from django.urls import path, re_path
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from clients.views import DeviceView
from django.conf import settings


app_name = 'device'


urlpatterns = [
    path('device', DeviceView.as_view(), name='device_index'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
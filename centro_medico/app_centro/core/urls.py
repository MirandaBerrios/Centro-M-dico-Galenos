from django.urls import path
from django.views.generic import base
from .views import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home , name='home'),
    path('login', login , name ="login"),
    path('registrar', registrar , name ='registrar'),
    path('reserva' , reserva , name="reserva"),
    path('perfil', perfil , name="perfil"),
    path('contacto', contacto, name="contacto"),
    path('mod_paciente/<action>/<rut>', mod_paciente , name = "mod_paciente"),
    path('cerrar_sesion', cerrar_sesion , name = "cerrar_sesion"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

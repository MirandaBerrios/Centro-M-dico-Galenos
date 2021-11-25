from django.urls import path
from django.views.generic import base
from .views import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home , name='home'),
    path('login', login , name ="login"),
    path('registrar', registrar , name ='registrar'),
    path('reserva' , reserva , name="reserva"),
    
    
]

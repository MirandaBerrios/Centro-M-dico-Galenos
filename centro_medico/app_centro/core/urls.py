from django.urls import path
from .views import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
]

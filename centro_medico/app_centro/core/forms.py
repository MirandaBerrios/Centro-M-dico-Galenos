from django import forms
from django.forms import ModelForm, fields , Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class IniciarSesionForm(ModelForm):
    # user_rut = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}), label="rut")
    # contrasena = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        model = Paciente
        fields = ['rut_paciente', 'contrasena']


class CustomUserCreationForms(UserCreationForm):
    last_name1 = forms.CharField( max_length=50, required=False, label="Apellido paterno")
    last_name2 = forms.CharField( max_length=50, required=False, label= "Apellido materno")
    address = forms.CharField(max_length=100 , required = False, label="Dirección")
    class Meta:
        model = User
        fields = ["username", "first_name" , "last_name1" , "last_name2" , "address" ,"email" , "password1", "password2"]        
    
class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ["rut_paciente" , "primer_nombre" , "segundo_nombre" , "apellido_paterno" , "apellido_materno" , "fecha_nacimiento" , "genero" , 
        "direccion" , "email" , "telefono" , "contrasena" , "contrasena2"]
from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def base(request):
    return render (request , "base.html")

def home(request):
    return render (request , "home.html")

def reserva(request):
    return render (request , "reserva.html")

def nav(request):
    return render (request, "nav.html")
    
def footer (request):
    return render (request, "footer.html")

def validar(user , pas):
    usuario = "no"
    try: 
        usuario = Paciente.objects.get(rut_paciente = user , contrasena = pas)
    except: 
         mensaje = "La clave ingresada es incorrecta"
         return False   

    return True   
           

def login(request):
    data = {"mesg": "", "form": IniciarSesionForm()}
    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            rut_paciente = request.POST.get("rut_paciente")
            contrasena = request.POST.get("contrasena")
            isValidate = validar(rut_paciente , contrasena )         
            print(isValidate)
            if isValidate is True:
                return redirect(to = 'home')
                # if user.is_active:
                #     login(request, user)
                #     return redirect(to="")
                # else:
                #     data["mesg"] = "¡La cuenta o la password no son correctos!"
                #     print(data)
                #     print("1         uno")
            else:
                data["mesg"] = "¡La cuenta o la password no son correctos!"
                print(data)
                print("2         dos")
    return render(request, "login.html", data)


def registrar(request):
    data = {'form': PacienteForm}
    if request.method == 'POST':
        formulario = PacienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # implementar las sweet alert
            # messages.success(request, "Te has registrado correctamente")
            # guardar la darta que hará login
            user = authenticate(username=formulario.cleaned_data["rut_paciente"], password=formulario.cleaned_data["contrasena"])
            # pasar los parámetros que harán login
            login(request, user)
            # redirigir al home
            return redirect(to="")
    return render(request , 'registrar.html', data)      
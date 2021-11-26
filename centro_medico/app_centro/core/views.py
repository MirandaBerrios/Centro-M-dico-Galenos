from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages

def show_perfil(request):
    flag = False
    try: 
        aux = request.COOKIES.get('rut_paciente')
        print(aux)
        if len(aux)> 0:
            flag = True
            return flag
        else: 
            flag = False
            return flag   
    except: 
        return flag

def home(request):
    data = {"flag": show_perfil(request)}
    return render(request, "home.html" , data)
        

def reserva(request):
    return render (request , "reserva.html")

def perfil (request ):
    rut_paciente = request.COOKIES.get('rut_paciente')
    print(rut_paciente)
    user = Paciente.objects.all().filter(rut_paciente = rut_paciente)
    data = {"paciente": user , "flag": show_perfil(request)}
    return render(request, "perfil.html" , data )

def validar(user , pas):
    usuario = "no"
    try: 
        usuario = Paciente.objects.get(rut_paciente = user , contrasena = pas)
    except: 
         mensaje = "La clave ingresada es incorrecta"
         return False   

    return True   

def mod_paciente(request , action , rut):
    data = {"message": "" , "form": PacienteForm , "action" : action , "rut_paciente": rut }
    if action == 'upd':
        object = Paciente.objects.get(rut_paciente = rut)
        if request.method == "POST":
            form = PacienteForm(data = request.POST , files = request.FILES , instance = object)
            if form.is_valid():
                form.save()
                messages.success(request , "¡El usuario ha sido actualizado!")
                return redirect(to = "perfil")
        data["form"] = PacienteForm(instance= object)  
    elif action == 'del':
        try:
            Paciente.objects.get(rut_paciente=rut).delete()
            messages.error(request, "¡Usuario eliminado correctamente!")
            return redirect(to="home")
        except:
            messages.error(request,"¡El usuario ya estaba eliminado!")
            return render(request,"home.html")  
    return render(request , "mod_paciente.html" , data )            

def login(request ):
    data = {"mesg": "", "form": IniciarSesionForm()}
    if request.method == "POST":
        form = IniciarSesionForm(request.POST)
        if form.is_valid:
            rut_paciente = request.POST.get("rut_paciente")
            contrasena = request.POST.get("contrasena")
            isValidate = validar(rut_paciente , contrasena )         
            print(isValidate)
            if isValidate is True:
                obj = redirect(to = 'home')
                obj.set_cookie('rut_paciente',rut_paciente)
                return obj
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



def contacto(request):
    return render(request, "contacto.html")

def cerrar_sesion(request): 
    obj = redirect(to= 'home')
    obj.delete_cookie('rut_paciente')
    return obj   
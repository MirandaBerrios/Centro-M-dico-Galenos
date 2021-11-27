from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages

def show_perfil(request):
    #Con esta funcion creamos una bandera que nos retornará False si no hay 
    #datos en las cookies y true si tenemos valores en las cookies
    #la función la inyectaremos en cada una de las view, para agregarlos al 
    # diccionario data , con el fin de mostrar el botón perfil cargado en templates/nav
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
    #Obtendremos el cookie del nav, para renderizar toda la info que está en la 
    # base de datos mediantes el object.all
    rut_paciente = request.COOKIES.get('rut_paciente')
    print(rut_paciente)
    user = Paciente.objects.all().filter(rut_paciente = rut_paciente)
    data = {"paciente": user , "flag": show_perfil(request)}
    return render(request, "perfil.html" , data )

def validar(user , pas):
    #Intentamos obtener una registro de la base de datos que cumpla la condición que 
    #el rut_paciente y la contrasena coincidan, en caso contrasrio usuario no tendrá
    #valor y arrojará error, por eso está encapsulado en un try catch

    usuario = "no"
    try: 
        usuario = Paciente.objects.get(rut_paciente = user , contrasena = pas)
    except: 
         mensaje = "La clave ingresada es incorrecta"
         return False   

    return True   

def mod_paciente(request , action , rut):
    #modificar  paciente , creamos un diccionario con los datos ingresados
    # action gatillará la seción update en caso de que se reciba dicho parámetro
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
            obj = redirect(to= 'home')
            obj.delete_cookie('rut_paciente')
            messages.error(request, "¡Usuario eliminado correctamente!")
            return obj
        except:
            messages.error(request,"¡El usuario ya estaba eliminado!")
            return render(request,"home.html")  
    return render(request , "mod_paciente.html" , data )            

def login(request ):
    data = {"messages": "", "form": IniciarSesionForm()}
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
                data["messages"] = "¡La cuenta o la password no son correctos!"
                return obj
            else:
                data["messages"] = "¡La cuenta o la password no son correctos!"
                messages.error(request, "dios es grande")
             
    return render(request, "login.html", data)


def registrar(request):
    data = {'form': PacienteForm , 'messages': "" }
    if request.method == 'POST':
        formulario = PacienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request , "Te haz registrado exitosamente")
            return redirect(to="login")
        else: 
            messages.warning(request, 'Credenciales inválidas')
    return render(request , 'registrar.html', data)      



def contacto(request):
    return render(request, "contacto.html")

def cerrar_sesion(request): 
    obj = redirect(to= 'home')
    obj.delete_cookie('rut_paciente')
    data = {"messages":"Te haz desconectado de tu sesión"}
    return obj
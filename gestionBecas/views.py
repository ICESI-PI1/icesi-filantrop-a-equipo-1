from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Rol
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def editar_firstname(request, username):
    usuario = get_object_or_404(User, username=username)

    if request.method == 'POST':
        nuevo_first_name = request.POST.get('first_name')
        if nuevo_first_name:
            usuario.first_name = nuevo_first_name
            usuario.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'El campo first_name no puede estar vacío.'})

    return JsonResponse({'success': False, 'error': 'Método no permitido.'}, status=405)





def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'asignar_roles.html', {'usuarios': usuarios})


def asignar_roles(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario')
        rol_id = request.POST.get('rol')
        
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            rol = Rol.objects.get(id=rol_id)
            
            # Asignar el rol al usuario (dependiendo de cómo esté diseñado tu modelo de datos)
            usuario.roles.add(rol)
            
            return redirect('asignar_roles')
        except Usuario.DoesNotExist or Rol.DoesNotExist:
            # Manejar errores aquí si es necesario
            pass
    
    usuarios = Usuario.objects.all()
    roles = Rol.objects.all()
    
    return render(request, 'asignar_roles.html', {'usuarios': usuarios, 'roles': roles})

def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contraseña')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario ha iniciado sesión correctamente
            first_name = user.first_name  
            login(request, user)
            
            #return redirect('app_login:inicio') 
            if first_name == "Sin Rol":
                return redirect('app_login:inicio_sin_rol')  # Reemplaza 'ruta_pagina_uno' con la URL de tu primera página.
            elif first_name == "Administrador":
                return redirect('app_login:inicio')
            elif first_name == "Donante":
                return redirect('app_login:inicio_donante')
            elif first_name == "Filantropia":
                return redirect('app_login:inicio')
            elif first_name == "Beneficiario":
                return redirect('app_login:inicio')
            
            
        else:
            # El inicio de sesión ha fallado, puedes mostrar un mensaje de error
            error_message = "Nombre de usuario o contraseña incorrectos"
            return render(request, 'login.html', {'error_message': error_message})
    else :
        return render(request, 'login.html') # Redirige a la URL con nombre 'inicio' en la aplicación 'app_login'


def inicio_view(request):

    return render(request, 'inicio.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app_login:login')  # Redirige a la página principal después del registro
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')

def perfil(request):
    return render(request, 'perfil.html') 

def gestion_programa_beca(request):
    return render(request, 'gestion_programa_beca.html')
def inicio_SinRol(request):
        return render(request, 'inicio_SinRol.html')
    
def inicio_Donante(request):
        return render(request, 'inicio_Donante.html')

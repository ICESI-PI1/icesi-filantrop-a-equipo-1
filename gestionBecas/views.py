from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Rol

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


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contraseña')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario ha iniciado sesión correctamente
            login(request, user)
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
            return redirect('login.html')  # Redirige a la página principal después del registro
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')
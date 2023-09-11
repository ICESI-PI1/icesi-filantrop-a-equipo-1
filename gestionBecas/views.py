from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

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


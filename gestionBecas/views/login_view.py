from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('usuario')
        password = request.POST.get('contraseña')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # El usuario ha iniciado sesión correctamente
            first_name = user.first_name
            login(request, user)
            
            # Lógica para redirigir según el tipo de usuario (primer nombre)
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


from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    pass
AUTH_USER_MODEL = 'app_login.CustomUser'

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['contraseña']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('home')
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')

    return render(request, 'login.html')

from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('login/', views.user_login, name='login'),
   
]


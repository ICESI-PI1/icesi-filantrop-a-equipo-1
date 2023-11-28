from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User

class ListaUsuariosView(View):
    def get(self, request):
        usuarios = User.objects.all()
        return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

from django.views import View
from django.shortcuts import render

class InicioSinRolView(View):
    def get(self, request):
        return render(request, 'inicio_SinRol.html')


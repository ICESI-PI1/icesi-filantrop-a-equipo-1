from django.views import View
from django.shortcuts import render

class InicioDonanteView(View):
    def get(self, request):
        return render(request, 'inicio_Donante.html')

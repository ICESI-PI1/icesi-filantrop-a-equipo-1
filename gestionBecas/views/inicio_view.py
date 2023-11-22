from django.views import View
from django.shortcuts import render

class InicioView(View):
    def get(self, request):
        return render(request, 'inicio.html')

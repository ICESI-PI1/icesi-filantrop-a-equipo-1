from django.views import View
from django.shortcuts import render

class PerfilView(View):
    def get(self, request):
        return render(request, 'perfil.html')

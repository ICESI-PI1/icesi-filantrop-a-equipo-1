from django.views import View
from django.shortcuts import render

class GestionInformeBecaView(View):
    def get(self, request):
        return render(request, 'gestion_informe_beca.html')

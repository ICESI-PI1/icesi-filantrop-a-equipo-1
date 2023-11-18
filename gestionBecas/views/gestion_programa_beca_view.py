from django.views import View
from django.shortcuts import render

class GestionProgramaBecaView(View):
    def get(self, request):
        return render(request, 'gestion_programa_beca.html')

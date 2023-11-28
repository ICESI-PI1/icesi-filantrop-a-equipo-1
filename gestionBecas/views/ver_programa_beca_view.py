from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
import programas_beca
from gestionBecas.models import ProgramaBeca

class VerProgramaBecaView(View):
    def get(self, request):
        programas = ProgramaBeca.objects.all()
        return render(request, 'ver_programa_beca.html', {'programas': programas})

    def post(self, request):
        programa_id = request.POST.get('nombre')
        programa_seleccionado = get_object_or_404(ProgramaBeca, id=programa_id)
        return render(request, 'ver_programa_beca.html', {'programas': programas_beca, 'programa_seleccionado': programa_seleccionado})

from django.views import View
from django.shortcuts import render, redirect
from gestionBecas.models import ProgramaBeca
import programas_beca

class SeleccionarProgramaBecaView(View):
    def get(self, request):
        programas = ProgramaBeca.objects.all()
        return render(request, 'seleccionar_programa_beca.html', {'programas': programas})

    def post(self, request):
        programa_id = request.POST.get('programa_id')
        if programa_id:
            return redirect('app_login:editar_programa_beca', programa_id=programa_id)
        return render(request, 'seleccionar_programa_beca.html', {'programas': programas_beca})

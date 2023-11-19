from django.views import View
from django.shortcuts import render, redirect
from gestionBecas.models import ProgramaBeca
import programas_beca

class Seleccionar2ProgramaBecaView(View):
    def get(self, request):
        programas = ProgramaBeca.objects.all()
        return render(request, 'seleccionar_pb2.html', {'programas': programas})

    def post(self, request):
        programa_id = request.POST.get('programa_id')
        if programa_id:
            return redirect('app_login:registrar_cronograma', programa_id=programa_id)
        return render(request, 'seleccionar_pb2.html', {'programas': programas_beca})

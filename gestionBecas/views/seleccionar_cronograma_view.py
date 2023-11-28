from django.views import View
from django.shortcuts import render, redirect
from gestionBecas.forms import CronogramaForm
from gestionBecas.models import Cronograma

class SeleccionarCronogramaView(View):
    def get(self, request):
        cronogramas = Cronograma.objects.all()
        return render(request, 'seleccionar_cronograma.html', {'cronogramas': cronogramas})

    def post(self, request):
        cronograma_id = request.POST.get('cronograma_id')
        if cronograma_id:
            return redirect('app_login:editar_cronograma', cronograma_id=cronograma_id)
        return render(request, 'seleccionar_cronograma.html', {'cronogramas': CronogramaForm})

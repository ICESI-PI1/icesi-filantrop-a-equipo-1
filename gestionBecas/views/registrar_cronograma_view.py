from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from gestionBecas.models import ProgramaBeca
from gestionBecas.forms import CronogramaForm

class CrearCronogramaView(View):
    def get(self, request, programa_id):
        programa_beca = get_object_or_404(ProgramaBeca, id=programa_id)
        form = CronogramaForm(initial={'programa_becas': programa_beca})
        return render(request, 'registrar_cronograma.html', {'form': form})

    def post(self, request, programa_id):
        form = CronogramaForm(request.POST)
        if form.is_valid():
            cronograma_obj = form.save(commit=False)
            cronograma_obj.programa_becas = get_object_or_404(ProgramaBeca, id=programa_id)
            cronograma_obj.save()
            return HttpResponseRedirect(reverse('app_login:inicio'))  # Redirige a la página de éxito después de crear el cronograma
        return render(request, 'registrar_cronograma.html', {'form': form})

from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from gestionBecas.models import Cronograma, ProgramaBeca
from gestionBecas.forms import CronogramaForm

class EditarCronogramaView(View):
    def get(self, request, cronograma_id):
        cronograma_seleccionado = get_object_or_404(Cronograma, id=cronograma_id)
        programas = ProgramaBeca.objects.all()
        form = CronogramaForm(instance=cronograma_seleccionado)
        return render(request, 'editar_cronograma.html', {'cronograma_seleccionado': cronograma_seleccionado, 'programas': programas, 'form': form})

    def post(self, request, cronograma_id):
        cronograma_seleccionado = get_object_or_404(Cronograma, id=cronograma_id)
        programas = ProgramaBeca.objects.all()
        form = CronogramaForm(request.POST, instance=cronograma_seleccionado)
        success_message = ""
        if form.is_valid():
            form.save()
            success_message = "Los cambios se han guardado exitosamente."
        else:
            print("Errores en el formulario:", form.errors)
        return render(request, 'editar_cronograma.html', {'cronograma_seleccionado': cronograma_seleccionado, 'programas': programas, 'success_message': success_message, 'form': form})

from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from gestionBecas.models import ProgramaBeca
from gestionBecas.forms import ProgramaBecaForm
from django.contrib.auth.models import User

class EditarProgramaBecaView(View):
    def get(self, request, programa_id):
        programa_seleccionado = get_object_or_404(ProgramaBeca, id=programa_id)
        programas = ProgramaBeca.objects.all()
        usuarios_donantes = User.objects.filter(first_name='Donante')
        form = ProgramaBecaForm(instance=programa_seleccionado)
        return render(request, 'editar_programa_beca.html', {'programa_seleccionado': programa_seleccionado, 'programas': programas, 'usuarios_donantes': usuarios_donantes, 'form': form})

    def post(self, request, programa_id):
        programa_seleccionado = get_object_or_404(ProgramaBeca, id=programa_id)
        programas = ProgramaBeca.objects.all()
        usuarios_donantes = User.objects.filter(first_name='Donante')
        form = ProgramaBecaForm(request.POST, instance=programa_seleccionado)
        success_message = ""
        if form.is_valid():
            form.save()
            success_message = "Los cambios se han guardado exitosamente."
        else:
            print("Errores en el formulario:", form.errors)
        return render(request, 'editar_programa_beca.html', {'programa_seleccionado': programa_seleccionado, 'programas': programas, 'usuarios_donantes': usuarios_donantes, 'success_message': success_message, 'form': form})

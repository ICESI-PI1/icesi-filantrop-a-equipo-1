from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from gestionBecas.models import ProgramaBeca

class EliminarProgramaBeca(View):
    def get(self, request):
        # Mostrar la lista de cronogramas
        programas = ProgramaBeca.objects.all()
        context = {'programas_beca': programas}
        return render(request, 'eliminar_programa_beca.html', context)

class EliminarProgramaBecaIndividual(View):
    def delete(self, request, programa_id):
        try:
            programa = ProgramaBeca.objects.get(id=programa_id)
            programa.delete()
            return JsonResponse({'success': True, 'message': 'programa beca eliminado con éxito.'})
        except ProgramaBeca.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El programa beca no existe.'})
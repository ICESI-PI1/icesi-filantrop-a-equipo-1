from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from gestionBecas.models import Cronograma

class EliminarCronograma(View):
    def get(self, request):
        # Mostrar la lista de cronogramas
        cronogramas = Cronograma.objects.all()
        context = {'cronogramas': cronogramas}
        return render(request, 'eliminar_cronograma.html', context)

class EliminarCronogramaIndividual(View):
    def delete(self, request, cronograma_id):
        try:
            cronograma = Cronograma.objects.get(id=cronograma_id)
            cronograma.delete()
            return JsonResponse({'success': True, 'message': 'Cronograma eliminado con éxito.'})
        except Cronograma.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'El cronograma no existe.'})
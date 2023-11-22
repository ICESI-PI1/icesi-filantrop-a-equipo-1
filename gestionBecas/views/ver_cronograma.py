from django.shortcuts import render, get_object_or_404
from django.views import View
from gestionBecas.models import Cronograma



class VerCronogramaView(View):
    def get(self, request):
        cronogramas = Cronograma.objects.all()
        return render(request, 'ver_cronograma.html', {'cronogramas': cronogramas})

    def post(self, request):
        cronograma_id = request.POST.get('nombre')
        cronograma_seleccionado = get_object_or_404(Cronograma, id=cronograma_id)
        cronogramas = Cronograma.objects.all()  # Agrega esta línea para obtener la lista de cronogramas
        return render(request, 'ver_cronograma.html', {'cronogramas': cronogramas, 'cronograma_seleccionado': cronograma_seleccionado})

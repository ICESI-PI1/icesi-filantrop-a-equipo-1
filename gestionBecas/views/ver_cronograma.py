# views.py

from django.shortcuts import render
from django.views import View
from gestionBecas.models import Cronograma

class VerCronogramaView(View):
    template_name = 'ver_cronograma.html'  

    def get(self, request):
        cronogramas = Cronograma.objects.all()
        context = {'cronogramas': cronogramas}
        return render(request, self.template_name, context)

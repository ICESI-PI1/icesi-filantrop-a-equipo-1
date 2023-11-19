from django.views import View
from django.shortcuts import render

class InformesyEstadisticas(View):
    def get(self, request):
        return render(request, 'informes_estadisticas.html')


from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView
from gestionBecas.models import ProgramaBeca
from django.shortcuts import get_object_or_404

class ObtenerProgramasBecaView(View):
    def get(self, request, *args, **kwargs):
        programas_beca = ProgramaBeca.objects.all().values('id', 'nombre')
        return JsonResponse(list(programas_beca), safe=False)

class DetallesProgramaBecaView(DetailView):
    model = ProgramaBeca
    template_name = 'detalles_programa_beca.html'  # Ajusta el nombre del template según tu estructura

    def render_to_response(self, context, **response_kwargs):
        programa_beca = context['programabeca']
        response_data = {
            'id': programa_beca.id,
            'nombre': programa_beca.nombre,
            'descripcion': programa_beca.descripcion,
            # Agrega más campos según sea necesario
        }
        return JsonResponse(response_data, safe=False)

    def get_object(self, queryset=None):
        id_programa_beca = self.kwargs.get('id_programa_beca')
        return get_object_or_404(ProgramaBeca, id=id_programa_beca)

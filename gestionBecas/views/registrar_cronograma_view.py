from django.views import View
from django.shortcuts import render, redirect
from gestionBecas.models import ProgramaBeca, TipoConvocatoria, Cronograma
from gestionBecas.forms import CronogramaForm

class CrearCronogramaView(View):
    def get(self, request):
        programas_beca = ProgramaBeca.objects.all()
        tipos_convocatoria = TipoConvocatoria.objects.all()
        return render(request, 'registrar_cronograma.html', {'programas_beca': programas_beca, 'tipos_convocatoria': tipos_convocatoria})

    def post(self, request):
        programa_becas = request.POST['programa_becas']
        tipo_convocatoria = request.POST['tipo_convocatoria']
        fecha_inscripciones = request.POST['fecha_inscripciones']
        fecha_cierre_inscripciones = request.POST['fecha_cierre_inscripciones']
        fecha_seleccion_aspirantes = request.POST['fecha_seleccion_aspirantes']
        fecha_entrevistas = request.POST['fecha_entrevistas']
        fecha_publicacion_beneficiarios = request.POST['fecha_publicacion_beneficiarios']

        programa_beca_obj = ProgramaBeca.objects.create(nombre=programa_becas)
        tipo_convocatoria_obj = TipoConvocatoria.objects.create(nombre=tipo_convocatoria)
        cronograma_obj = Cronograma.objects.create(
            programa_becas=programa_beca_obj,
            tipo_convocatoria=tipo_convocatoria_obj,
            fecha_inscripciones=fecha_inscripciones,
            fecha_cierre_inscripciones=fecha_cierre_inscripciones,
            fecha_seleccion_aspirantes=fecha_seleccion_aspirantes,
            fecha_entrevistas=fecha_entrevistas,
            fecha_publicacion_beneficiarios=fecha_publicacion_beneficiarios
        )

        return render(request, 'inicio.html')

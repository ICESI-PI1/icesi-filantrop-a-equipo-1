from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User
from gestionBecas.models import ProgramaBeca

class RegistrarProgramaBecaView(View):
    def get(self, request):
        usuarios = User.objects.filter(first_name='Donante')
        return render(request, 'registrar_programa_beca.html', {'usuarios': usuarios})

    def post(self, request):
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fechaInicio = request.POST.get('fechaInicio')
        fechaFin = request.POST.get('fechaFin')
        cupo = request.POST.get('cupo')
        donantes = request.POST.getlist('donantesSeleccionados')  # Obtener lista de donantes seleccionados
        coberturaEconomica = request.POST.get('coberturaEconomica')
        tipoBeca = request.POST.get('tipoBeca')
        requisitos = request.POST.get('requisitos')

        programa_beca = ProgramaBeca(
            nombre=nombre,
            descripcion=descripcion,
            fechaInicio=fechaInicio,
            fechaFin=fechaFin,
            cupo=cupo,
            donantes=', '.join(donantes),  # Convertir lista de donantes a string
            coberturaEconomica=coberturaEconomica,
            tipoBeca=tipoBeca,
            requisitos=requisitos
        )

        programa_beca.save()  # Guardar el programa de beca en la base de datos

        return render(request, 'registrar_programa_beca.html', {'success_message': 'Programa de Beca registrado exitosamente.'})

from django.contrib import admin
from .models import ProgramaBeca

class ProgramaBecaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fechaInicio', 'fechaFin', 'cupo', 'donantes', 'coberturaEconomica', 'tipoBeca', 'requisitos')

from .models import Cronograma

admin.site.register(Cronograma)

admin.site.register(ProgramaBeca, ProgramaBecaAdmin)

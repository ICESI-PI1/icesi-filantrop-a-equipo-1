from django.contrib import admin
from .models import ProgramaBeca

class ProgramaBecaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fechaInicio', 'fechaFin', 'cupo', 'donantes', 'coberturaEconomica', 'tipoBeca', 'requisitos')

# Registra el modelo ProgramaBeca con la clase ProgramaBecaAdmin personalizada
admin.site.register(ProgramaBeca, ProgramaBecaAdmin)

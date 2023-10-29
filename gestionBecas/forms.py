from django import forms
from .models import Usuario, Rol
from gestionBecas.models import ProgramaBeca


class AsignarRolForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all())
    rol = forms.ModelChoiceField(queryset=Rol.objects.all())

class ProgramaBecaForm(forms.ModelForm):
    class Meta:
        model = ProgramaBeca
        fields = ['nombre', 'descripcion', 'fechaInicio', 'fechaFin', 'cupo', 'donantes', 'coberturaEconomica', 'tipoBeca', 'requisitos']


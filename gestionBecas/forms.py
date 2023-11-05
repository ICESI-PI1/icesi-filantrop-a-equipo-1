from django import forms
from .models import Usuario, Rol, Cronograma
from gestionBecas.models import ProgramaBeca


class AsignarRolForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all())
    rol = forms.ModelChoiceField(queryset=Rol.objects.all())

class ProgramaBecaForm(forms.ModelForm):
    class Meta:
        model = ProgramaBeca
        fields = ['nombre', 'descripcion', 'fechaInicio', 'fechaFin', 'cupo', 'donantes', 'coberturaEconomica', 'tipoBeca', 'requisitos']

class CronogramaForm(forms.ModelForm):
    class Meta:
        model = Cronograma
        fields = ['programa_becas', 'tipo_convocatoria', 'fecha_inscripciones', 'fecha_cierre_inscripciones', 'fecha_seleccion_aspirantes', 'fecha_entrevistas', 'fecha_publicacion_beneficiarios']

    def __init__(self, *args, **kwargs):
        super(CronogramaForm, self).__init__(*args, **kwargs)
        self.fields['programa_becas'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_convocatoria'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_inscripciones'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_cierre_inscripciones'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_seleccion_aspirantes'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_entrevistas'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_publicacion_beneficiarios'].widget.attrs['class'] = 'form-control'
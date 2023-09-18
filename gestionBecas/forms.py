from django import forms
from .models import Usuario, Rol

class AsignarRolForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all())
    rol = forms.ModelChoiceField(queryset=Rol.objects.all())

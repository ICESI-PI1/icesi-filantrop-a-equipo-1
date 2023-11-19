from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def asignar_rol_sin_rol(sender, instance, created, **kwargs):
    if created:
        instance.first_name = "Sin Rol"
        instance.save()

class ProgramaBeca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    cupo = models.PositiveIntegerField()
    donantes = models.CharField(max_length=255)
    coberturaEconomica = models.DecimalField(max_digits=10, decimal_places=2)
    tipoBeca = models.CharField(max_length=50)
    requisitos = models.TextField()

class TipoConvocatoria(models.Model):
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre

class Cronograma(models.Model):
    programa_becas = models.ForeignKey(ProgramaBeca, on_delete=models.CASCADE)
    tipo_convocatoria = models.CharField(max_length=100, choices=[
        ('Abierta', 'Abierta'),
        ('Mixta', 'Mixta'),
        ('Cerrada', 'Cerrada'),
    ])
    fecha_inscripciones = models.DateField()
    fecha_cierre_inscripciones = models.DateField()
    fecha_seleccion_aspirantes = models.DateField()
    fecha_entrevistas = models.DateField()
    fecha_publicacion_beneficiarios = models.DateField()

    def __str__(self):
        return f'Cronograma para {self.programa_becas.nombre} - {self.tipo_convocatoria}'


class Rol(models.Model):
    nombre = models.CharField(max_length=100)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Rol)

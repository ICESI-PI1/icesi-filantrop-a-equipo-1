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


class Rol(models.Model):
    nombre = models.CharField(max_length=100)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Rol)

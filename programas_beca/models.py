from django.db import models
from django.contrib.auth.models import User

class ProgramaBeca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fechaInicio = models.DateField()  # Tipo de dato para fecha de inicio
    fechaFin = models.DateField()     # Tipo de dato para fecha de fin
    cupo = models.PositiveIntegerField()  # Tipo de dato para un número entero positivo
    donantes = models.CharField(max_length=255)  # Tipo de dato para una lista de donantes
    coberturaEconomica = models.DecimalField(max_digits=10, decimal_places=2)  # Tipo de dato para una cantidad monetaria
    tipoBeca = models.CharField(max_length=50)  # Tipo de dato para el tipo de beca
    requisitos = models.TextField()  # Tipo de dato para los requisitos

    def __str__(self):
        return self.nombre


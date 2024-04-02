from django.db import models

class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    pais = models.CharField(max_length=2) 
    telefono = models.CharField(max_length=20)
    empresa = models.CharField(max_length=100)
    empleados = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
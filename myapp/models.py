# models.py
from django.db import models

class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    rol = models.CharField(max_length=100)
    pais = models.CharField(max_length=2)
    telefono = models.CharField(max_length=20)  # Actualizado para reflejar el formato deseado
    empresa = models.CharField(max_length=200)
    empleados = models.CharField(max_length=20)
    sector = models.CharField(max_length=50)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, Correo: {self.correo}, Rol: {self.rol}, País: {self.pais}, Teléfono: {self.telefono}, Empresa: {self.empresa}, Empleados: {self.empleados}, Sector: {self.sector}"



class Respuestas(models.Model):
    respuesta_1 = models.CharField(max_length=255)
    respuesta_2 = models.CharField(max_length=255)
    respuesta_3 = models.CharField(max_length=255)
    respuesta_4 = models.CharField(max_length=255)
    respuesta_5 = models.CharField(max_length=255)
    respuesta_6 = models.CharField(max_length=255)
    respuesta_7 = models.CharField(max_length=255)
    respuesta_8 = models.CharField(max_length=255)
    respuesta_9 = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Respuestas - {self.respuesta_1}, {self.respuesta_2}, {self.respuesta_3}, {self.respuesta_4}, {self.respuesta_5}, {self.respuesta_6}, {self.respuesta_7}, {self.respuesta_8}, {self.respuesta_9}'
class Respuestasdos(models.Model):

    respuesta_10 = models.CharField(max_length=255)
    respuesta_11 = models.CharField(max_length=255)
    respuesta_12 = models.CharField(max_length=255)
    respuesta_13 = models.CharField(max_length=255)
    respuesta_14 = models.CharField(max_length=255)
    respuesta_15 = models.CharField(max_length=255)
    respuesta_16 = models.CharField(max_length=255)
    respuesta_17 = models.CharField(max_length=255)
    respuesta_18 = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Respuestasdos - {self.respuesta_10}, {self.respuesta_11}, {self.respuesta_12}, {self.respuesta_13}, {self.respuesta_14}, {self.respuesta_15}, {self.respuesta_16}, {self.respuesta_17}, {self.respuesta_18}'
class Respuestastres(models.Model):

    respuesta_19 = models.CharField(max_length=255)
    respuesta_20 = models.CharField(max_length=255)
    respuesta_21 = models.CharField(max_length=255)
    respuesta_22 = models.CharField(max_length=255)
    respuesta_23 = models.CharField(max_length=255)
    respuesta_24 = models.CharField(max_length=255)
    respuesta_25 = models.CharField(max_length=255)
    respuesta_26 = models.CharField(max_length=255)
    respuesta_27 = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Respuestasdos - {self.respuesta_19}, {self.respuesta_20}, {self.respuesta_21}, {self.respuesta_22}, {self.respuesta_23}, {self.respuesta_24}, {self.respuesta_25}, {self.respuesta_26}, {self.respuesta_27}'

class Respuestascuatro(models.Model):

    respuesta_28 = models.CharField(max_length=255)
    respuesta_29 = models.CharField(max_length=255)
    respuesta_30 = models.CharField(max_length=255)
    respuesta_31 = models.CharField(max_length=255)
    respuesta_32 = models.CharField(max_length=255)
    respuesta_33 = models.CharField(max_length=255)
    respuesta_34 = models.CharField(max_length=255)
    respuesta_35 = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Respuestasdos - {self.respuesta_28}, {self.respuesta_29}, {self.respuesta_30}, {self.respuesta_31}, {self.respuesta_32}, {self.respuesta_33}, {self.respuesta_34}, {self.respuesta_35}'

from django import forms
from .models import Registro, Respuestas, Respuestasdos


class RespuestasForm(forms.ModelForm):
    class Meta:
        model = Respuestas
        fields = '__all__'
        
class RespuestasdosForm(forms.ModelForm):
    class Meta:
        model = Respuestasdos
        fields = '__all__'

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['correo', 'nombre', 'apellidos', 'rol', 'pais', 'nombre_empresa', 'sector_negocio']
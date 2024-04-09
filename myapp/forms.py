from django import forms
from .models import Registro, Respuestas, Respuestasdos, Registromodelo

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'

class RespuestasForm(forms.ModelForm):
    class Meta:
        model = Respuestas
        fields = '__all__'
        
class RespuestasdosForm(forms.ModelForm):
    class Meta:
        model = Respuestasdos
        fields = '__all__'

class RegistromodeloForm(forms.ModelForm):
    class Meta:
        model = Registromodelo
        fields = ['correo']

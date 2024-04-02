# forms.py
from django import forms
from .models import Registro
from .models import Respuestas
from .models import Respuestasdos

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
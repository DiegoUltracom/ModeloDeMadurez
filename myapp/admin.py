from django.contrib import admin
from .models import Registro, Respuestas, Respuestasdos,Respuestastres,Respuestascuatro

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'correo', 'rol', 'pais', 'telefono', 'empresa', 'empleados', 'sector')

class RespuestasAdmin(admin.ModelAdmin):
    
    pass
class RespuestasdosAdmin(admin.ModelAdmin):
    
    pass
class RespuestastresAdmin(admin.ModelAdmin):
    
    pass
class RespuestascuatroAdmin(admin.ModelAdmin):
    
    pass


admin.site.register(Registro, RegistroAdmin)
admin.site.register(Respuestas, RespuestasAdmin)
admin.site.register(Respuestasdos, RespuestasdosAdmin)
admin.site.register(Respuestastres, RespuestastresAdmin)
admin.site.register(Respuestascuatro, RespuestascuatroAdmin)




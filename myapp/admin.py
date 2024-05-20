from django.contrib import admin
from .models import Registro, Respuestas, Respuestasdos, Respuestastres, Respuestascuatro


class RespuestasAdmin(admin.ModelAdmin):
    pass

class RespuestasdosAdmin(admin.ModelAdmin):
    pass

class RespuestastresAdmin(admin.ModelAdmin):
    pass

class RespuestascuatroAdmin(admin.ModelAdmin):
    pass

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('correo', 'nombre', 'apellidos', 'rol', 'pais', 'nombre_empresa', 'sector_negocio', 'numero_empleados', 'telefono_codigo', 'telefono_numero')

admin.site.register(Registro, RegistroAdmin)
admin.site.register(Respuestas, RespuestasAdmin)
admin.site.register(Respuestasdos, RespuestasdosAdmin)
admin.site.register(Respuestastres, RespuestastresAdmin)
admin.site.register(Respuestascuatro, RespuestascuatroAdmin)

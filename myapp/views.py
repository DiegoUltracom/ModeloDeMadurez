
import json
import gspread
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registro
from .models import Respuestas

@csrf_exempt
def home_view(request):
    if request.method == 'POST':
        try:
            # Obtén los datos del formulario
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            correo = request.POST.get('correo')
            rol = request.POST.get('rol')
            pais = request.POST.get('pais')
            telefono_codigo = request.POST.get('telefono_codigo')
            telefono_numero = request.POST.get('telefono_numero')
            nombre_empresa = request.POST.get('nombre_empresa')
            num_empleados = request.POST.get('num_empleados')
            sector_negocio = request.POST.get('sector_negocio')

          
            registro = Registro(
                nombre=nombre,
                apellidos=apellidos,
                correo=correo,
                rol=rol,
                pais=pais,
                telefono=f"{telefono_codigo} {telefono_numero}",
                empresa=nombre_empresa,
                empleados=num_empleados,
                sector=sector_negocio
            )

            # Guarda la instancia en la base de datos
            registro.save()

            # Redirige a la vista 'indexdos' después de completar el formulario
            return redirect('indexdos')

        except Exception as e:
            # Maneja cualquier otra excepción que pueda ocurrir
            error_message = f"Error: {str(e)}"
            return render(request, 'myapp/hello.html', {'error_message': error_message})
    else:
        # Si es una solicitud GET, simplemente renderiza el formulario
        return render(request, 'myapp/hello.html')

# Importa la vista 'indexdos'
def indexdos_view(request):
    return render(request, 'myapp/indexdos.html', {})


def indexseis_view(request):
    # Lógica para la vista 'indexseis'
    return render(request, 'myapp/indexseis.html', {})


# Vista para el primer formulario
# views.py

@csrf_exempt
def indextres_view(request):
    if request.method == 'POST':
        try:
            # Obtén los datos del formulario
            respuesta_1 = request.POST.get('respuesta')
            respuesta_2 = request.POST.get('respuesta2')
            respuesta_3 = request.POST.get('respuesta3')
            respuesta_4 = request.POST.get('respuesta4')
            respuesta_5 = request.POST.get('respuesta5')
            respuesta_6 = request.POST.get('respuesta6')
            respuesta_7 = request.POST.get('respuesta7')
            respuesta_8 = request.POST.get('respuesta8')
            respuesta_9 = request.POST.get('respuesta9')

            # Crea una instancia del modelo y guarda los datos
            nueva_respuesta = Respuestas(
                respuesta_1=respuesta_1,
                respuesta_2=respuesta_2,
                respuesta_3=respuesta_3,
                respuesta_4=respuesta_4,
                respuesta_5=respuesta_5,
                respuesta_6=respuesta_6,
                respuesta_7=respuesta_7,
                respuesta_8=respuesta_8,
                respuesta_9=respuesta_9
            )

            nueva_respuesta.save()

            # Redirige a la vista 'indexcuatro' después de completar el primer formulario
            return redirect('indexcuatro')

        except Exception as e:
            # Maneja cualquier otra excepción que pueda ocurrir
            error_message = f"Error: {str(e)}"
            return render(request, 'myapp/indextres.html', {'error_message': error_message})

    else:
        # Si es una solicitud GET, simplemente renderiza el formulario
        return render(request, 'myapp/indextres.html')

from .models import Respuestasdos

@csrf_exempt
def indexcuatro_view(request):
    if request.method == 'POST':
        try:
            # Obtén los datos del formulario
            respuesta_10 = request.POST.get('respuesta10')
            respuesta_11 = request.POST.get('respuesta11')
            respuesta_12 = request.POST.get('respuesta12')
            respuesta_13 = request.POST.get('respuesta13')
            respuesta_14 = request.POST.get('respuesta14')
            respuesta_15 = request.POST.get('respuesta15')
            respuesta_16 = request.POST.get('respuesta16')
            respuesta_17 = request.POST.get('respuesta17')
            respuesta_18 = request.POST.get('respuesta18')

            # Crea una instancia del modelo Respuestasdos y guarda los datos
            nueva_respuesta = Respuestasdos(
                respuesta_10=respuesta_10,
                respuesta_11=respuesta_11,
                respuesta_12=respuesta_12,
                respuesta_13=respuesta_13,
                respuesta_14=respuesta_14,
                respuesta_15=respuesta_15,
                respuesta_16=respuesta_16,
                respuesta_17=respuesta_17,
                respuesta_18=respuesta_18
            )

            nueva_respuesta.save()

            # Redirige a la vista 'indexcinco' después de completar el segundo formulario
            return redirect('indexcinco')

        except Exception as e:
            # Maneja cualquier otra excepción que pueda ocurrir
            error_message = f"Error: {str(e)}"
            return render(request, 'myapp/indexcuatro.html', {'error_message': error_message})

    else:
        # Si es una solicitud GET, simplemente renderiza el formulario
        return render(request, 'myapp/indexcuatro.html')

from .models import Respuestastres

# Vista para el tercer formulario
@csrf_exempt
def indexcinco_view(request):
    if request.method == 'POST':
        try:
            # Obtén los datos del formulario
            respuesta_19 = request.POST.get('respuesta19')
            respuesta_20 = request.POST.get('respuesta20')
            respuesta_21 = request.POST.get('respuesta21')
            respuesta_22 = request.POST.get('respuesta22')
            respuesta_23 = request.POST.get('respuesta23')
            respuesta_24 = request.POST.get('respuesta24')
            respuesta_25 = request.POST.get('respuesta25')
            respuesta_26 = request.POST.get('respuesta26')
            respuesta_27 = request.POST.get('respuesta27')

            # Crea una instancia del modelo RespuestasTres y guarda los datos
            nueva_respuesta_tres = Respuestastres(
                respuesta_19=respuesta_19,
                respuesta_20=respuesta_20,
                respuesta_21=respuesta_21,
                respuesta_22=respuesta_22,
                respuesta_23=respuesta_23,
                respuesta_24=respuesta_24,
                respuesta_25=respuesta_25,
                respuesta_26=respuesta_26,
                respuesta_27=respuesta_27
            )

            nueva_respuesta_tres.save()

            # Puedes redirigir a donde necesites después de completar el tercer formulario
            return redirect('indexsiete')

        except Exception as e:
            # Maneja cualquier otra excepción que pueda ocurrir
            error_message = f"Error: {str(e)}"
            return render(request, 'myapp/indexcinco.html', {'error_message': error_message})

    else:
        # Si es una solicitud GET, simplemente renderiza el formulario
        return render(request, 'myapp/indexcinco.html')

from .models import Respuestascuatro

@csrf_exempt
def indexsiete_view(request):
    if request.method == 'POST':
        try:
            # Obtén los datos del formulario
            respuesta_28 = request.POST.get('respuesta28')
            respuesta_29 = request.POST.get('respuesta29')
            respuesta_30 = request.POST.get('respuesta30')
            respuesta_31 = request.POST.get('respuesta31')
            respuesta_32 = request.POST.get('respuesta32')
            respuesta_33 = request.POST.get('respuesta33')
            respuesta_34 = request.POST.get('respuesta34')
            respuesta_35 = request.POST.get('respuesta35')

            # Crea una instancia del modelo Respuestascuatro y guarda los datos
            nueva_respuesta_cuatro = Respuestascuatro(
                respuesta_28=respuesta_28,
                respuesta_29=respuesta_29,
                respuesta_30=respuesta_30,
                respuesta_31=respuesta_31,
                respuesta_32=respuesta_32,
                respuesta_33=respuesta_33,
                respuesta_34=respuesta_34,
                respuesta_35=respuesta_35
            )

            nueva_respuesta_cuatro.save()

            # Puedes redirigir a donde necesites después de completar el séptimo formulario
            return redirect('iframe')

        except Exception as e:
            # Maneja cualquier otra excepción que pueda ocurrir
            error_message = f"Error: {str(e)}"
            return render(request, 'myapp/indexsiete.html', {'error_message': error_message})

    else:
        # Si es una solicitud GET, simplemente renderiza el formulario
        return render(request, 'myapp/indexsiete.html')
def iframe_view(request):
    return render(request, 'myapp/iframe.html', {})

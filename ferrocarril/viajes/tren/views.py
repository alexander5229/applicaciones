
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DireccionBuscada

# Create your views here.
from .models import Estacion, Viajero, TipoMaquina, PuntoPago,Destino
from .forms import (
    EstacionForm,
    TipoMaquinaForm,
    DestinoForm,
    PuntoPagoForm,
    ViajeroForm
)

def viajes_tren(request):
    return render(request,'tren/viajes_tren.html')


def listar_estaciones(request):
    query = request.GET.get('q', '')

    if query:
        # Filtra si coincide el nombre, el apellido o el documento
        estaciones = Estacion.objects.filter(
            Q(nombre__icontains=query) | 
            Q(ciudad__icontains=query) | 
            Q(telefono__icontains=query)
        )
    else:
        estaciones = Estacion.objects.all()

    return render(request,'tren/listar_estaciones.html',{'estaciones': estaciones, 'query': query})

def crear_estacion(request):

    if request.method == 'POST':

        form = EstacionForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('listar_estaciones')

    else:

        form = EstacionForm()

    return render(request,'tren/formulario_estacion.html',{'form': form})

# UPDATE: editar estaciones
def editar_estacion(request, pk):

    estacion = get_object_or_404(Estacion,pk=pk)

    if request.method == 'POST':

        form = EstacionForm(request.POST,request.FILES,instance=estacion)

        if form.is_valid():

            form.save()

            return redirect('listar_estaciones')

    else:

        form = EstacionForm(
            instance=estacion
        )

    return render(
        request,
        'tren/formulario_estacion.html',
        {
            'form': form,
            'estaciones': estacion
        }
    )


# DELETE: eliminar estaciones
def eliminar_estacion(request, pk):

    estacion = get_object_or_404(
        Estacion,
        pk=pk
    )

    if request.method == 'POST':

        estacion.delete()

        return redirect('listar_estaciones')

    return render(
        request,
        'tren/eliminar_estacion.html',
        {'estacion': estacion}
    )


        #VIAJEROS
def listar_viajero(request):
    query = request.GET.get('q', '')

    if query:
        # Filtra si coincide el nombre, el apellido o el documento
        viajeros = Viajero.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) | 
            Q(tipo_documento__icontains=query) |
            Q(documento__icontains=query) | 
            Q(correo__icontains=query) |  
            Q(telefono__icontains=query)
        )
    else:
        viajeros = Viajero.objects.all()

    return render(request,'tren/listar_viajero.html',{'viajeros': viajeros, 'query': query})

def crear_viajero(request):

    if request.method == 'POST':

        form = ViajeroForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('listar_viajero')

    else:

        form = ViajeroForm()

    return render(request,'tren/crear_viajero.html',{'form': form})

# UPDATE: editar entrenador
def editar_viajero(request, pk):

    viajero = get_object_or_404(Viajero, pk=pk)

    if request.method == 'POST':

        form = ViajeroForm(request.POST,instance=viajero)

        if form.is_valid():

            form.save()

            return redirect('listar_viajero')

    else:

        form = ViajeroForm(
            instance=viajero
        )

    return render(
        request,
        'tren/formulario_viajero.html',
        {
            'form': form,
            
        }
    )


# DELETE: eliminar entrenador
def eliminar_viajero(request, pk):

    viajero = get_object_or_404(
        Viajero,
        pk=pk
    )

    if request.method == 'POST':

        viajero.delete()

        return redirect('listar_viajero')

    return render(
        request,
        'tren/eliminar_viajero.html',
        {'viajeros': viajero}
    )


    #TIPO DE MAQUINA
def listar_maquina(request):
    query = request.GET.get('q', '')

    if query:
        # Filtra si coincide el nombre, el apellido o el documento
        maquinas = TipoMaquina.objects.filter(
            Q(nombre_tren__icontains=query) | 
            Q(numero_tren__icontains=query) | 
            Q(capacidades__icontains=query)
        )
    else:
        maquinas = TipoMaquina.objects.all()

    return render(request,'tren/listar_maquina.html',{'maquinas': maquinas, 'query': query})

def crear_maquina(request):

    if request.method == 'POST':

        form = TipoMaquinaForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('listar_maquina')

    else:

        form = TipoMaquinaForm()

    return render(request,'tren/formulario_maquina.html',{'form': form})

# UPDATE: editar entrenador
def editar_maquina(request, pk):

    maquinas = get_object_or_404(TipoMaquina,pk=pk)

    if request.method == 'POST':

        form = TipoMaquinaForm(request.POST,request.FILES,instance=maquinas)

        if form.is_valid():

            form.save()

            return redirect('listar_maquina')

    else:

        form = TipoMaquinaForm(
            instance=maquinas
        )

    return render(
        request,
        'tren/formulario_maquina.html',
        {
            'form': form,
            'maquinas': maquinas
        }
    )


# DELETE: eliminar entrenador
def eliminar_maquina(request, pk):

    maquina = get_object_or_404(
        TipoMaquina,
        pk=pk
    )

    if request.method == 'POST':

        maquina.delete()

        return redirect('listar_maquina')

    return render(
        request,
        'tren/eliminar_maquina.html',
        {'maquina': maquina}
    )

# READ: listar punto de pago
def listar_pago(request):

    query = request.GET.get('q', '')
    
    if query:
        # Filtra si coincide el lider, elemento o medallas
        pagos = PuntoPago.objects.filter(
            Q(estacion__icontains=query) | 
            Q(en_linea__icontains=query) |
            Q(en_vagon__icontains=query)
        )
    else:
        pagos = PuntoPago.objects.all()

    return render(
        request,
        'tren/listar_pago.html',
        {'pagos': pagos, 'query': query}
    )

# CREATE: registrar pago
def crear_pago(request):

    if request.method == 'POST':

        form = PuntoPagoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('listar_pago')
        else:
            print(form.errors)

    else:
        form = PuntoPagoForm()

    return render(
        request,
        'tren/formulario_pago.html',
        {'form': form}
    )

# UPDATE: editar pago
def editar_pago(request, pk):

    pago = get_object_or_404(PuntoPago, pk=pk)

    if request.method == 'POST':

        form = PuntoPagoForm(
            request.POST,
            
            instance=pago
        )

        if form.is_valid():
            form.save()
            return redirect('listar_pago')

    else:
        form = PuntoPagoForm(instance=pago)

    return render(
        request,
        'tren/formulario_pago.html',
        {
            'form': form,
            'pago': pago
        }
    )

# DELETE: eliminar pago
def eliminar_pago(request, pk):

    pago = get_object_or_404(PuntoPago, pk=pk)

    if request.method == 'POST':

        pago.delete()

        return redirect('listar_pago')

    return render(
        request,
        'tren/eliminar_pago.html',
        {'pago': pago}
    )

# READ: listar destino
def listar_destino(request):

    query = request.GET.get('q', '')
    
    if query:
        # Filtra si coincide el lider, elemento o medallas
        destinos = Destino.objects.filter(
            Q(nombre__icontains=query) | 
            Q(ciudad__icontains=query) |
            Q(telefono__icontains=query)
        )
    else:
        destinos = Destino.objects.all()

    return render(
        request,
        'tren/listar_destino.html',
        {'destinos': destinos, 'query': query}
    )

# CREATE: registrar destino
def crear_destino(request):

    if request.method == 'POST':

        form = DestinoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('listar_destino')

    else:
        form = DestinoForm()

    return render(
        request,
        'tren/formulario_destino.html',
        {'form': form}
    )

# UPDATE: editar destino
def editar_destino(request,pk):

    destino = get_object_or_404(Destino, pk=pk)

    if request.method == 'POST':

        form = DestinoForm(
            request.POST,
            request.FILES,
            instance=destino
        )

        if form.is_valid():
            form.save()
            return redirect('listar_destino')

    else:
        form = DestinoForm(instance=destino)

    return render(
        request,
        'tren/formulario_destino.html',
        {
            'form': form,
            'destino': destino
        }
    )

# DELETE: eliminar destino
def eliminar_destino(request, pk):

    destino = get_object_or_404(Destino, pk=pk)

    if request.method == 'POST':

        destino.delete()

        return redirect('listar_destino')

    return render(
        request,
        'tren/eliminar_destino.html',
        {'destino': destino}
    )


def mapa_view(request):
    return render(request, 'tren/mapa.html')


@csrf_exempt 
def guardar_direccion(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            direccion = data.get('address')
            lat = data.get('lat')
            lon = data.get('lon')

            if direccion:
                # Guardar en PostgreSQL
                DireccionBuscada.objects.create(
                    direccion=direccion,
                    latitud=lat,
                    longitud=lon
                )
                return JsonResponse({"status": "success", "message": "¡Guardado en PostgreSQL con éxito!"})
            else:
                return JsonResponse({"status": "error", "message": "Dirección vacía"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
            
    return JsonResponse({"status": "error", "message": "Método no permitido"}, status=405)
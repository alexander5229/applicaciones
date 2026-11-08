

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Aprendiz
from .forms import AprendizForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DireccionBuscada


# READ: Consultar y mostrar aprendices
def lista_aprendices(request):
    query = request.GET.get('q', '')

    if query:
        # Filtra si coincide el nombre, el apellido o el documento
        aprendices = Aprendiz.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) | 
            Q(documento__icontains=query)
        )
    else:

        aprendices = Aprendiz.objects.all()


    return render(
        request,
        "oficio/lista_aprendices.html",{
        'aprendices': aprendices, 'query': query}
    )


# CREATE: Registrar un nuevo aprendiz
def crear_aprendiz(request):

    if request.method == 'POST':

        formulario = AprendizForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_aprendices')

    else:
        formulario = AprendizForm()

    contexto = {
        'formulario': formulario
    }

    return render(
        request,
        'oficio/crear_aprendiz.html',
        contexto
    )

def editar_aprendiz(request, id):
    aprendiz = get_object_or_404(Aprendiz, id=id)

    if request.method == 'POST':
        formulario = AprendizForm(request.POST, instance=aprendiz)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_aprendices')
    else:
        formulario = AprendizForm(instance=aprendiz)

    return render(request, 'oficio/crear_aprendiz.html', {
        'formulario': formulario,
        'titulo': 'Editar aprendiz'
    })


# DELETE: Eliminar aprendiz
def eliminar_aprendiz(request, id):
    aprendiz = get_object_or_404(Aprendiz, id=id)

    if request.method == 'POST':
        aprendiz.delete()
        return redirect('lista_aprendices')

    return render(request, 'oficio/eliminar_aprendiz.html', {
        'aprendiz': aprendiz
    })


def mapa_view(request):
    return render(request, 'oficio/mapa.html') 


@csrf_exempt # forma temporal para simplificar peticiones AJAX en proyectos académicos
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
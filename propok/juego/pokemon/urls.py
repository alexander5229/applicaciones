
from django.urls import path
from . import views


urlpatterns = [


    path(
        '',
        views.inicio,
        name='inicio'
),

    # ENTRENADORES

    path(
        'entrenadores/',
        views.listar_entrenadores,
        name='listar_entrenadores'
    ),

    path(
        'entrenadores/crear/',
        views.crear_entrenador,
        name='crear_entrenador'
    ),

    path(
        'entrenadores/editar/<int:id>/',
        views.editar_entrenador,
        name='editar_entrenador'
    ),

    path(
        'entrenadores/eliminar/<int:id>/',
        views.eliminar_entrenador,
        name='eliminar_entrenador'
    ),


    path(
    'pokemones/',
    views.listar_pokemones,
    name='listar_pokemones'
),


path(
    'pokemones/crear/',
    views.crear_pokemon,
    name='crear_pokemon'
),

path(
    'pokemones/editar/<int:id>/',
    views.editar_pokemon,
    name='editar_pokemon'
),

path(
    'pokemones/eliminar/<int:id>/',
    views.eliminar_pokemon,
    name='eliminar_pokemon'
),

path(
    'gimnasios/',
    views.listar_gimnasios,
    name='listar_gimnasios'
),

path(
    'gimnasios/crear/',
    views.crear_gimnasio,
    name='crear_gimnasio'
),

path(
    'gimnasios/editar/<int:id>/',
    views.editar_gimnasio,
    name='editar_gimnasio'
),

path(
    'gimnasios/eliminar/<int:id>/',
    views.eliminar_gimnasio,
    name='eliminar_gimnasio'
),

path('mapa/', views.mapa_view, name='mapa'),

path('api/guardar-direccion/', views.guardar_direccion, name='guardar_direccion'),
]

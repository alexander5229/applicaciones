from django.urls import path
from . import views

urlpatterns = [
    path('',
            views.viajes_tren, name='viajes_tren'),
    path(
            'viajeros/',
            views.listar_viajero,
            name='listar_viajero'
        ),
    
        path(
            'viajeros/crear/',
            views.crear_viajero,
            name='crear_viajero'
        ),
    
        path(
            'viajeros/editar/<int:pk>/',
            views.editar_viajero,
            name='editar_viajero'
        ),
    
        path(
            'viajeros/eliminar/<int:pk>/',
            views.eliminar_viajero,
            name='eliminar_viajero'
        ),
    
        #estaciones
        path(
        'estaciones/',
        views.listar_estaciones,
        name='listar_estaciones'
    ),
    
    
    path(
        'estaciones/crear/',
        views.crear_estacion,
        name='crear_estacion'
    ),
    
    path(
        'estaciones/editar/<int:pk>/',
        views.editar_estacion,
        name='editar_estacion'
    ),
    
    path(
        'estaciones/eliminar/<int:pk>/',
        views.eliminar_estacion,
        name='eliminar_estacion'
    ),


    # maquinas
    path(
        'maquina/',
        views.listar_maquina,
        name='listar_maquina'
    ),
    
    path(
        'maquina/crear/',
        views.crear_maquina,
        name='crear_maquina'
    ),
    
    path(
        'maquina/editar/<int:pk>/',
        views.editar_maquina,
        name='editar_maquina'
    ),
    
    path(
        'maquina/eliminar/<int:pk>/',
        views.eliminar_maquina,
        name='eliminar_maquina'
    ),

    # Pagos
    path(
        'pago/',
        views.listar_pago,
        name='listar_pago'
        ),
    
        path(
        'pago/crear/',
        views.crear_pago,
        name='crear_pago'
        ),
    
        path(
        'pago/editar/<int:pk>/',
        views.editar_pago,
        name='editar_pago'
        ),
    
        path(
        'pago/eliminar/<int:pk>/',
        views.eliminar_pago,
        name='eliminar_pago'
        ),
    
        # Destino
        path(
        'destino/',
        views.listar_destino,
        name='listar_destino'),
    
    
    path(
        'destino/crear/',
        views.crear_destino,
        name='crear_destino'
    ),
    
    path(
        'destino/editar/<int:pk>/',
        views.editar_destino,
        name='editar_destino'
    ),
    
    path(
        'destino/eliminar/<int:pk>/',
        views.eliminar_destino,
        name='eliminar_destino'
    ),


    path('mapa/', views.mapa_view, name='mapa'),
    
    path('api/guardar-direccion/', views.guardar_direccion, name='guardar_direccion'),
    ]
    



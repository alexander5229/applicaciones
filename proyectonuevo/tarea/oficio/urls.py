
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.lista_aprendices,
        name="lista_aprendices"
    ),

    path(
        'crear/',
        views.crear_aprendiz,
        name="crear_aprendiz"
    ),

    path('editar/<int:id>/', views.editar_aprendiz, name='editar_aprendiz'),

    path('eliminar/<int:id>/', views.eliminar_aprendiz, name='eliminar_aprendiz'),
    path('mapa/', views.mapa_view, name='mapa'),
    path('api/guardar-direccion/', views.guardar_direccion, name='guardar_direccion'),

]

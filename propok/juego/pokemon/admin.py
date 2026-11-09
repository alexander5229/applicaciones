from django.contrib import admin

# Register your models here.
from .models import Entrenadores, Pokemones, Gimnasio


@admin.register(Entrenadores)
class EntrenadoresAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nombre',
        'apellido',
        'documento'
    )

    search_fields = (
        'nombre',
        'apellido',
        'documento'
    )


@admin.register(Pokemones)
class PokemonesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nombre',
        'peso',
        'naturaleza',
        'fecha_captura',
        'entrenador_pokemon'
    )

    search_fields = ('nombre', 'naturaleza')

    list_filter = (
        'naturaleza',
        'fecha_captura'
    )


@admin.register(Gimnasio)
class GimnasioAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'lider_gim',
        'elemento_gim',
        'medallas'
    )

    search_fields = (
        'lider_gim',
        'elemento_gim'
    )

    list_filter = ('elemento_gim',)

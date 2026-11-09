
from django import forms
from .models import Entrenadores, Pokemones, Gimnasio


class EntrenadoresForm(forms.ModelForm):

    class Meta:
        model = Entrenadores

        fields = [
            'nombre',
            'apellido',
            'documento',
            'imagen'
        ]


class PokemonesForm(forms.ModelForm):

    class Meta:
        model = Pokemones

        fields = [
            'nombre',
            'peso',
            'habilidades',
            'naturaleza',
            'descripcion',
            'fecha_captura',
            'entrenador_pokemon',
            'imagen'
        ]

        widgets = {
            'fecha_captura': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'descripcion': forms.Textarea(
                attrs={'rows': 4}
            )
        }


class GimnasioForm(forms.ModelForm):

    class Meta:
        model = Gimnasio

        fields = [
            'lider_gim',
            'elemento_gim',
            'medallas',
            'imagen_gim',
            'imagen_estadio'
        ]

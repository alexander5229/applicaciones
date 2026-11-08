
from django import forms
from .models import Aprendiz


class AprendizForm(forms.ModelForm):

    class Meta:
        model = Aprendiz

        fields = [
            'Programa',
            'nombre',
            'apellido',
            'documento',
            'tipo_documento',
            'correo',
            'telefono',
            'ficha'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),

            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),

            'documento': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el documento'
            }),

            'tipo_documento': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: C.C.'
            }),

            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el correo electrónico'
            }),

            'telefono': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el teléfono'
            }),

            'ficha': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el número de ficha'
            }),

            'Programa': forms.Select(attrs={
                'class': 'form-control'
            })
        }

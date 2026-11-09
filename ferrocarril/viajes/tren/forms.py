
from django import forms
from .models import Estacion,Viajero,TipoMaquina,PuntoPago,Destino


class EstacionForm(forms.ModelForm):

    class Meta:
        model = Estacion

        fields = [
            'nombre',
            'ciudad',
            'telefono'
            
        ]


class ViajeroForm(forms.ModelForm):

    class Meta:
        model = Viajero

        fields = [
            'nombre',
            'apellido',
            'tipo_documento',
            'documento',
            'correo',
            'telefono'
            
        ]

class TipoMaquinaForm(forms.ModelForm):

    class Meta:
        model = TipoMaquina

        fields = [
            'nombre_tren',
            'numero_tren',
            'capacidades'
           
        ]
class PuntoPagoForm(forms.ModelForm):

    class Meta:
        model = PuntoPago

        fields = [
            'estacion',
            'en_linea',
            'en_vagon'
           
        ]

class DestinoForm(forms.ModelForm):

    class Meta:
        model = Destino

        fields = [
            'nombre',
            'ciudad',
            'telefono'
           
        ]

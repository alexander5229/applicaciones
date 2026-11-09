from django.contrib import admin

# Register your models here.
from .models import Viajero, TipoMaquina, Estacion, Destino, PuntoPago 


admin.site.register(Viajero)
admin.site.register(TipoMaquina)
admin.site.register(Estacion)
admin.site.register(Destino)
admin.site.register(PuntoPago)
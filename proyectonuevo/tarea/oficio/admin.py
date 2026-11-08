from django.contrib import admin
from .models import Aprendiz, Programa, Instructores, Competencias
# Register your models here.

admin.site.register(Aprendiz)
admin.site.register(Programa)
admin.site.register(Instructores)
admin.site.register(Competencias)
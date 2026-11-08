from django.db import models

# Create your models here.

class Aprendiz(models.Model):
    Programa=models.ForeignKey('Programa',
    on_delete=models.CASCADE,
    related_name=("aprendices"),
    null=True,
    blank=True
    )
    
    nombre = models.CharField(max_length=23)
    apellido = models.CharField(max_length=23)
    documento = models.IntegerField(unique=True)
    tipo_documento= models.CharField(max_length=5)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField(unique=True)
    ficha = models.IntegerField()
    

    def __str__(self):      
        return f" Nom: {self.nombre} - Ape:{self.apellido} - Doc: {self.documento} - T_doc: {self.tipo_documento} - Correo: {self.correo} - Tel: {self.telefono} - Ficha: {self.ficha}"

class Programa(models.Model):
    Instructores=models.ForeignKey('Instructores',
    on_delete=models.CASCADE,
    related_name=("instructores"),
    null=True,
    blank=True
    )

    nombre = models.CharField(max_length=23)
    ficha = models.IntegerField(unique=True)
    jornada = models.CharField(max_length=15)
    lugar = models.CharField(max_length=25)
    duracion = models.CharField(max_length=23)
    modalidad = models.CharField(max_length=20)
    nivel_profesional = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):      
        return f" Nombre: {self.nombre} - Ficha: {self.ficha} - Jor: {self.jornada} - Lug: {self.ficha} - Dura: {self.duracion} - Mod: {self.modalidad} - Niv: {self.nivel_profesional} - Desc: {self.descripcion}"

class Instructores(models.Model):
    nombre = models.CharField(max_length=23)
    apellido = models.CharField(max_length=23)
    documento = models.IntegerField(unique=True)
    telefono = models.IntegerField(unique=True)
    especialidad = models.CharField(max_length=23)
    ficha_asignada = models.IntegerField(unique=True)
    correo = models.EmailField(unique=True)
    

    def __str__(self):      
        return f" Nombre: {self.nombre} - - Ape:{self.apellido} - Tel: {self.telefono} - Esp: {self.especialidad} - Ficha:{self.ficha_asignada} - Correo: {self.correo}"

class Competencias(models.Model):
    nombre = models.CharField(max_length=23)
    ficha = models.IntegerField(unique=True)
    instructores =  models.CharField(max_length=50) 

    def __str__(self):      
        return f"Nombre: {self.nombre} - Ficha: {self.ficha} - Inst: {self.instructores}"       


class BusquedaUbicacion(models.Model):
    direccion = models.CharField(max_length=255)
    fecha_busqueda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion


class DireccionBuscada(models.Model):
    direccion = models.CharField(max_length=255)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    fecha_busqueda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.direccion} ({self.fecha_busqueda.strftime('%Y-%m-%d %H:%M')})"    




from django.db import models

# Create your models here.

class Entrenadores(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=20,unique=True)
    imagen = models.ImageField(upload_to='entrenadores/',null=True,blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Pokemones(models.Model):

    nombre = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=6,decimal_places=2)
    habilidades = models.CharField(max_length=80)
    naturaleza = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_captura = models.DateField()
    entrenador_pokemon = models.ForeignKey(
        Entrenadores,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pokemones'
    )

    imagen = models.ImageField(upload_to='pokemones/',null=True,blank=True)

    def __str__(self):
        return self.nombre

class Gimnasio(models.Model):

    lider_gim = models.CharField(max_length=50)
    elemento_gim = models.CharField(max_length=50)
    medallas = models.CharField(max_length=100)

    imagen_gim = models.ImageField(upload_to='gimnasios/',null=True,blank=True)
    imagen_estadio = models.ImageField(upload_to='estadios/',null=True,blank=True)

    def __str__(self):
        return self.lider_gim


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
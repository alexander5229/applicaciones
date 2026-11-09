from django.db import models

class Estacion(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    telefono = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.ciudad})"


class TipoMaquina(models.Model):
    # Relación muchos a muchos con Estaciones
    estaciones = models.ManyToManyField(
        Estacion,
        related_name="maquinas",
        blank=True
    )
    nombre_tren = models.CharField(max_length=50)
    numero_tren = models.IntegerField(unique=True) # Corregido: unique debe ser booleano
    capacidades = models.CharField(max_length=50)

    def __str__(self):
        return f"Tren: {self.nombre_tren} (#{self.numero_tren})"


class Destino(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    telefono = models.IntegerField(unique=True)

    def __str__(self):
        return f"Destino: {self.nombre} - {self.ciudad}"


class PuntoPago(models.Model):
    estacion = models.CharField(max_length=50)
    en_linea = models.CharField(max_length=50)
    en_vagon = models.CharField(max_length=50)

    def __str__(self):
        return f"Punto de Pago - Estación: {self.estacion}"


class Viajero(models.Model):
    
    tipo_maquina = models.ForeignKey(
        TipoMaquina,
        on_delete=models.CASCADE,
        related_name="viajeros",
        null=True,
        blank=True
    )
    destino = models.ForeignKey(
        Destino,
        on_delete=models.CASCADE,
        related_name="viajeros",
        null=True,
        blank=True
    )
    punto_pago = models.ManyToManyField(
        PuntoPago,
        related_name="viajeros",
        blank=True # En Django moderno, null=True no se usa en ManyToManyField
    )
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_documento = models.CharField(max_length=5)
    documento = models.IntegerField(unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - T.Doc: {self.tipo_documento} - Doc: {self.documento}"


class BusquedaUbicacion(models.Model):
    direccion = models.CharField(max_length=255)
    fecha_busqueda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.direccion    


from django.db import models

class DireccionBuscada(models.Model):
    direccion = models.CharField(max_length=255)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    fecha_busqueda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.direccion} ({self.fecha_busqueda.strftime('%Y-%m-%d %H:%M')})"    
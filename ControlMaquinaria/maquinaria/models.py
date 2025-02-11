from django.db import models

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=255, default="Desconocido")  # Agregar un valor por defecto



class Obra(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True, blank=True)  # Campo agregado
    responsable = models.ForeignKey("Responsable", on_delete=models.SET_NULL, null=True, blank=True)  # Campo agregado

    def __str__(self):
        return self.nombre


class Responsable(models.Model):
    nombre = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255, default="Sin especificar")  # Campo agregado
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='equipos/', null=True, blank=True)
    documento = models.FileField(upload_to='documentos/', null=True, blank=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True, blank=True)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

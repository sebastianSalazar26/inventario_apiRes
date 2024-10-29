from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=80)
    cantidad_min = models.IntegerField()
    catidad_max = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
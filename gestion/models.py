from django.db import models

class Cliente(models.Model):
    nombre = models.CharField()
    direccion = models.CharField()
    email = models.EmailField()
    telefono = models.CharField()
    
class Articulo(models.Model):
    nombre = models.CharField()
    seccion = models.CharField()
    precio = models.IntegerField()
    
class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    

    
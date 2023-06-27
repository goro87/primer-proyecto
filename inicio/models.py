from django.db import models

# Create your models here.

class Perro(models.Model):
    nombre = models.CharField(max_length=20) 
    edad = models.IntegerField()
    
    
    
#Se crean los 3 modelos
class Persona(models.Model):
    nombre_Persona = models.CharField(max_length=20) 
    edad_Persona = models.IntegerField()    
    
class Producto(models.Model):
    nombre_Producto = models.CharField(max_length=10) 
    Precio_Producto = models.IntegerField()  
    
class Proveedor(models.Model):
    Nombre_Empresa = models.CharField(max_length=50) 
    CUIT = models.IntegerField()  
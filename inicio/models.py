from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Perro(models.Model):
    nombre = models.CharField(max_length=20) 
    edad = models.IntegerField()
    
    
    
#Se crean los 3 modelos
class Persona(models.Model):
    nombre_Persona = models.CharField(max_length=20) 
    edad_Persona = models.IntegerField() 
    descripcion = RichTextField(null=True)
    Lugar_De_Nacimiento = models.CharField(max_length=20,null=True) 
    Fecha_Nacimiento = models.DateField(null=True)
    avatar = models.ImageField(upload_to='avatares',null=True,blank=True)
    

    
    def  __str__(self):
        return f" Persona:{self.nombre_Persona} - Edad: {self.edad_Persona}"
       
    
class Producto(models.Model):
    nombre_Producto = models.CharField(max_length=10) 
    Precio_Producto = models.IntegerField()  
    
class Proveedor(models.Model):
    Nombre_Empresa = models.CharField(max_length=50) 
    CUIT = models.IntegerField()  
    avatarProve = models.ImageField(upload_to='avatares',null=True,blank=True)
    
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm



class PersonaFormularioBase(forms.Form):
    nombre= forms.CharField(max_length=20, required=False)
    edad= forms.IntegerField(required=False)
    avatar = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['nombre','edad','avatar']
    
   

class CrearPerroFormulario(PersonaFormularioBase):
    ...
    
class CrearPersonaFormulario(PersonaFormularioBase):
    ...

    
class ModificarPersonaFormulario(forms.Form):
    nombre= forms.CharField(max_length=20, required=False)
    edad= forms.IntegerField() 
    avatar = forms.ImageField(required=False)

    
    
class BuscarPersona(forms.Form):
    nombre= forms.CharField(max_length=20, required=False)
    
class CrearProductoFormulario(forms.Form):
    nombre_Producto_f= forms.CharField(max_length=10, required=False)
    Precio_Producto_f= forms.IntegerField()

class CrearProveedorFormulario(forms.Form):
     Nombre_Empresa= forms.CharField(max_length=50, required=False)
     CUIT_Empresa= forms.IntegerField()        
    
from django import forms

class CrearPerroFormulario(forms.Form):
    nombre= forms.CharField(max_length=20, required=False)
    edad= forms.IntegerField()
    
class CrearPersonaFormulario(forms.Form):
    nombre= forms.CharField(max_length=20, required=False)
    edad= forms.IntegerField()
    
class BuscarPersona(forms.Form):
    nombre= forms.CharField(max_length=20, required=False)

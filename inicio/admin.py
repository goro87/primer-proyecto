from django.contrib import admin
from inicio.models import Perro
from inicio.models import Persona
from inicio.models import Producto
from inicio.models import Proveedor
# Register your models here.
admin.site.register(Perro)
admin.site.register(Persona)
admin.site.register(Producto)
admin.site.register(Proveedor)
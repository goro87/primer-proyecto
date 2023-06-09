from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context

# def inicio(request):
#     return HttpResponse('Hola soy la vista loca')

def inicio(request):
    archivo = open(r'C:\Users\guang\Documents\Proyectos\MI_PRIMER_DJANGO\templates\inicio.html','r')
    
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    renderizar_template = template.render(contexto)
    
    return HttpResponse(renderizar_template)


def segunda_vista(request):
    return HttpResponse('<h1>Soy la segunda vista<h1>')

def fecha_actual(request):

    fecha=datetime.now()
    return HttpResponse(f'Fecha actual : {fecha}')

def saludar(request):
    return HttpResponse('Bienvenido')

def Bienvenida(request,nombre,apellido):
    return HttpResponse(f'Bienvenida {nombre.title()} {apellido.title()}!!!!')
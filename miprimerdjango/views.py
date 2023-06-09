from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context, loader

# def inicio(request):
#     return HttpResponse('Hola soy la vista loca')

#v2
# def inicio(request):
#     archivo = open(r'C:\Users\guang\Documents\Proyectos\MI_PRIMER_DJANGO\templates\inicio.html','r')
#     template = Template(archivo.read())
#     archivo.close()
#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Este es el mensaje de inicio...',
#         'segundos' : segundos,
#         'segundo_par' : segundos%2==0,
#         'segundo_redondo' : segundos%10==0,
#         'listado_de_numeros':list(range(25))}
#     contexto = Context(diccionario)
#     renderizar_template = template.render(contexto)
#     return HttpResponse(renderizar_template)

#v3
def inicio(request):
    #archivo = open(r'C:\Users\guang\Documents\Proyectos\MI_PRIMER_DJANGO\templates\inicio.html','r')
    #template = Template(archivo.read())
    #archivo.close()
    template  = loader.get_template('inicio.html')
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos' : segundos,
        'segundo_par' : segundos%2==0,
        'segundo_redondo' : segundos%10==0,
        'listado_de_numeros':list(range(25))}
    # contexto = Context(diccionario)
    # renderizar_template = template.render(contexto)
    renderizar_template = template.render(diccionario)
    
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
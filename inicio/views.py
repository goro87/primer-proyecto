from django.http import HttpResponse
from datetime import datetime
from django.template import Template,Context, loader
from inicio.models import Perro
from inicio.models import Persona
from inicio.models import Producto
from inicio.models import Proveedor
from django.shortcuts import render,redirect
from inicio.form import BuscarPersona,CrearPersonaFormulario,CrearProductoFormulario,CrearProveedorFormulario
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

# #v3
# def inicio(request):
#     #archivo = open(r'C:\Users\guang\Documents\Proyectos\MI_PRIMER_DJANGO\templates\inicio.html','r')
#     #template = Template(archivo.read())
#     #archivo.close()
#     template  = loader.get_template('inicio.html')
#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Este es el mensaje de inicio...',
#         'segundos' : segundos,
#         'segundo_par' : segundos%2==0,
#         'segundo_redondo' : segundos%10==0,
#         'listado_de_numeros':list(range(25))}
#     # contexto = Context(diccionario)
#     # renderizar_template = template.render(contexto)
#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)
#v4
def prueba(request):
    # template  = loader.get_template('inicio.html')
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos' : segundos,
        'segundo_par' : segundos%2==0,
        'segundo_redondo' : segundos%10==0,
        'listado_de_numeros':list(range(25))
    }
    # renderizar_template = template.render(diccionario)
    # return HttpResponse(renderizar_template)
    return render(request,'inicio/prueba.html',diccionario)

def inicio(request):
    return render(request,'inicio/inicio.html')

def segunda_vista(request):
    return HttpResponse('<h1>Soy la segunda vista<h1>')

def fecha_actual(request):
    fecha=datetime.now()
    return HttpResponse(f'Fecha actual : {fecha}')

def saludar(request):
    return HttpResponse('Bienvenido')

def Bienvenida(request,nombre,apellido):
    return HttpResponse(f'Bienvenida {nombre.title()} {apellido.title()}!!!!')
#v1
# def crear_perro(request , nombre , edad):
#     template  = loader.get_template('crear_perro.html')
#     perro = Perro(nombre=nombre,edad=edad)
#     perro.save()
#     diccionario = {
#             'perro':perro,
#     }
#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)

# v2
def crear_perro(request , nombre , edad):
    perro = Perro(nombre=nombre,edad=edad)
    perro.save()
    diccionario = {
            'perro':perro,
    }
    return render(request,'inicio/crear_perro.html',diccionario)

def Alta(request):
    
    #diccionario={}
    
    if request.method == "POST":
        formulario=CrearPersonaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            persona = Persona(nombre_Persona=info['nombre'],edad_Persona=info['edad']) 
            persona.save()
          #  diccionario['persona']=persona
            return redirect('inicio:Busqueda')
        else :
           # diccionario['formulario']=formulario
            return render(request,'inicio/Busqueda.html')
    
    formulario=CrearPersonaFormulario()
   # diccionario['formulario']=formulario
    return render(request,'inicio/Alta.html', {'formulario':formulario})

def Busqueda(request):
    
    formulario = BuscarPersona(request.GET)
    if formulario.is_valid():
        nombre_a_buscar=formulario.cleaned_data['nombre']
        listado_de_personas = Persona.objects.filter(nombre_Persona__icontains=nombre_a_buscar)
        
    formulario = BuscarPersona()
    return render(request,'inicio/Busqueda.html',{'formulario':formulario , 'personas': listado_de_personas })
    #return render(request,'inicio/Busqueda.html',{'formulario':formulario})

#v1
# def Alta_Producto(request):
    
#     diccionario={}
    
#     if request.method == "POST":
#      producto = Producto(nombre_Producto=request.POST['nombre'],Precio_Producto=request.POST['precio']) 
#      producto.save()
#      diccionario['producto']:producto
     
#     return render(request,'inicio/Alta_Producto.html')


def Alta_Producto(request):
    
    #diccionario={}
    
    if request.method == "POST":
        formulario=CrearProductoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            producto = Producto(nombre_Producto=info['nombre_Producto_f'],Precio_Producto=info['Precio_Producto_f']) 
            producto.save()
          #  diccionario['persona']=persona
            return redirect('inicio:Alta_Producto')
        else :
          #  diccionario['formulario']=formulario
            return render(request,'inicio/inicio.html')
    
    formulario=CrearProductoFormulario()
   # diccionario['formulario']=formulario
    return render(request,'inicio/Alta_Producto.html', {'formulario':formulario})



# def Alta_Empresa(request):
    
#     diccionario={}
    
#     if request.method == "POST":
#      proveedor = Proveedor(Nombre_Empresa=request.POST['nombre'],CUIT=request.POST['CUIT']) 
#      proveedor.save()
#      diccionario['proveedor']:proveedor
     
#     return render(request,'inicio/Alta_Empresa.html')


def Alta_Empresa(request):
    
    #diccionario={}
    
    if request.method == "POST":
        formulario=CrearProveedorFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            proveedor = Proveedor(Nombre_Empresa=info['Nombre_Empresa'],CUIT=info['CUIT_Empresa']) 
            proveedor.save()
          #  diccionario['persona']=persona
            return redirect('inicio:Alta_Empresa')
        else :
          #  diccionario['formulario']=formulario
            return render(request,'inicio/inicio.html')
    
    formulario=CrearProveedorFormulario()
   # diccionario['formulario']=formulario
    return render(request,'inicio/Alta_Empresa.html', {'formulario':formulario})


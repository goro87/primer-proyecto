from django.urls import path
from inicio  import views

app_name='inicio'

urlpatterns = [
    path('', views.inicio , name='inicio'),
    path('Alta_SIN_CBV/', views.Alta_SIN_CBV , name='Alta_SIN_CBV'),
    path('Alta_Producto/', views.Alta_Producto , name='Alta_Producto'),
    path('Alta_Empresa/', views.Alta_Empresa , name='Alta_Empresa'),
    path('prueba/', views.prueba, name='prueba'),
    path('segunda-vista',views.segunda_vista, name='segunda_vista'),
    path('fecha-actual',views.fecha_actual, name='fecha_actual'),
    path('saludar',views.saludar, name='saludar'),
    path('Bienvenida/<str:nombre>/<str:apellido>/',views.Bienvenida, name='bienvenida'),
    # 
    
    # path('Busqueda/', views.Busqueda , name='Busqueda'),
    # path('crear-perro/<str:nombre>/<int:edad>/',views.crear_perro, name='crear_perro'),
    # path('eliminar/<int:persona_id>/',views.eliminar_persona, name='eliminar_persona'),
    # path('modificar/<int:persona_id>/',views.modificar_persona, name='modificar_persona'),
    
    
    #CBV
    path('Busqueda/', views.ListarPersonas.as_view() , name='Busqueda'),
    path('Alta/', views.AltaPersona.as_view() , name='Alta'),
    path('eliminar/<int:pk>/', views.EliminarPersona.as_view() , name='EliminarPersona'),
    path('modificar/<int:pk>/', views.ModificarPersona.as_view() , name='ModificarPersona'),
    path('DatosPersona/<int:pk>/', views.DatosPersona.as_view() , name='DatosPersona'),
    path('Acerca/', views.Acerca.as_view() , name='Acerca'),
]

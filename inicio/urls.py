from django.urls import path
from inicio  import views

app_name='inicio'

urlpatterns = [
    path('', views.inicio , name='inicio'),
    path('Alta/', views.Alta , name='Alta'),
    path('Alta_Producto/', views.Alta_Producto , name='Alta_Producto'),
    path('Alta_Empresa/', views.Alta_Empresa , name='Alta_Empresa'),
    path('Busqueda/', views.Busqueda , name='Busqueda'),
    path('prueba/', views.prueba, name='prueba'),
    path('segunda-vista',views.segunda_vista, name='segunda_vista'),
    path('fecha-actual',views.fecha_actual, name='fecha_actual'),
    path('saludar',views.saludar, name='saludar'),
    path('Bienvenida/<str:nombre>/<str:apellido>/',views.Bienvenida, name='bienvenida'),
    path('crear-perro/<str:nombre>/<int:edad>/',views.crear_perro, name='crear_perro'),

]

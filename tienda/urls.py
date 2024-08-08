from django.urls import path
from . import views
app_name='Tienda'

urlpatterns = [
    #path('', views.base, name="base"),
    path('navegar/', views.navegar, name="navegar"),
    path('cerrarSesion/', views.cerrar_sesion,name="cerrarSesion"),
    path('historial/', views.historialCompra, name="historialCompra")
]
from django.urls import path, include
from . import views
app_name='carro'

urlpatterns = [
    path('agregar/<int:producto_id>', views.agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id>', views.eliminar_producto, name="eliminar"),
    path('sumar/<int:producto_id>', views.sumar_producto, name="sumar"),
    path('restar/<int:producto_id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carro, name="limpiar"),
    path('carro/', views.template_carro, name="tCarro"),
    path('pago/', views.pago, name='pago')
]

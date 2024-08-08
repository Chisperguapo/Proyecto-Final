from django.urls import path
from . import views
app_name='AppAdmin'

urlpatterns = [
    path('panelAdmin/', views.viewPanelAdmin, name="panelAdmin"),
    path('pqrsAdmin/', views.viewContacts, name="pqrsAdmin"),
    path('reportes/', views.reportes, name="reportes"),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('descargar-compras/', views.pdfCompras, name='pdfCompras'),
]

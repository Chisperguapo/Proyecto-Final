
from django.urls import path
from . import views
from .views import reporteTipoContactoFechas, reporteBajoStock

app_name='Reportes'

urlpatterns = [
    path('reportePorContacto/', reporteTipoContactoFechas, name="reportePorContacto"),
    path('bajoStock/', reporteBajoStock, name="bajoStock"),
]
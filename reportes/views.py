from django.shortcuts import render
from django.shortcuts import render
# Librerías necesarias para generar reportes del contacto por fechas:
from django.db.models import Count
from contacto.models import Contacto
from django.utils.dateparse import parse_date
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64

from productos.models import Producto

# Librerias para verificar si la sesion es super user
from django.contrib.auth.decorators import user_passes_test
from appAdmin.views import is_superuser

# Mapeo de los valores de tipo de contacto a sus nombres
opciones_pqrs = {
    0: 'Peticiones',
    1: 'Quejas',
    2: 'Reclamos',
    3: 'Sugerencias'
}

@user_passes_test(is_superuser)
def reporteTipoContactoFechas(request):
    # Obtener rango de fechas desde los parámetros GET:
    fechaInicio = request.GET.get('fecha_inicio')
    fechaFin = request.GET.get('fecha_fin')
    
    # Inicializar variables de fecha
    contactos = []
    reporte = []
    uri = None

    if fechaInicio and fechaFin:
        # Convertir fechas a objeto de fecha
        fechaInicio = parse_date(fechaInicio)
        fechaFin = parse_date(fechaFin)

        # Filtrar contactos por rango de fechas y contar por tipo de contacto
        contactos = Contacto.objects.filter(fecha_envio__range=[fechaInicio, fechaFin])
        reporte = contactos.values('tipo_contacto').annotate(total=Count('tipo_contacto'))

        # Convertir QuerySet en un DataFrame de pandas para facilitar el manejo
        df = pd.DataFrame(list(reporte))

        if not df.empty:
            # Mapear los números a los nombres de tipo de contacto
            df['tipo_contacto'] = df['tipo_contacto'].map(opciones_pqrs)

            # Graficar el reporte usando Matplotlib
            plt.figure(figsize=(10, 6))
            plt.bar(df['tipo_contacto'], df['total'])
            plt.xlabel('Tipo de contacto')
            plt.ylabel('Número de contactos')
            plt.title('Reporte de contactos por tipo')

            # Guardar la gráfica en un objeto BytesIO
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = urllib.parse.quote(string)

    # Renderizar la plantilla con el reporte y gráfica:
    context = {
        'reporte': df.to_dict(orient='records') if reporte else [],
        'grafico': uri,
    }
    return render(request, 'reportes.html', context)

def reporteBajoStock(request):
    # Obtener el valor de bajoStock desde el formulario, o usar 10 como valor por defecto
    bajoStock = request.GET.get('bajoStock', 10)
    try:
        bajoStock = int(bajoStock)
    except ValueError:
        bajoStock = 10

    
    # Filtrar productos con stock bajo
    productosStockBajo = Producto.objects.filter(stock__lte = bajoStock)
    
    # Crear diccionario para agregarlo al contexto
    context = {
        'productosStockBajo':productosStockBajo
    }
    
    return render(request, 'productos/bajoStock.html', context)
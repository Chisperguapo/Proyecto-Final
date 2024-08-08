from django.contrib import admin
from django.urls import path, include
from paypal.standard.ipn import urls as paypal_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),
    path('', include('productos.urls')),
    path('', include('carro.urls')),
    path('', include('usuario.urls')),
    path('', include('contacto.urls')),
    path('', include('reportes.urls')),
    path('', include('appAdmin.urls')),
    path('', include('paypal.standard.ipn.urls')),
    path('', include('pasarelaPago.urls')),
    path('paypal/', include(paypal_urls))
]

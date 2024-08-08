from django.contrib import admin
from .models import Contacto

class ContactoAdmin(admin.ModelAdmin): # Se inicia la clase'ContactoAdmin' con los parametros de admin'admin.ModelAdmin':
    list_display = ('nombre', 'email', 'mensaje', 'tipo_contacto', 'notificacion') # Se crea una lista con los campos que se va a mostrar'list_display', estó con el fin de mostrar los correos enviados por los clientes.
    search_fields = ('nombre', 'email', 'mensaje') # Se le agrega un buscador de campos'search_fields' para una busqueda más comoda.
    list_filter = ('nombre', 'email') # Se le crea un filtrado'list_filter' con 2 campos.

admin.site.register(Contacto, ContactoAdmin) # Se registra'register' en el sitio'site' de administación'admin' las clases'Contacto'y'ContactoAdmin'.
from django.contrib import admin
from .models import User

# class RegistroUsuarioAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'apellido', 'direccion', 'fechaNaci', 'numTel', 'correo', 'contrasenha')
#     search_fields = ('nombre', 'apellido', 'correo')
#     list_filter = ('nombre', 'apellido', 'correo', 'numTel')

admin.site.register(User)

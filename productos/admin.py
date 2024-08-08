from django.contrib import admin
from . import models

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class MarcaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Marca, MarcaAdmin)
admin.site.register(models.Producto)
admin.site.register(models.Promocion)
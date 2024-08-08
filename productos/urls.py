# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from .views import ProductosCrud

app_name = 'Productos'

urlpatterns = [
    path('productos/', views.productos, name="tProductos"),

    path('prodsAdmin/', ProductosCrud.viewAdminProds, name="prodsAdmin"),
    path('add/', ProductosCrud.agregarProd, name="add"),
    path('updated/<int:id>/', ProductosCrud.updatedProd, name='updatedProd'),
    path('<int:id>/', ProductosCrud.delateProd, name='delateProd'),

    path('categorias/', ProductosCrud.viewCateg, name="categorias"),
    path('addCateg/', ProductosCrud.addCateg, name="addCateg"),
    path('updatedCateg/<int:id>/', ProductosCrud.updatedCateg, name="updatedCateg"),
    path('categoria/<int:id>/', ProductosCrud.delateCateg, name="delateCateg"),

    path('marcas/', ProductosCrud.viewMarc, name="marcas"),
    path('addMarca/', ProductosCrud.addMarca, name="addMarca"),
    path('updatedMarca/<int:id>/', ProductosCrud.updatedMarca, name="updatedMarca"),
    path('marca/<int:id>/', ProductosCrud.delateMarca, name="delateMarca"),

    path('slide/', views.promocion, name="promocion")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render,redirect, get_object_or_404
from productos.models import Producto, Categoria, Marca, Promocion
#
from django.db.models import Q
# Librerias oara el CRUD  del admin
from .forms import ProductoForm, CategoriaForm, MarcaForm

import os
#
from django.contrib import messages

# Librerias para verificar si el de la sesion es super user.
from django.contrib.auth.decorators import user_passes_test
from appAdmin.views import is_superuser

def productos(request):
    categorias = Categoria.objects.all()
    query = request.GET.get('query', '')  # Captura el valor del parámetro de búsqueda
    if query:
        products = Producto.objects.filter(
            Q(nombre__icontains=query) |  # Busca productos cuyo nombre contiene la consulta
            Q(marca__marca__icontains=query) |  # Busca productos cuya marca contiene la consulta
            Q(categoria__categoria__icontains=query)  # Busca productos cuya categoría contiene la consulta
        ).exclude(precio_anterior='')  # Excluye productos sin precio anterior
    else:
        products = Producto.objects.filter(precio_anterior__isnull=False).exclude(precio_anterior='')  # Filtra productos con precio anterior
    return render(request, 'productos.html', {'productos': products, 'query': query, 'categorias': categorias})
class ProductosCrud():
    # PRODUCTOS
    @user_passes_test(is_superuser)
    def viewAdminProds(request):
        query = request.GET.get('query', '')
        if query:
            products = Producto.objects.filter(
                Q(nombre__icontains=query) |  # Busca productos cuyo nombre contiene la consulta
                Q(marca_marca_icontains=query) |  # Busca productos cuya marca contiene la consulta
                Q(categoria_categoria_icontains=query) # Busca productos cuya categoría contiene la consulta
            )# Filtra productos que contienen el término de búsqueda en nombre, marca o categoría
        else: 
            products = Producto.objects.all()
        return render(request, 'productosAdmin.html', {'productos':products, 'query':query})
    def agregarProd(request):
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Se ha guardado la información correctamente")
                return redirect('Productos:prodsAdmin')
            else:
                messages.error(request, "Hubo un error, revisa la información e intenta de nuevo.")
                form = ProductoForm()
        else:
            form = ProductoForm()
        return render(request, 'crudProds/addProduct.html', {'form' : form})
    def updatedProd(request, id):
        try:
            product = Producto.objects.get(pk=id) # Se debe obtener el producto por la 'clave primaria' (id)
        except Producto.DoesNotExist:
            return redirect('Productos:prodsAdmin')
        
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES, instance=product)
            if len(request.FILES) != 0:
                if len(product.imagen) > 0:
                    os.remove(product.imagen.path)
            if form.is_valid():
                form.save()
                messages.success(request, "Se ha actualizado la información correctamente.")
                return redirect('Productos:prodsAdmin')
        else:
            form = ProductoForm(instance=product) # Pre-popula el formulario con los datos del producto

        return render(request, 'crudProds/updatedProd.html', {'form': form})
    def delateProd(request, id):
        product = get_object_or_404(Producto, pk=id)
        if product.imagen and os.path.isfile(product.imagen.path):
            os.remove(product.imagen.path)

        product.delete()
        messages.success(request, "El producto se ha eliminado correctamente.")
        return redirect('Productos:prodsAdmin')
    
    # CATEGORÍA
    def viewCateg(request):
        categorias = Categoria.objects.all()
        context = {'categorias':categorias}
        return render(request, 'categorias/categorias.html', context)
    def addCateg(request):
        if request.method == 'POST':
            form = CategoriaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "La categoría se agrego correctamente.")
                return redirect('Productos:categorias')
            else:
                messages.error(request, "Hubo un error con la información, intentalo de nuevo.")
                form = CategoriaForm()
        else:
            form = CategoriaForm()
        return render(request, 'categorias/addCateg.html', {'form':form})
   
    def updatedCateg(request, id):
        try:
            categoria = Categoria.objects.get(pk=id)
        except Marca.DoesNotExist:
            return redirect('Productos:categorias')       
        if request.method == 'POST':
            form = CategoriaForm(request.POST, request.FILES,instance=categoria)
            if len(request.FILES) != 0:
                if len(categoria.imagen) > 0:
                    os.remove(categoria.imagen.path)
            if form.is_valid():
                messages.success(request, "Se actualizó correctamente la información.")
                form.save()
                return redirect('Productos:categorias')
            else:
                messages.error(request, "Hubo un error, verifica la información e intenta de nuevo.")
        else:
            form = CategoriaForm(instance=categoria)
        return render(request, 'categorias/addCateg.html', {'form':form})
    def delateCateg(request, id):
        categoria = get_object_or_404(Categoria, pk=id)
        
        categoria.delete()
        messages.success(request, "Se eliminó correctamente la categoría.")
        return redirect('Productos:categorias')

    # MARCA.
    def viewMarc(request):
        marcas = Marca.objects.all()
        context = {'marcas':marcas}
        return render(request, 'marcas/marcas.html', context)
    def addMarca(request):
        if request.method == 'POST':
            form = MarcaForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "La marca se agrego correctamente.")
                return redirect('Productos:marcas')
            else:
                messages.error(request, "Hubo un error con la información, intentalo de nuevo.")
                form = MarcaForm()
        else:
            form = MarcaForm()
        return render(request, 'marcas/addMarca.html', {'form':form})
    def updatedMarca(request, id):
        try:
            marca = Marca.objects.get(pk=id)
        except Marca.DoesNotExist:
            return redirect('Productos:marcas')
        
        if request.method == 'POST':
            form = MarcaForm(request.POST, instance=marca)
            if form.is_valid():
                messages.success(request, "Se actualizó correctamente la información.")
                form.save()
                return redirect('Productos:marcas')
            else:
                messages.error(request, "Hubo un error, verifica la información e intenta de nuevo.")
        else:
            form = MarcaForm(instance=marca)
        return render(request, 'marcas/addMarca.html', {'form':form})
    def delateMarca(request, id):
        marca = get_object_or_404(Marca, pk=id)
        
        marca.delete()
        messages.success(request, "Se eliminó correctamente la marca.")
        return redirect('Productos:marcas')

def promocion(request):
    promociones = Promocion.objects.all()
    return render(request, 'promocion.html', {'promociones': promociones})
from django.shortcuts import render, redirect
from .carro import Carro
from productos.models import Producto
from django.contrib.auth.decorators import login_required

@login_required(login_url="/usuario/register")
def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    precio = float(producto.precio)
    carro.agregar(producto=producto, precio=precio)
    return redirect("Productos:tProductos")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("carro:tCarro")

def sumar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.sumar(producto=producto)
    return redirect("carro:tCarro")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect("carro:tCarro")


def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar()
    return redirect("carro:tCarro")

def template_carro(request):
    return render(request, 'carro.html')

@login_required
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    precio = float(producto.precio)
    carro.agregar(producto=producto, precio=precio)
    return redirect("Productos:tProductos")

def pago(request):
    return render(request, 'pagar.html')
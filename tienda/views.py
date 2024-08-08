from django.shortcuts import render,redirect
from productos.models import Producto
from pasarelaPago.models import DetallePedido

def navegar(request):
    nombre_usuario = request.session.get('nombre_usuario')
    return render(request, 'navegar.html', {'nombre_usuario':nombre_usuario})

def cerrar_sesion(request):
    request.session.flush()
    return redirect('Usuario:login')

def historialCompra(request):
    if not request.user.is_authenticated:
        return redirect('Usuario:login')
    
    pedidos = DetallePedido.objects.filter(usuario=request.user)

    for pedido in pedidos:
        productos_info = pedido.get_productos_info()
        for producto in productos_info:
            producto_obj = Producto.objects.get(id=producto['id'])
            producto['nombre'] = producto_obj.nombre
            
    context = {
        'pedidos': pedidos,
    }
    return render(request, "historialCompra.html", context)  

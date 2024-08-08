from django.shortcuts import render, redirect
from contacto.models import Contacto
from productos.models import Producto
from usuario.models import User
#
from django.contrib.auth.decorators import user_passes_test

#
from pasarelaPago.models import DetallePedido
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def is_superuser(user):
    return user.is_superuser if user else False

@user_passes_test(is_superuser)
def viewPanelAdmin(request):
    producto = Producto.objects.all()
    user = User.objects.all()
    return render(request, 'admin/panelAdmin.html', {"productos": producto, "usuarios": user})

@user_passes_test(is_superuser)
def viewContacts(request):
    contactsInf = Contacto.objects.all()
    context = {'pqrs':contactsInf}
    return render(request, 'admin/contactoAdmin/pqrs.html', context)

@user_passes_test(is_superuser)
def reportes(request):
    return render(request, 'admin/reportes/reportes.html')

@user_passes_test(is_superuser)
def pedidos(request):
    pedidos = DetallePedido.objects.all()
    return render(request, 'admin/pedidos/pedidosUsuarios.html', {'pedidos': pedidos})

@user_passes_test(is_superuser)
def pdfCompras(request):
    if not request.user.is_authenticated:
        return redirect('Usuario:login')
    
    # Filtrar pedidos del usuario autenticado
    pedidos = DetallePedido.objects.filter(usuario=request.user)

    # Obtener información completa del producto
    for pedido in pedidos:
        productos_info = pedido.get_productos_info()
        for producto in productos_info:
            try:
                producto_obj = Producto.objects.get(id=producto['id'])
                producto['nombreProd'] = producto_obj.nombre  # Asegúrate de que la clave coincida con la plantilla
            except Producto.DoesNotExist:
                producto['nombreProd'] = 'Desconocido'  # O algún valor predeterminado si no se encuentra el producto

    # Ruta de la plantilla para el PDF
    template_path = 'admin/pedidos/pedidosUsuariosPdf.html'
    context = {
        'pedidos': pedidos,
    }

    # Crear respuesta PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="historial_compras.pdf"'

    # Renderizar la plantilla
    template = get_template(template_path)
    html = template.render(context)

    # Crear PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Manejar errores en la creación del PDF
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response

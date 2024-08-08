from django.shortcuts import render,redirect
from django.urls import reverse
from django.conf import settings
from paypalrestsdk import Payment
from carro.carro import Carro
import uuid
from .models import DetallePedido
from django.utils import timezone
from productos.models import Producto
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import paypalrestsdk

# Configuración del SDK de PayPal
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

@login_required
def CheckOut(request):
    carro = Carro(request)
    total = 0
    item_list = []
    for key, value in carro.carro.items():
        total += float(value['precio_unitario']) * value['cantidad']
        item_list.append({
            'name': value['producto'],
            'sku': key,
            'price': value['precio_unitario'],
            'currency': 'USD',
            'quantity': value['cantidad'],
        })

    payment = Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('pasarela:payment-return')),
            "cancel_url": request.build_absolute_uri(reverse('pasarela:payment-failed'))},
        "transactions": [{
            "item_list": {
                "items": item_list},
            "amount": {
                "total": str(total),
                "currency": "USD"},
            "description": "Compra en aplicación de Tu Mercado A La Mano."}]})
    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                return redirect(approval_url)
    else:
        return HttpResponse("Error en la creación del pago")
    
@login_required
def PaymentReturn(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    if not payment_id or not payer_id:
        return redirect('pasarela:payment-failed')
    
    payment = Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        carro = Carro(request)
        usuario = request.user

        #Guardar información de productos en lista(Json)
        productos_info = []
        precio_total = 0

        for item in payment.transactions[0].item_list.items:
            producto = Producto.objects.get(id=item.sku)
            productos_info.append({
                'id': producto.id, 
                'nombreProd': producto.nombre,
                'cantidad': int(item.quantity),
                'precio': float(item.price),
                })
            precio_total += float(item.price) * int(item.quantity)
            producto.actualizar_stock(item.quantity) # Se actualiza el stock.

        detallePedido = DetallePedido.objects.create(
            usuario = usuario,
            precio_total = precio_total,
            fechaOrden = timezone.now()
        )
        detallePedido.set_productos_info(productos_info)
        detallePedido.save()

            

        carro.limpiar()
        return render(request, 'payment-success.html')
    else:
        return redirect('pasarela:payment-failed')
    
def PaymentFailed(request):
    return render(request, 'payment-failed.html')
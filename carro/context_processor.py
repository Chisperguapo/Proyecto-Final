def importe_total_carro(request):
    total = 0
    cantidad = 0
    carro = request.session.get("carro", {})
    for value in carro.values():
        total += float(value["precio_unitario"]) * int(value["cantidad"])
        cantidad += int(value["cantidad"])
    return {'importe_total_carro': total, 'importe_cantidad':cantidad}

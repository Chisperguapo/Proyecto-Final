from django.db import models
from django.conf import settings
from django.utils import timezone
# Crear una lista para guardar los id's y luego recorrerlos con un for.
import json

class DetallePedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productos_info = models.TextField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fechaOrden = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Detalle pedido'
        verbose_name_plural = 'Detalles pedido'
    
    def __str__(self):
        return f"{self.usuario} - {self.producto} - {self.cantidad}"

    # Metodos para guardar id's en Json.
    def set_productos_info(self, productos_info):
        self.productos_info = json.dumps(productos_info)

    def get_productos_info(self):
        return json.loads(self.productos_info)
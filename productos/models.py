from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    categoria = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='productos/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.categoria
    

class Marca(models.Model):
    marca = models.CharField(max_length=25, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'

    def __str__(self):
        return self.marca



class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio_anterior = models.CharField(max_length=50, blank=True, null=True)
    precio = models.CharField(max_length=50)
    stock = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    fecha_vencimiento = models.DateField()
    imagen = models.ImageField(upload_to='productos/')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True, blank=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
    def __str__(self):
        return self.nombre
    
    # Metodo para actualizar el stock.
    def actualizar_stock(self, cantidad):
        self.stock -= cantidad
        self.save()
    
class Promocion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField()
    imagen2 = models.ImageField(blank=True)
    imagen3 = models.ImageField(blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    descuento = models.IntegerField()
    fechaTermino = models.DateField()

    class Meta:
        verbose_name = 'Promocion'
        verbose_name_plural = 'Promociones'

    def vigente(self):
        return timezone.now().date() <= self.fechaTermino
    
    def __str__(self):
        return f"Promoción #{self.id} - Descuento: {self.descuento}% - Producto: {self.producto.nombre}"
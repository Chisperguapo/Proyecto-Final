from django import forms 
from .models import Producto, Categoria, Marca

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'categoria', 'precio_anterior', 'precio', 'stock', 'descripcion', 'fecha_vencimiento', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'nombre', 'placeholder': 'Nombre'}),
            # 'marca': forms.TextInput(attrs={'class': 'marca', 'placeholder': 'Marca'}),
            # 'categoria': forms.TextInput(attrs={'class': 'categoria', 'placeholder': 'Categoría'}),
            'precio_anterior': forms.NumberInput(attrs={'class': 'precio_anterior', 'placeholder': 'Precio anterior'}),
            'precio': forms.NumberInput(attrs={'class': 'precio', 'placeholder': 'Precio'}),
            'stock': forms.TextInput(attrs={'class': 'stock', 'placeholder': 'Stock'}),
            'descripcion': forms.TextInput(attrs={'class': 'descripcion', 'placeholder': 'Descripción'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'fecha_vencimiento', 'placeholder': 'Fecha de vencimiento'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'imagen', 'placeholder': 'Imagen'}),
        }
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria', 'imagen']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'imagen1', 'placeholder': 'Imagen'}),
        }

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['marca']
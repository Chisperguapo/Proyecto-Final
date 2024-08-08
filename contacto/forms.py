from django import forms # Se hace uso del paquete 'forms'.
from .models import Contacto # Se importa del archivo 'models', el modelo 'Contacto'.

class ContactoForm(forms.ModelForm): # Se inicializa la 'class' para el formulario 'ContactoForm', que va tener cómo 'parametro' el paquete 'forms'.

    class Meta: # Se inicializa una subclase.
        model = Contacto # Se le indicó a la variable 'modelo', que va a tener el valor del modelo importado 'Contacto', 'model'es una palabra reservada.
        fields = ["nombre", "email", "mensaje", "tipo_contacto", "notificacion"] # Se le indica a la variable 'campos', que va a guardar una lista con unos campos en especial del 'modelo' 'Contacto', 'fields'es una palabra reservada.
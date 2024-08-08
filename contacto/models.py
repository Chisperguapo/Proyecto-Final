from django.db import models

# Inicialización de opciones del tipo de contacto:
opciones_pqrs = [
    [0, 'Peticiones'],
    [1, 'Quejas'],
    [2, 'Reclamos'],
    [3, 'Sugerencia'],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombres y apellidos') # Se le indica a la variable 'nombre' que va a almacenar un tipo de dato 'charfield' con una 'logitud' de 50chars y le asignamos un 'verbose_name' para el campo.
    email = models.EmailField(verbose_name="Correo electrónico") # Se le indica a la variable 'email' que va almacenar un tipo de dato 'emailfield' con 'verbose_name' para el campo.
    mensaje = models.TextField(verbose_name="Mensaje") # Se le indica a la variable 'mensaje' que va almacenar un información de tipo 'TextField' y se le asigana un 'verbose_name' para el nombre del campo.
    tipo_contacto = models.IntegerField(choices=opciones_pqrs, verbose_name="Razón del contacto") # Se le indica a la variable 'tipo_contacto' que va almacenar un valor de tipo 'IntegerField' y que va a tener unas 'choices' que se llaman en la variable ya inicializada 'opciones_pqrs' con un 'verbose_name' para el campo.
    notificacion = models.BooleanField(default=False, verbose_name="Recibir respuesta al correo") # Se le indica a la variable 'notificación' que va almacenar un valor de tipo 'BooleanField' el cuál por 'default' va estar desactivado y le agregamos un verbose name al campo.
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío") #Se le indica a la variable 'fecha_envio' que va a capturar un 'DateTimeFIeld' que va a tener un 'auto_now_add' en verdadero para la obtención de la fecha que se emite el formulario, con un 'verbose_name' para el campo.
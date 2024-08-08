from django.shortcuts import render, redirect  # Se hace uso de las librerías 'render' y 'redirect'.
from django.urls import reverse  # Se hace uso de la librería 'reverse'.
from . import forms  # Se importa el formulario 'ContactoForm' del archivo 'forms'.
from django.core.mail import EmailMessage

def contacto(request):  # Se inicializa una función con el nombre'contacto' que va a tener como parámetro un'request'.
    contacto_form = forms.ContactoForm()  # Se le da como valor el método'ContactoForm()' a la variable'contacto_form'.

    if request.method == 'POST':  # Se hace un condicional'if' para validar si el método'method' de respuesta'request' es igual'==' a posteo'POST', si es correcto se hará lo siguiente:
        contacto_form = forms.ContactoForm(data=request.POST)  # Se indica que la variable'contacto_form' va a dar una respuesta'request' para postear'POST' la información.
        if contacto_form.is_valid():  # Se anida otro condicional'if' el cual validará si el contenido de la variable'contacto_form' es válido'is_valid()', en caso de que sí:
            contacto_form.save()
            nombre = contacto_form.cleaned_data["nombre"]
            email = contacto_form.cleaned_data["email"]
            mensaje = contacto_form.cleaned_data["mensaje"]
            # correo_app = "webstorewarriors@gmail.com"
            correopqrs = EmailMessage("App Gestión de Pedidos Warriors", 
                                  "El usuario {} con Email {} envió el siguiente mensaje \n\n{}.".format(nombre, email, mensaje),
                                 "", ["webstorewarriors@gmail.com"], reply_to=[email])
            try:
                correopqrs.send()
                return redirect(reverse('AppContacto:pqrs') + '?ok')  # Y se retornará'return' una redirección'redirect()' a la URL asociada al patrón de URL nombrado'contact' y le concatenamos'+' un valor'?ok' a la url.
            except:
                return redirect(reverse('AppContacto:pqrs') + '?error')  # Y se retornará'return' una redirección'redirect()' a la URL asociada al patrón de URL nombrado'contact' y le concatenamos'+' un valor'?error' a la url.
    return render(request, 'contacto/contacto.html', { 'formulario' : contacto_form }) # Retornamos'return' una renderización'render' que va tener una respuesta'request' con una template'contacto/contacto.html' y el diccionario con los campos de la clase'contacto_form'.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login as login_active
from carro.carro import Carro
from django.core.mail import send_mail
from .models import User
from .forms import FormularioUser
#
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import update_session_auth_hash

# metodo para verificar si es super user
from appAdmin.views import is_superuser
from django.contrib.auth.decorators import user_passes_test

from productos.models import Producto
from pasarelaPago.models import DetallePedido
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import json

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Su cuenta ha sido creada exitosamente.')
            return redirect('Usuario:login')
        
        else:
            return render(request, 'usuario/register.html', {'form': form})  # Añade esta línea para devolver una respuesta en caso de formulario inválido
    else:
        form = UserRegistrationForm()
        return render(request, 'usuario/register.html', {'form': form})
   

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login_active(request, user)
                return redirect('Tienda:navegar')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def historial(request):
    return render(request, 'usuario/historial.html')

def configUser(request):
    return render(request, 'usuario/settings.html')

def configSecurity(request):
    return render(request, 'usuario/settingSecurity.html')

def viewRecoverPass(request):
    return render(request, 'recoverPassword.html')

class recoverPassword():
    def recoverPasswordStep1(request):
        if request.method == 'POST':
            emailUser = request.POST.get('correo_destino')
            user = User.objects.filter(email=emailUser).first()
            if user:
                uidb64 = urlsafe_base64_encode(str(user.id).encode())
                token = default_token_generator.make_token(user)
                # Se construye un enlace con el uidb64 y el token.
                reset_link = f"127.0.0.1:8000/changePassword/{uidb64}/{token}/"
                
                affair = 'Cambio de contraseña Tu mercado a la mano.'
                user_name = user.get_full_name() or user.email
                messageRecover = f'Hola, {user_name}. Para continuar con el reestablecimiento de su contraseña, haga clic en el siguiente enlace: {reset_link}'
                send_mail(affair, messageRecover, 'webstorewarriors@gmail.com', [emailUser])
                message = 'Favor revisar su correo, allí seguirá los últimos pasos para reestablecer su contraseña :]'
                return render(request, 'recoverPassword.html', {'message': message})
            else:
                message = 'El correo electrónico ingresado no se encuentra registrado.'
                return render(request, 'recoverPassword.html', {'message': message})
        else:
            return render(request, 'recoverPassword.html')


        
    def changePassword(request,uidb64, token):
        try: 
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if request.method == 'POST':
                new_password = request.POST.get('new_password')
                confirm_password = request.POST.get('confirm_password')
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user) # Mantener la sesión del usuario después de cambiar la contraseña
                    messages.success(request, "La contraseña se ha cambiado")
                    return render(request,'si_db.html') # Redirige a una vista de éxito
                else:
                    return render(request, 'changePassword.html', {'error': 'Las contraseñas no coinciden.'})
            else:
                return render(request, 'changePassword.html')
        else:
            return render(request, 'no_db.html')
        
class CrudUsuarios():
    @user_passes_test(is_superuser)
    def viewUsuarios(request):
        users = User.objects.all()
        context = {'users':users}
        return render(request, 'admin/usuarios.html', context)
    
    def delateUser(request, id):
        user = get_object_or_404(User, pk=id)
    
        user.delete()
        messages.success(request, 'Se eliminó correctamente el usuario.')
        return redirect('Usuario:usuarios')
    
    def editar(request, id):
        usuario = get_object_or_404(User, pk=id)
        if request.method == 'POST':
            form = FormularioUser(request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                messages.success(request,"Se actualizó el usuario")
                return redirect('Usuario:usuarios')
            else:
                messages.error(request, "Hubo un error, verifica la información e intenta de nuevo.")
        else:
            form = FormularioUser(instance=usuario)
        return render(request, 'admin/staff.html', {'form':form}) 
    
def generar_pdf(request):
    if not request.user.is_authenticated:
        return redirect('Usuario:login')
    
    pedidos = DetallePedido.objects.filter(usuario=request.user)

    for pedido in pedidos:
        productos_info = pedido.get_productos_info()
        for producto in productos_info:
            producto_obj = Producto.objects.get(id=producto['id'])
            producto['nombre'] = producto_obj.nombre

    template_path = 'historialCompra_pdf.html'
    context = {
        'pedidos': pedidos,
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="historial_compras.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response
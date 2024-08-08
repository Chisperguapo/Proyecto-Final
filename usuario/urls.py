from django.urls import path
from . import views
from .views import viewRecoverPass, recoverPassword, CrudUsuarios

app_name='Usuario'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('', views.login, name="login"),
    path('historial/', views.historial, name="historial"),
    path('config/', views.configUser, name="configUser"),
    path('confgSecu', views.configSecurity, name="security"),
    path('viewReco/', viewRecoverPass, name="viewReco"),
    path('recoverPasswordStep1/', recoverPassword.recoverPasswordStep1, name='recoverStep1'),
    path('changePassword/<str:uidb64>/<str:token>/', recoverPassword.changePassword, name="changePassword"),
    
    path('usuarios/', CrudUsuarios.viewUsuarios, name="usuarios"),
    path('usuario/<int:id>/', CrudUsuarios.delateUser, name="delateUser"),
    path('updatedUser/<int:id>/', CrudUsuarios.editar, name="updatedUser"),
    path('historial/pdf/', views.generar_pdf, name="generar_pdf"),
]
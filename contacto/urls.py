from django.urls import path
from . import views
app_name = 'AppContacto'

urlpatterns = [
    path('pqrs/', views.contacto, name="pqrs"),
]
from django.urls import path
from . import views

app_name = "pasarela"

urlpatterns = [
    path('checkout/', views.CheckOut, name='checkout'),
    path('payment-return/', views.PaymentReturn, name='payment-return'),
    path('payment-failed/', views.PaymentFailed, name='payment-failed'),
]
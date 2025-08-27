from django.urls import path
from . import views

urlpatterns = [
    path('cliente/nuevo/', views.crear_cliente, name='crear_cliente'),
    path('cliente/<int:pk>/', views.cliente_detalle, name='cliente_detalle'),
]

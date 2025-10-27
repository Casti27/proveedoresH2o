from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.crear_cliente, name='crear_cliente'),
    path('<int:pk>/', views.cliente_detalle, name='cliente_detalle'),
]

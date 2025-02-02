from django.urls import path
from .api_views import *

urlpatterns= [
    path('usuarios', listar_usuarios),
    path('empleados', listar_empleados),
    path('empleados_mejorado', listar_empleados_mejorado),
    path('clientes_mejorado', listar_clientes_mejorado),
    path('pedido_mejorado', listar_pedido_mejorado),
]
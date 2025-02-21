from django.urls import path
from .api_views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns= [
    path('usuarios', listar_usuarios),
    path('empleados', listar_empleados),
    path('empleados_mejorado', listar_empleados_mejorado),
    path('clientes_mejorado', listar_clientes_mejorado),
    path('pedido_mejorado', listar_pedido_mejorado),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    #Busqueda
    #Para hacer peticiones a la api usar la url 
    path('busquedasimpleempleados/',busquedaSimpleEmpleado,name='busquedaSimpleEmpleado'),
    
    path('busqueda-avanzada-empleados/',busquedaAvanzadaEmpleado,name='busquedaAvanzadaEmpleado'),
    path('busqueda-avanzada-clientes/',busquedaAvanzadaClientes,name='busquedaAvanzadaClientes'),
    path('busqueda-avanzada-pedidos/',busquedaAvanzadaPedidos,name='busquedaAvanzadaPedidos'),
    path('busqueda-avanzada-proveedor/',busquedaAvanzadaProveedor,name='busquedaAvanzadaProveedor'),

    #patch put delete proveedor
    path('proveedores/proveedores_listar/',proveedor_list),
    path('proveedores/crear/',proveedor_create),
    path('proveedores/<int:proveedor_id>/',proveedor_obtener),
    path('proveedores/editar/<int:proveedor_id>/',proveedores_editar),
    path('proveedores/editar/nombre/<int:proveedor_id>/',proveedores_editar_patch),
    path('proveedores/eliminar/<int:proveedor_id>/',proveedores_eliminar,name='proveedores_eliminar'),

    #patch put delete pedido metodo de pago
    path('pedido-metodopago_listar/', pedido_metodopago_lista, name='pedido_metodopago_lista'),
    path('pedido-metodopago/crear/', pedido_metodopago_crear, name='pedido_metodopago_crear'),
    path('pedido-metodopago/<int:pedido_id>/',pedido_metodopago_editar_put,name='pedido_metodopago_editar_put'),
    path('pedido-metodopago/editar/nombre/<int:pedido_id>/',pedido_metodopago_editar_patch,name='pedido_metodopago_editar_patch'),
    path('pedido-metodopago/eliminar/<int:proveedor_id>/',pedido_metodopago_eliminar,name='pedido_metodopago_eliminar'),

]
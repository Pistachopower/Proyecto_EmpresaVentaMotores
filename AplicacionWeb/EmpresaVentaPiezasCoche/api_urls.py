from django.urls import path, include
from .api_views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from rest_framework.routers import DefaultRouter

#Viewset
router = DefaultRouter()
router.register(
    r"pieza-motor-pedido", PiezaMotorPedidoViewSet, basename="pieza-motor-pedido"
)

urlpatterns = [
    path("usuarios", listar_usuarios),
    path("empleados", listar_empleados),
    path("empleados_mejorado", listar_empleados_mejorado),
    path("clientes_mejorado", listar_clientes_mejorado),
    path("pedido_mejorado", listar_pedido_mejorado),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Busqueda
    # Para hacer peticiones a la api usar la url
    path(
        "busquedasimpleempleados/",
        busquedaSimpleEmpleado,
        name="busquedaSimpleEmpleado",
    ),
    path(
        "busqueda-avanzada-empleados/",
        busquedaAvanzadaEmpleado,
        name="busquedaAvanzadaEmpleado",
    ),
    path(
        "busqueda-avanzada-clientes/",
        busquedaAvanzadaClientes,
        name="busquedaAvanzadaClientes",
    ),
    path(
        "busqueda-avanzada-pedidos/",
        busquedaAvanzadaPedidos,
        name="busquedaAvanzadaPedidos",
    ),
    path(
        "busqueda-avanzada-proveedor/",
        busquedaAvanzadaProveedor,
        name="busquedaAvanzadaProveedor",
    ),
    # patch put delete proveedor
    path("proveedores/proveedores_listar/", proveedor_list),
    path("proveedores/crear/", proveedor_create),
    path("proveedores/<int:proveedor_id>/", proveedor_obtener),
    path("proveedores/editar/<int:proveedor_id>/", proveedores_editar),
    path("proveedores/editar/nombre/<int:proveedor_id>/", proveedores_editar_patch),
    path(
        "proveedores/eliminar/<int:proveedor_id>/",
        proveedores_eliminar,
        name="proveedores_eliminar",
    ),
    # patch put delete pedido metodo de pago
    path("pedidos-lista/", pedidos_lista, name="pedidos_lista"),
    path("metodos-pago-lista/", metodos_pago__lista, name="pedidos_lista"),
    path("usuario-lista/", usuario_lista, name="usuario_lista"),
    path("clientes-lista/", clientes_lista, name="clientes_lista"),
    path("pedido-metodopago/crear/", pedidos_create, name="pedidos_create"),
    path(
        "pedido/eliminar/<int:pedido_id>/",
        pedido_eliminar,
        name="pedido_eliminar",
    ),
    path("pedido-metodopago/editar/nombre/<int:pedido_id>/", pedido_editar_patch),
    path("pedido-metodopago/editar/<int:pedido_id>/", pedidos_update),
    path("pedido-metodopago/<int:pedido_id>/", pedido_obtener),
    
    # Viewsets
    path("", include(router.urls)),
    
    
    #sesiones
    path('registrar/usuario',registrar_usuario.as_view()),
    path('usuario/token/<str:token>',obtener_usuario_token),
    
]

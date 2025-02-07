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
    path('busquedasimpleempleados',busquedaSimpleEmpleado,name='busquedaSimpleEmpleado'),
    
    path('busqueda-avanzada-empleados',busquedaAvanzadaEmpleado,name='busquedaAvanzadaEmpleado'),
]
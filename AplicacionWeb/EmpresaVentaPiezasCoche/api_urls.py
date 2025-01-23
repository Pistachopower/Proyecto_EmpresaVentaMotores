from django.urls import path
from .api_views import listar_clientes

urlpatterns = [
    path('clientes/', listar_clientes, name='listar_clientes'),  # Asegúrate de que esta línea esté correcta
]



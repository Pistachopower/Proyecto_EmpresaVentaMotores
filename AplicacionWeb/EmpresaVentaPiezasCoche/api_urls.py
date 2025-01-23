from django.urls import path

from .api_views import listar_clientes

urlpatterns = [
    #http://127.0.0.1:8000/api/v1/clientes/
    path('clientes/', listar_clientes, name='listar_clientes'),     #Es una buena práctica incluir una barra (/) al final de las URLs para que Django pueda manejarlas correctamente.
]



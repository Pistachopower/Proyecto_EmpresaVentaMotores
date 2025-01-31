from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import *


@api_view(['GET'])
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer= UsuarioSerializer(usuarios, many=True) #parámetro many=True, para indicar que serializamos muchos valores
    return Response(serializer.data)

@api_view(['GET'])
def listar_empleados(request):
    empleados = Empleado.objects.all()
    serializer= EmpleadoSerializer(empleados, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_empleados_mejorado(request):
    empleados = Empleado.objects.all()
    serializer= EmpleadoSerializerMejorado(empleados, many=True)
    return Response(serializer.data)
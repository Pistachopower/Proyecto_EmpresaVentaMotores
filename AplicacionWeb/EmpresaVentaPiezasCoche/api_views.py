from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import *
from django.db.models import Q


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

@api_view(['GET'])
def listar_clientes_mejorado(request):
    clientes = Cliente.objects.all()
    serializer= ClienteSerializerMejorado(clientes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_pedido_mejorado(request):
    pedido = Pedido.objects.all()
    serializer= PedidoSerializer_Mejorado(pedido, many=True)
    return Response(serializer.data)

#busqueda simple de empleados
@api_view(['GET'])
def busquedaSimpleEmpleado(request):
    #request.query_params: hace referencia de los parametros que vienen del cliente. ejemplo: busquedasimpleempleados/?textoBusqueda=HOLA
    formulario= BusquedaEmpleadoForm(request.query_params)
    
    if formulario.is_valid():
        #aqui lo que hacemos es obtener el valor que viene del cliente. ejemplo: textoBusqueda: HOLA
        texto = formulario.data.get('textoBusqueda')
        
        empleado= Empleado.objects.all()
        empleado= empleado.filter(
            
            Q(apellido__icontains=texto) |
            Q(cargo__icontains=texto) 
            )
        
        #convertimos el objeto a json
        serializer= EmpleadoSerializerMejorado(empleado, many=True)
        
        #enviamos los datos
        return Response(serializer.data)
    else:
        return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
                
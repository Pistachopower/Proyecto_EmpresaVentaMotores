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
    
    
@api_view(['GET'])
def busquedaAvanzadaEmpleado(request):
    # Si hay parámetros en la query
    if len(request.query_params) > 0:
        formulario = BusquedaEmpleadoFormAvanzado(request.query_params)
        
        if formulario.is_valid():
            # Obtener los datos del formulario
            empleado = formulario.cleaned_data.get('empleado')
            apellido = formulario.cleaned_data.get('apellido')
            cargo = formulario.cleaned_data.get('cargo')
            fecha_contratacion = formulario.cleaned_data.get('fecha_contratacion')
            
            # Si todos los campos están vacíos, devolvemos un error
            if not empleado and not apellido and not cargo and not fecha_contratacion:
                return Response({"error": "Debe proporcionar al menos un parámetro de búsqueda."}, status=status.HTTP_400_BAD_REQUEST)
            
            #hacemos la queryset para buscar los empleados
            QS_Empleado = Empleado.objects.all()
            
            # Filtramos por cada campo si se proporcionó
            if empleado:
                QS_Empleado = QS_Empleado.filter(empleado__icontains=empleado)
                print(QS_Empleado.query)
                
            if apellido:
                QS_Empleado = QS_Empleado.filter(apellido__icontains=apellido)
                print(QS_Empleado.query)
                
            if cargo:
                QS_Empleado = QS_Empleado.filter(cargo__icontains=cargo)
                print(QS_Empleado.query)
                
            if fecha_contratacion:
                QS_Empleado = QS_Empleado.filter(fecha_contratacion=fecha_contratacion)
                print(QS_Empleado.query)
            # Convertimos la queryset en un objeto serializado
            serializer = EmpleadoSerializerMejorado(QS_Empleado, many=True)


            
            # Devolvemos los datos
            return Response(serializer.data)
        else:
            # Si el formulario no es válido
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
    else:
        # Si no hay parámetros en la query
        return Response({"error": "Debe proporcionar al menos un parámetro de búsqueda."}, status=status.HTTP_400_BAD_REQUEST)
        
        
#busquedaAvanzadaClientes
@api_view(['GET'])
def busquedaAvanzadaClientes(request):
    # Si hay parámetros en la query
    if len(request.query_params) > 0:
        formulario = BusquedaAvanzadaClientesForm(request.query_params)
        
        if formulario.is_valid():
            # Obtener los datos del formulario
            cliente = formulario.cleaned_data.get('cliente')
            apellido = formulario.cleaned_data.get('apellido')
            tipo_clientes = formulario.cleaned_data.get('tipo_clientes')
            
            
            # Si todos los campos están vacíos, devolvemos un error
            if not cliente and not apellido  and not tipo_clientes:
                return Response({"error": "Debe proporcionar al menos un parámetro de búsqueda."}, status=status.HTTP_400_BAD_REQUEST)
            
            #hacemos la queryset para buscar los empleados
            QS_Cliente = Cliente.objects.all()
            
            # Filtramos por cada campo si se proporcionó
            if cliente:
                QS_Cliente = QS_Cliente.filter(cliente__icontains=cliente)
                
                
            if apellido:
                QS_Cliente = QS_Cliente.filter(apellido__icontains=apellido)
                
                
            if tipo_clientes:
                QS_Cliente = QS_Cliente.filter(tipo_clientes__icontains=tipo_clientes)
                

            # Convertimos la queryset en un objeto serializado
            serializer = ClienteSerializerMejorado(QS_Cliente, many=True)
            
       

            # Devolvemos los datos
            return Response(serializer.data)
        else:
            # Si el formulario no es válido
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
    else:
        # Si no hay parámetros en la query
        return Response({"error": "Debe proporcionar al menos un parámetro de búsqueda."}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def busquedaAvanzadaPedidos(request):
    # Si hay parámetros en la query
    if len(request.query_params) > 0:
        formulario = BusquedaAvanzadaPedidoForm(request.query_params)
        
        if formulario.is_valid():
            # Obtener los datos del formulario
            pedido = formulario.cleaned_data.get('pedido')
            fecha_pedido = formulario.cleaned_data.get('fecha_pedido')
            metodo_pago = formulario.cleaned_data.get('metodo_pago')
            
            
            # Si todos los campos están vacíos, devolvemos un error
            if not pedido and not fecha_pedido and not metodo_pago:
                return Response({"error": "Debe proporcionar al menos un parámetro de búsqueda."}, status=status.HTTP_400_BAD_REQUEST)
            
            #hacemos la queryset para buscar los empleados
            QS_Pedido = Pedido.objects.all()
            print(QS_Pedido)
            
            # Filtramos por cada campo si se proporcionó
            if pedido:
                QS_Pedido = QS_Pedido.filter(pedido__icontains=pedido)
                print(QS_Pedido)
                
                
            if fecha_pedido:
                QS_Pedido = QS_Pedido.filter(fecha_pedido__icontains=fecha_pedido)
                print(QS_Pedido)
                
                 
            if metodo_pago:
                QS_Pedido = QS_Pedido.filter(metodo_pago__metodo_pago__icontains=metodo_pago)
                print(QS_Pedido)
                

            # Convertimos la queryset en un objeto serializado
            serializer = PedidoSerializer_Mejorado(QS_Pedido, many=True)
            
       

            # Devolvemos los datos
            return Response(serializer.data)
        else:
            # Si el formulario no es válido
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
    else:
        # Si no hay parámetros en la query
        return Response({"error": "Debe proporcionar al menos un parámetro de búsqueda."}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def busquedaAvanzadaProveedor(request):
    # Si hay parámetros en la query
    if len(request.query_params) > 0:
        formulario = BusquedaAvanzadaProveedorForm(request.query_params)
        
        if formulario.is_valid():
            # Obtener los datos del formulario
            proveedor = formulario.cleaned_data.get('proveedor')
            telefono = formulario.cleaned_data.get('telefono')
            correo = formulario.cleaned_data.get('correo')
            
            
            # Si todos los campos están vacíos, devolvemos un error
            if not proveedor and not telefono and not correo:
                return Response({"error": "Debe proporcionar al menos un parámetro de búsqueda."}, status=status.HTTP_400_BAD_REQUEST)
            
            #hacemos la queryset para buscar los empleados
            QS_Proveedor = Proveedor.objects.all()
            print(QS_Proveedor)
            
            # Filtramos por cada campo si se proporcionó
            if proveedor:
                QS_Proveedor = QS_Proveedor.filter(proveedor__icontains=proveedor)
                print(QS_Proveedor)
                
                
            if telefono:
                QS_Proveedor = QS_Proveedor.filter(telefono__icontains=telefono)
                print(QS_Proveedor)
                
                 
            if correo:
                QS_Proveedor = QS_Proveedor.filter(correo__icontains=correo)
                print(QS_Proveedor)
                

            # Convertimos la queryset en un objeto serializado
            serializer = ProveedorSerializer(QS_Proveedor, many=True)
            
       

            # Devolvemos los datos
            return Response(serializer.data)
        else:
            # Si el formulario no es válido
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
    else:
        # Si no hay parámetros en la query
        return Response({"error": "Debe proporcionar al menos un parámetro de búsqueda."}, status=status.HTTP_400_BAD_REQUEST)
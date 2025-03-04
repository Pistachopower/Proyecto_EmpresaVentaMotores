from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .forms import *
from django.db.models import Q
from rest_framework.viewsets import ViewSet


@api_view(["GET"])
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(
        usuarios, many=True
    )  # parámetro many=True, para indicar que serializamos muchos valores
    return Response(serializer.data)


@api_view(["GET"])
def listar_empleados(request):
    empleados = Empleado.objects.all()
    serializer = EmpleadoSerializer(empleados, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def listar_empleados_mejorado(request):
    empleados = Empleado.objects.all()
    serializer = EmpleadoSerializerMejorado(empleados, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def listar_clientes_mejorado(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializerMejorado(clientes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def listar_pedido_mejorado(request):
    pedido = Pedido.objects.all()
    serializer = PedidoSerializer_Mejorado(pedido, many=True)
    return Response(serializer.data)


# busqueda simple de empleados
@api_view(["GET"])
def busquedaSimpleEmpleado(request):
    # request.query_params: hace referencia de los parametros que vienen del cliente. ejemplo: busquedasimpleempleados/?textoBusqueda=HOLA
    formulario = BusquedaEmpleadoForm(request.query_params)

    # aqui lo que hacemos es obtener el valor que viene del cliente. ejemplo: textoBusqueda: HOLA
    texto = formulario.data.get("textoBusqueda")

    empleado = Empleado.objects.filter(
        Q(apellido__icontains=texto) | Q(cargo__icontains=texto)
    )

    # convertimos el objeto a json
    serializer = EmpleadoSerializerMejorado(empleado, many=True)

    # enviamos los datos
    return Response(serializer.data)


@api_view(["GET"])
def busquedaAvanzadaEmpleado(request):
    # Si hay parámetros en la query
    if len(request.query_params) > 0:
        formulario = BusquedaEmpleadoFormAvanzado(request.query_params)

        if formulario.is_valid():
            # Obtener los datos del formulario
            empleado = formulario.cleaned_data.get("empleado")
            apellido = formulario.cleaned_data.get("apellido")
            cargo = formulario.cleaned_data.get("cargo")
            fecha_contratacion = formulario.cleaned_data.get("fecha_contratacion")

            # Si todos los campos están vacíos, devolvemos un error
            if not empleado and not apellido and not cargo and not fecha_contratacion:
                return Response(
                    {"error": "Debe proporcionar al menos un parámetro de búsqueda."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # hacemos la queryset para buscar los empleados
            QS_Empleado = Empleado.objects.select_related("empleadoUsuario")

            # Filtramos por cada campo si se proporcionó
            if empleado:
                QS_Empleado = QS_Empleado.filter(empleado__icontains=empleado)

            if apellido:
                QS_Empleado = QS_Empleado.filter(apellido__icontains=apellido)

            if cargo:
                QS_Empleado = QS_Empleado.filter(cargo__icontains=cargo)

            if fecha_contratacion:
                QS_Empleado = QS_Empleado.filter(fecha_contratacion=fecha_contratacion)

            # Convertimos la queryset en un objeto serializado
            serializer = EmpleadoSerializerMejorado(QS_Empleado, many=True)

            # Devolvemos los datos
            return Response(serializer.data)
        else:
            # Si el formulario no es válido
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        # Si no hay parámetros en la query
        return Response(
            {"error": "Debe proporcionar al menos un parámetro de búsqueda."},
            status=status.HTTP_400_BAD_REQUEST,
        )


# busquedaAvanzadaClientes
@api_view(["GET"])
def busquedaAvanzadaClientes(request):
    # Si hay parámetros en la query
    if len(request.query_params) > 0:
        formulario = BusquedaAvanzadaClientesForm(request.query_params)

        if formulario.is_valid():
            # Obtener los datos del formulario
            cliente = formulario.cleaned_data.get("cliente")
            apellido = formulario.cleaned_data.get("apellido")
            tipo_clientes = formulario.cleaned_data.get("tipo_clientes")

            # Si todos los campos están vacíos, devolvemos un error
            if not cliente and not apellido and not tipo_clientes:
                return Response(
                    {"error": "Debe proporcionar al menos un parámetro de búsqueda."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # hacemos la queryset para buscar los empleados
            QS_Cliente = Cliente.objects.select_related("empleado", "clienteUsuario")

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
        return Response(
            {"error": "Debe proporcionar al menos un parámetro de búsqueda."},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def busquedaAvanzadaPedidos(request):
    # Si hay parámetros en la query
    if len(request.query_params) > 0:
        formulario = BusquedaAvanzadaPedidoForm(request.query_params)

        if formulario.is_valid():
            # Obtener los datos del formulario
            pedido = formulario.cleaned_data.get("pedido")
            fecha_pedido = formulario.cleaned_data.get("fecha_pedido")
            metodo_pago = formulario.cleaned_data.get("metodo_pago")

            # Si todos los campos están vacíos, devolvemos un error
            if not pedido and not fecha_pedido and not metodo_pago:
                return Response(
                    {"error": "Debe proporcionar al menos un parámetro de búsqueda."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # hacemos la queryset para buscar los empleados
            QS_Pedido = Pedido.objects.select_related("cliente", "usuario_Pedido")

            # Filtramos por cada campo si se proporcionó
            if pedido:
                QS_Pedido = QS_Pedido.filter(pedido__icontains=pedido)

            if fecha_pedido:
                QS_Pedido = QS_Pedido.filter(fecha_pedido__icontains=fecha_pedido)

            if metodo_pago:
                QS_Pedido = QS_Pedido.filter(
                    metodo_pago__metodo_pago__icontains=metodo_pago
                )

            # Convertimos la queryset en un objeto serializado
            serializer = PedidoSerializer_Mejorado(QS_Pedido, many=True)

            # Devolvemos los datos
            return Response(serializer.data)
        else:
            # Si el formulario no es válido
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        # Si no hay parámetros en la query
        return Response(
            {"error": "Debe proporcionar al menos un parámetro de búsqueda."},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def busquedaAvanzadaProveedor(request):
    # Si hay parámetros en la query
    if len(request.query_params) > 0:
        formulario = BusquedaAvanzadaProveedorForm(request.query_params)

        if formulario.is_valid():
            # Obtener los datos del formulario
            proveedor = formulario.cleaned_data.get("proveedor")
            telefono = formulario.cleaned_data.get("telefono")
            correo = formulario.cleaned_data.get("correo")

            # Si todos los campos están vacíos, devolvemos un error
            if not proveedor and not telefono and not correo:
                return Response(
                    {"error": "Debe proporcionar al menos un parámetro de búsqueda."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # hacemos la queryset para buscar los empleados
            QS_Proveedor = Proveedor.objects.all()

            # Filtramos por cada campo si se proporcionó
            if proveedor:
                QS_Proveedor = QS_Proveedor.filter(proveedor__icontains=proveedor)

            if telefono:
                QS_Proveedor = QS_Proveedor.filter(telefono__icontains=telefono)

            if correo:
                QS_Proveedor = QS_Proveedor.filter(correo__icontains=correo)

            # Convertimos la queryset en un objeto serializado
            serializer = ProveedorSerializer(QS_Proveedor, many=True)

            # Devolvemos los datos
            return Response(serializer.data)
        else:
            # Si el formulario no es válido
            return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        # Si no hay parámetros en la query
        return Response(
            {"error": "Debe proporcionar al menos un parámetro de búsqueda."},
            status=status.HTTP_400_BAD_REQUEST,
        )


# post patch put delete
@api_view(["GET"])
def proveedor_list(request):
    if request.user.has_perm('EmpresaVentaPiezasCoche.view_proveedor'):
        proveedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedor, many=True)
        return Response(serializer.data)
    
    return Response("No tiene permisos para ver proveedores", status=status.HTTP_403_FORBIDDEN)


@api_view(["POST"])
def proveedor_create(request):
    print(request.data)
    proveedorCreateSerializer = ProveedorSerializerCreate(data=request.data)
    if proveedorCreateSerializer.is_valid():
        try:
            proveedorCreateSerializer.save()
            return Response("proveedor CREADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print(repr(error))
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(
            proveedorCreateSerializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def proveedor_obtener(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    serializer = ProveedorSerializer(proveedor)
    return Response(serializer.data)


@api_view(["PUT"])
def proveedores_editar(request, proveedor_id):
    proveedores = Proveedor.objects.get(id=proveedor_id)
    proveedoresCreateSerializer = ProveedorSerializerCreate(
        data=request.data, instance=proveedores
    )
    if proveedoresCreateSerializer.is_valid():
        try:
            proveedoresCreateSerializer.save()
            return Response("Proveedor EDITADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(
            proveedoresCreateSerializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["PATCH"])
def proveedores_editar_patch(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    proveedoresCreateSerializer = ProveedorSerializerActualizarNombre(
        proveedor, data=request.data, partial=True
    )
    if proveedoresCreateSerializer.is_valid():
        try:
            proveedoresCreateSerializer.save()
            return Response("Proveedor EDITADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(
            proveedoresCreateSerializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["DELETE"])
def proveedores_eliminar(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    try:
        proveedor.delete()
        return Response("proveedor ELIMINADO")  # PREGUNTAR A JORGE
    except Exception as error:
        return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# pedido metodo de pago
@api_view(["GET"])
def pedidos_lista(request):
    if request.user.has_perm('EmpresaVentaPiezasCoche.view_pedido'):
        pedidos = Pedido.objects.select_related("metodo_pago").all()
        serializer = PedidoSerializer_Mejorado(pedidos, many=True)
        return Response(serializer.data)
    
    return Response("No tiene permisos para ver pedidos", status=status.HTTP_403_FORBIDDEN)


@api_view(["GET"])
def metodos_pago__lista(request):
    metodosPago = MetodoPago.objects.all()
    serializer = MetodoPagoSerializer(metodosPago, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def usuario_lista(request):
    usuario = Usuario.objects.all()
    serializer = UsuarioSerializer(usuario, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def clientes_lista(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def pedidos_create(request):
    serializer = PedidoConMetodoPagoSerializerCreate(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response("pedido CREADO")
        except serializer.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print(repr(error))
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def pedidos_update(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    serializer = PedidoConMetodoPagoSerializerUpdate(pedido, data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response("Pedido ACTUALIZADO")
        except serializer.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print(repr(error))
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# pedido_eliminar
@api_view(["DELETE"])
def pedido_eliminar(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    try:
        pedido.delete()
        return Response("pedido ELIMINADO")
    except Exception as error:
        return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# pedido_editar_patch
@api_view(["PATCH"])
def pedido_editar_patch(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    pedidoCreateSerializer = PedidoConMetodoPagoSerializerCreate(
        pedido, data=request.data, partial=True
    )
    if pedidoCreateSerializer.is_valid():
        try:
            pedidoCreateSerializer.save()
            return Response("Nombre de pedido EDITADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(
            pedidoCreateSerializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def pedido_obtener(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    serializer = PedidoSerializer_Mejorado(pedido)
    
    if request.user.has_perm('EmpresaVentaPiezasCoche.special_access'):
        return Response(serializer.data)  
    
    
    return Response({"error": "No tienes permiso"}, status=403)  
    


# VIEWSETS


class PiezaMotorPedidoViewSet(ViewSet):
    def list(self, request):
        queryset = PiezaMotor_Pedido.objects.all()
        serializer = PiezaMotorPedidoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PiezaMotorPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=201
            )  # Respuesta de creación exitosa
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        pieza_motor_pedido = PiezaMotor_Pedido.objects.get(pk=pk)
        serializer = PiezaMotorPedidoSerializer(pieza_motor_pedido)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pieza_motor_pedido = PiezaMotor_Pedido.objects.get(pk=pk)
        serializer = PiezaMotorPedidoSerializer(
            pieza_motor_pedido, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk=None):
        pieza_motor_pedido = PiezaMotor_Pedido.objects.get(pk=pk)
        serializer = PiezaMotorPedidoSerializer(
            pieza_motor_pedido, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        pieza_motor_pedido = PiezaMotor_Pedido.objects.get(pk=pk)
        pieza_motor_pedido.delete()
        return Response(status=204)  # Respuesta de eliminación exitosa



#SESIONES 
from rest_framework import generics
from rest_framework.permissions import AllowAny
class registrar_usuario(generics.CreateAPIView):
    serializer_class = UsuarioSerializerRegistro
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializers = UsuarioSerializerRegistro(data=request.data)
        if serializers.is_valid():
            try:
                rol = request.data.get('rol')
                #creacion del usuario
                user = Usuario.objects.create_user(
                        nombre= serializers.data.get("nombre"),
                        last_name= serializers.data.get("last_name"),
                        telefono= serializers.data.get("telefono"),
                        username = serializers.data.get("username"), 
                        correo = serializers.data.get("correo"), 
                        password = serializers.data.get("password1"),
                        rol = rol,
                        )
                
                #Creación de perfil según rol:
                if(rol == Usuario.CLIENTE):
                    cliente = Cliente.objects.create( usuario = user)
                    cliente.save()
                elif(rol == Usuario.EMPLEADO):
                    empleado = Empleado.objects.create(usuario = user)
                    empleado.save()
                usuarioSerializado = UsuarioSerializer(user)
                return Response(usuarioSerializado.data)
            except Exception as error:
                print(repr(error))
                return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

from oauth2_provider.models import AccessToken     
@api_view(['GET'])
def obtener_usuario_token(request,token):
    # Aquí se busca en la base de datos el AccessToken.
    ModeloToken = AccessToken.objects.get(token=token)
    
    #Aquí se obtiene el usuario dueño del token.
    usuario = Usuario.objects.get(id=ModeloToken.user_id)
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)


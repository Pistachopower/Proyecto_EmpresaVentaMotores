Añadir los permisos correspondiente en la API y documentar en el README(API), que tipo de usuario tiene acceso a cada apartado 

En esta vista: 
@api_view(["GET"])
def pedidos_lista(request):
    if request.user.has_perm('EmpresaVentaPiezasCoche.view_pedido'):
        pedidos = Pedido.objects.select_related("metodo_pago").all()
        serializer = PedidoSerializer_Mejorado(pedidos, many=True)
        return Response(serializer.data)
    return Response("No tiene permisos para ver pedidos", status=status.HTTP_403_FORBIDDEN)


Solo el administrador y los empleados cuentan con los permisos de listar los pedidos. 


En esta vista:
@api_view(["PUT"])
def pedidos_update(request, pedido_id):
    if not request.user.has_perm('EmpresaVentaPiezasCoche.change_pedido'):
        return Response("No tiene permisos para actualizar pedidos", status=status.HTTP_403_FORBIDDEN)
    
    pedido = Pedido.objects.get(id=pedido_id)
    serializer = PedidoConMetodoPagoSerializerUpdate(pedido, data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response("Pedido ACTUALIZADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print(repr(error))
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

Pueden editar los pedidos el administrador y los empleados

En esta vista: 
@api_view(["DELETE"])
def pedido_eliminar(request, pedido_id):
    if request.user.has_perm('EmpresaVentaPiezasCoche.delete_pedido'):
        pedido = Pedido.objects.get(id=pedido_id)
        try:
            pedido.delete()
            return Response("pedido ELIMINADO")
        except Exception as error:
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response("No tienes permisos para eliminar pedidos", status=status.HTTP_403_FORBIDDEN)

Pueden borrar el administrador y el cliente


En esta vista:
@api_view(["POST"])
def pedidos_create(request):
    data = request.data.copy()
    data['usuario_Pedido'] = request.user.id  # Asocia el pedido al usuario autenticado.
    serializer = PedidoConMetodoPagoSerializerCreate(data=data)
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

Pueden crear pedidos los clientes y el administrador


En esta vista:
@api_view(["GET"])
def proveedor_list(request):
    if request.user.has_perm('EmpresaVentaPiezasCoche.view_proveedor'):
        proveedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedor, many=True)
        return Response(serializer.data)
    return Response("No tiene permisos para ver proveedores", status=status.HTTP_403_FORBIDDEN)

Pueden ver los proveedores el administrador y empleados

En esta vista:
@api_view(["POST"])
def proveedor_create(request):
    proveedorCreateSerializer = ProveedorSerializerCreate(data=request.data)
    if proveedorCreateSerializer.is_valid():
        try:
            proveedorCreateSerializer.save()
            return Response("proveedor CREADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(proveedorCreateSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

Pueden crear proveedores el administrador y empleados

En esta vista: 
@api_view(["PUT"])
def proveedores_editar(request, proveedor_id):
    proveedores = Proveedor.objects.get(id=proveedor_id)
    proveedoresCreateSerializer = ProveedorSerializerCreate(data=request.data, instance=proveedores)
    if proveedoresCreateSerializer.is_valid():
        try:
            proveedoresCreateSerializer.save()
            return Response("Proveedor EDITADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(proveedoresCreateSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

Pueden editar proveedores el administrador y empleados

En esta vista:
@api_view(["PATCH"])
def proveedores_editar_patch(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    proveedoresCreateSerializer = ProveedorSerializerActualizarNombre(proveedor, data=request.data, partial=True)
    if proveedoresCreateSerializer.is_valid():
        try:
            proveedoresCreateSerializer.save()
            return Response("Proveedor EDITADO")
        except serializers.ValidationError as error:
            return Response(error.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(proveedoresCreateSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

Pueden editar nombre del proveedor el administrador y empleados

En esta vista: 
@api_view(["DELETE"])
def proveedores_eliminar(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    try:
        proveedor.delete()
        return Response("proveedor ELIMINADO")
    except Exception as error:
        return Response(repr(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

Pueden borrar el proveedor el administrador y empleados

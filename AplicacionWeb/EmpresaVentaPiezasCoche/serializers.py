from rest_framework import serializers
from .models import *
from .forms import *

#aqui es donde se crea a partir de los modelos a json y viceversa


# Serializer para Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    # obtiene el valor legible del rol segun el usuario
    rol_display = serializers.CharField(source='get_rol_display', read_only=True)  

    class Meta:
        model = Usuario
        fields = (
            'id', 
            'username',  # Campo heredado de AbstractUser
            'rol', 
            'rol_display',
            'nombre', 
            'telefono', 
            'correo',
        )

# Serializer para Empleado
class EmpleadoSerializer(serializers.ModelSerializer):
    # Incluye información del Usuario relacionado
    empleadoUsuario = UsuarioSerializer()  


    class Meta: #hace referencia al modelo y sus atributos
        model = Empleado
        fields = (
            'id',
            'empleadoUsuario', 
            'empleado', 
            'apellido', 
            'cargo', 
            'fecha_contratacion',
        )

# Serializer para Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = (
            'id', 
            'proveedor', 
            'telefono', 
            'correo', 
            'direccion',
        )

# Serializer para Cliente
class ClienteSerializer(serializers.ModelSerializer):
    clienteUsuario = UsuarioSerializer()  # Incluye información del Usuario relacionado
    empleado = EmpleadoSerializer()  # Incluye información del Empleado asignado
    tipo_clientes_display = serializers.CharField(source='get_tipo_clientes_display', read_only=True)  # Valor legible del choice

    class Meta:
        model = Cliente
        fields = (
            'id', 
            'clienteUsuario', 
            'cliente', 
            'apellido', 
            'correo', 
            'tipo_clientes', 
            'tipo_clientes_display', 
            'direccion', 
            'empleado',
        )

# Serializer para MetodoPago
class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = (
            'id', 
            'metodo_pago', 
            'nombre', 
            'tipo_pago', 
            'fecha_creacion', 
            'fecha_ultima_actualizacion', 
            'pagado',
        )

# Serializer para Pedido
class PedidoSerializer(serializers.ModelSerializer):
    metodo_pago = MetodoPagoSerializer()  # Incluye detalles del método de pago
    cliente = ClienteSerializer()  # Incluye detalles del cliente
    usuario_Pedido = UsuarioSerializer()  # Incluye detalles del usuario
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)  # Valor legible del estado

    class Meta:
        model = Pedido
        fields = (
            'id', 
            'pedido', 
            'fecha_pedido', 
            'total_importe', 
            'estado', 
            'estado_display', 
            'metodo_pago', 
            'cliente', 
            'usuario_Pedido',
        )

# Serializer para PiezaMotor
class PiezaMotorSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(many=True, read_only=True)  # Incluye los proveedores relacionados
    pedido = PedidoSerializer(many=True, read_only=True)  # Incluye los pedidos relacionados

    class Meta:
        model = PiezaMotor
        fields = (
            'id', 
            'pieza', 
            'proveedor', 
            'pedido', 
            'precio', 
            'descripcion', 
            'stock_disponible',
        )

# Serializer para la tabla intermedia PiezaMotor_Pedido
class PiezaMotorPedidoSerializer(serializers.ModelSerializer):
    pieza = PiezaMotorSerializer()  # Incluye detalles de la pieza
    pedido = PedidoSerializer()  # Incluye detalles del pedido

    class Meta:
        model = PiezaMotor_Pedido
        fields = (
            'id', 
            'pieza', 
            'pedido', 
            'cantidad', 
            'precioTotal',
        )


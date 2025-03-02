from rest_framework import serializers
from .models import *
from .forms import *

# aqui es donde se crea a partir de los modelos a json y viceversa


# Serializer para Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    # obtiene el valor legible del rol segun el usuario
    rol = serializers.CharField(source="get_rol_display", read_only=True)

    class Meta:
        model = Usuario
        fields = (
            "id",
            "username",  # Campo heredado de AbstractUser
            "rol",
            "nombre",
            "telefono",
            "correo",
        )


# Serializer para Empleado
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:  # hace referencia al modelo y sus atributos
        model = Empleado
        fields = (
            "id",
            "empleadoUsuario",
            "empleado",
            "apellido",
            "cargo",
            "fecha_contratacion",
        )


# mejorado
class EmpleadoSerializerMejorado(serializers.ModelSerializer):
    # Incluye información del Usuario relacionado
    empleadoUsuario = UsuarioSerializer()

    # Para formatear Fechas
    fecha_contratacion = serializers.DateField(format=("%d-%m-%Y"))

    class Meta:  # hace referencia al modelo y sus atributos
        model = Empleado
        fields = (
            "empleadoUsuario",
            "empleado",
            "apellido",
            "cargo",
            "fecha_contratacion",
        )


# Serializer para Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = (
            "id",
            "proveedor",
            "telefono",
            "correo",
            "direccion",
        )


# Serializer para Cliente
class ClienteSerializer(serializers.ModelSerializer):
    clienteUsuario = UsuarioSerializer()  # Incluye información del Usuario relacionado
    empleado = EmpleadoSerializer()  # Incluye información del Empleado asignado

    class Meta:
        model = Cliente
        fields = (
            "id",
            "clienteUsuario",
            "cliente",
            "apellido",
            "correo",
            "tipo_clientes",
            "direccion",
            "empleado",
        )


class ClienteSerializerMejorado(serializers.ModelSerializer):
    clienteUsuario = UsuarioSerializer()  # Incluye información del Usuario relacionado
    tipo_clientes = serializers.CharField(
        source="get_tipo_clientes_display", read_only=True
    )  # Valor legible del choice

    class Meta:
        model = Cliente
        fields = (
            "id",
            "clienteUsuario",
            "cliente",
            "apellido",
            "correo",
            "tipo_clientes",
            "direccion",
            "empleado",
        )


# Serializer para MetodoPago
class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = (
            "id",
            "metodo_pago",
            "nombre",
            "tipo_pago",
            "fecha_creacion",
            "fecha_ultima_actualizacion",
            "pagado",
        )


# Serializer para Pedido mejorado
class PedidoSerializer_Mejorado(serializers.ModelSerializer):
    metodo_pago = MetodoPagoSerializer()  # Incluye detalles del método de pago
    cliente = ClienteSerializer()  # Incluye detalles del cliente
    usuario_Pedido = UsuarioSerializer()  # Incluye detalles del usuario
    estado_display = serializers.CharField(
        source="get_estado_display", read_only=True
    )  # Valor legible del estado
    # Para formatear Fechas
    fecha_pedido = serializers.DateField(format=("%d-%m-%Y"))

    class Meta:
        model = Pedido
        fields = (
            "id",
            "pedido",
            "fecha_pedido",
            "total_importe",
            "estado",
            "estado_display",
            "metodo_pago",
            "cliente",
            "usuario_Pedido",
        )


# Serializer para PiezaMotor
class PiezaMotorSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(
        many=True, read_only=True
    )  # Incluye los proveedores relacionados
    pedido = PedidoSerializer_Mejorado(
        many=True, read_only=True
    )  # Incluye los pedidos relacionados

    class Meta:
        model = PiezaMotor
        fields = (
            "id",
            "pieza",
            "proveedor",
            "pedido",
            "precio",
            "descripcion",
            "stock_disponible",
        )


# Serializer para la tabla intermedia PiezaMotor_Pedido
class PiezaMotorPedidoSerializer(serializers.ModelSerializer):
    # pieza = PiezaMotorSerializer()  # Incluye detalles de la pieza
    # pedido = PedidoSerializer_Mejorado()  # Incluye detalles del pedido

    class Meta:
        model = PiezaMotor_Pedido
        fields = (
            "id",
            "pieza",
            "pedido",
            "cantidad",
            "precioTotal",
        )


# post delete patch (CAMBIAR EL NOMBRE DE LA CLASE A ACTUALIZAR)
class ProveedorSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = ["proveedor", "telefono", "correo", "direccion"]

    def validate_proveedor(self, proveedor_nombre):
        proveedor = Proveedor.objects.filter(proveedor=proveedor_nombre).first()
        if not proveedor is None:  # sino es nulo
            if proveedor.proveedor == proveedor_nombre:
                raise serializers.ValidationError(
                    "Ya existe un proveedor con ese nombre"
                )

        return proveedor_nombre

    def validate_telefono(self, telefono_proveedor):
        proveedor = Proveedor.objects.filter(telefono=telefono_proveedor).first()
        if not proveedor is None:  # sino esta vacio
            if proveedor.telefono == telefono_proveedor:
                raise serializers.ValidationError(
                    "Ya existe un proveedor con ese telefono"
                )

        return telefono_proveedor

    def validate_correo(self, correo_proveedor):
        proveedor = Proveedor.objects.filter(correo=correo_proveedor).first()
        if not proveedor is None:
            if proveedor.correo == correo_proveedor:
                raise serializers.ValidationError(
                    "Ya existe un proveedor con ese correo"
                )

        return correo_proveedor

    def validate_direccion(self, direccion_proveedor):
        proveedor = Proveedor.objects.filter(direccion=direccion_proveedor).first()
        if not proveedor is None:
            if proveedor.direccion == direccion_proveedor:
                raise serializers.ValidationError(
                    "Ya existe un proveedor con ese direccion"
                )
        return direccion_proveedor


class ProveedorSerializerActualizarNombre(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = ["proveedor"]

    def validate_proveedor(self, proveedor_nombre):
        proveedor = Proveedor.objects.filter(proveedor=proveedor_nombre).first()
        if not proveedor is None:  # sino es nulo
            if proveedor.proveedor == proveedor_nombre:
                raise serializers.ValidationError("El proveedor ya existe")
        return proveedor_nombre


# pedido metodo de pago
class PedidoConMetodoPagoSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = "__all__"

    def validate_pedido(self, pedido_nombre):
        pedido = Pedido.objects.filter(pedido=pedido_nombre).first()
        if not pedido is None:  # sino es nulo
            if pedido.pedido == pedido_nombre:
                raise serializers.ValidationError("El pedido ya existe")
        return pedido_nombre

    def validate_fecha_pedido(self, pedido_fecha):
        fechaHoy = date.today()
        if pedido_fecha != fechaHoy:
            raise serializers.ValidationError("La fecha del pedido debe ser hoy")
        return pedido_fecha

    def validate_metodo_pago(self, metodo):
        metodobd = MetodoPago.objects.get(id=metodo.id)
        if metodobd is None:
            raise serializers.ValidationError("El metodo seleccionado no existe")
        return metodo

    def validate_usuario_Pedido(self, usuario):
        usuariobd = Usuario.objects.get(id=usuario.id)
        if usuariobd is None:
            raise serializers.ValidationError("El usuario seleccionado no existe")
        return usuario


class PedidoConMetodoPagoSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = "__all__"

    # def validate_pedido(self, pedido_nombre):
    #     pedido = Pedido.objects.filter(pedido=pedido_nombre).first()
    #     if not pedido is None:
    #         raise serializers.ValidationError("El pedido a actualizar no existe")
    #     return pedido_nombre

    def validate_fecha_pedido(self, pedido_fecha):
        fechaHoy = date.today()
        if pedido_fecha > fechaHoy:
            raise serializers.ValidationError(
                "La fecha del pedido no puede ser posterior a hoy"
            )
        return pedido_fecha

    def validate_metodo_pago(self, metodo):
        metodobd = MetodoPago.objects.get(id=metodo.id)
        if metodobd is None:
            raise serializers.ValidationError("El metodo seleccionado no existe")
        return metodo

    def validate_usuario_Pedido(self, usuario):
        usuariobd = Usuario.objects.get(id=usuario.id)
        if usuariobd is None:
            raise serializers.ValidationError("El usuario seleccionado no existe")
        return usuario


class PedidoSerializerActualizarNombre(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ["id", "pedido"]

    def validate_pedido(self, pedido_nombre):
        pedido = Pedido.objects.filter(pedido=pedido_nombre).first()
        if not pedido is None:  # sino es nulo
            if pedido.pedido == pedido_nombre:
                raise serializers.ValidationError("El nombre del pedido ya existe")
        return pedido_nombre


# SESIONES
class UsuarioSerializerRegistro(serializers.Serializer):
    username = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    correo = serializers.EmailField()
    rol = serializers.IntegerField()
    nombre = serializers.CharField()
    last_name = serializers.CharField()

    def validate_username(self, username):
        usuario = Usuario.objects.filter(username=username).first()
        if not usuario is None:
            raise serializers.ValidationError("Ya existe un usuario con ese nombre")
        return username

    def validate_last_name(self, last_name):
        print(last_name)
        return last_name

    def validate_nombre(self, nombre):
        print(nombre)
        return nombre

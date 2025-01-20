Formulario de Widgets

Este proyecto contiene un conjunto de formularios para la gestión de clientes, proveedores, piezas de motor y métodos de pago, así como los filtros de búsqueda correspondientes.

Formularios

Cliente:
    cliente = forms.CharField(required=False, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce nombre cliente'}))

Proveedor:
    correo = forms.EmailField(required=False, label="Correo Electrónico", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el correo electrónico'}))

Pieza de Motor:
    precio_min = forms.DecimalField(
        required=False, 
        label="Precio mínimo", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el precio mínimo', 'step': '0.01'})
    )
    
    precio_max = forms.DecimalField(
        required=False, 
        label="Precio máximo", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el precio máximo', 'step': '0.01'})
    )

Método de Pago:
    fecha_creacion = forms.DateField(
        required=False,
        label="Fecha de Creación",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD',
            'type': 'date'
        })
    )
    
    fecha_ultima_actualizacion = forms.DateField(
        required=False,
        label="Fecha de Última Actualización",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'YYYY-MM-DD',
            'type': 'date'
        })
    )

Filtros de Búsqueda

Clientes:
    if cliente:
        clientes = clientes.filter(cliente__icontains=cliente)
        mensaje_busqueda += f"Nombre que contenga: {cliente}\n"

    if apellido:
        clientes = clientes.filter(apellido__icontains=apellido)
        mensaje_busqueda += f"Apellido que contenga: {apellido}\n"

    if correo:
        clientes = clientes.filter(correo__icontains=correo)
        mensaje_busqueda += f"Correo que contenga: {correo}\n"

    if tipo_clientes:
        clientes = clientes.filter(tipo_clientes=tipo_clientes)
        mensaje_busqueda += f"Tipo de cliente: {tipo_clientes}\n"

    if direccion:
        clientes = clientes.filter(direccion__icontains=direccion)
        mensaje_busqueda += f"Dirección que contenga: {direccion}\n"

    if empleado:
        clientes = clientes.filter(empleado__empleado__icontains=empleado)
        mensaje_busqueda += f"Empleado que contenga: {empleado}\n"

Proveedores:
    if proveedor:
        proveedores = proveedores.filter(proveedor__icontains=proveedor)
        mensaje_busqueda += f"Nombre que contenga: {proveedor}\n"

    if telefono:
        proveedores = proveedores.filter(telefono=telefono)
        mensaje_busqueda += f"Teléfono: {telefono}\n"

    if correo:
        proveedores = proveedores.filter(correo__icontains=correo)
        mensaje_busqueda += f"Correo que contenga: {correo}\n"

Empleados:
    if empleado:
        empleados = empleados.filter(empleado__icontains=empleado)
        mensaje_busqueda += f"empleados que contenga: {empleados}\n"

    if apellido:
        empleados = empleados.filter(apellido=apellido)
        mensaje_busqueda += f"apellido: {apellido}\n"

    if cargo:
        empleados = empleados.filter(cargo__icontains=cargo)
        mensaje_busqueda += f"cargo que contenga: {cargo}\n"

Pedidos:
    if pedido:
        pedidos = pedidos.filter(pedido__icontains=pedido)
        mensaje_busqueda += f"pedido que contenga: {pedido}\n"

    if fecha_pedido:
        pedidos = pedidos.filter(fecha_pedido__icontains=fecha_pedido)
        mensaje_busqueda += f"fecha_pedido: {fecha_pedido}\n"

    if total_importe:
        pedidos = pedidos.filter(total_importe__icontains=total_importe)
        mensaje_busqueda += f"total_importe que contenga: {total_importe}\n"

Piezas de Motores:
    if pieza:
        piezasmotores = piezasmotores.filter(pieza__icontains=pieza)
        mensaje_busqueda += f"pieza que contenga: {pieza}\n"

    if precio_min is not None:
        piezasmotores = piezasmotores.filter(precio__gte=precio_min)
        mensaje_busqueda += f"precio mayor o igual a: {precio_min}\n"

    if precio_max is not None:
        piezasmotores = piezasmotores.filter(precio__lte=precio_max)
        mensaje_busqueda += f"precio menor o igual a: {precio_max}\n"

Método de Pago:
    if nombre:
        metodos_pago = metodos_pago.filter(nombre__icontains=nombre)
        mensaje_busqueda += f"Nombre que contiene: {nombre}\n"

    if fecha_creacion:
        metodos_pago = metodos_pago.filter(fecha_creacion__date=fecha_creacion)
        mensaje_busqueda += f"Fecha de creación: {fecha_creacion}\n"

    if fecha_ultima_actualizacion:
        metodos_pago = metodos_pago.filter(fecha_ultima_actualizacion__date=fecha_ultima_actualizacion)
        mensaje_busqueda += f"Fecha de última actualización: {fecha_ultima_actualizacion}\n"

Funcionalidades del Menú
Administrador: todas las funcionalidades

Empleado: todas las acciones, excepto ver los datos de las nominas 

usuario: ver y buscar motores






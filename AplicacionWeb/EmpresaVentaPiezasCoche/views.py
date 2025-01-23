from django.shortcuts import render,redirect, get_object_or_404
from .models import Proveedor, Empleado, Cliente, MetodoPago, Pedido, PiezaMotor, PiezaMotor_Pedido
from django.db.models import Q, Sum
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login


# Create your views here.
def index(request):
    
    #"fecha_inicio" no existe en el objeto request.session. 
    if(not "fecha_inicio" in request.session):
        request.session["fecha_inicio"] = datetime.now().strftime('%d/%m/%Y %H:%M')
         
    return render(request, 'principal.html')


@permission_required('EmpresaVentaPiezasCoche.listar_proveedor', raise_exception=True)
def listar_proveedor(request):
    proveedor = Proveedor.objects.all()

    return render (request, 'proveedor/lista.html', {'listar_proveedor':proveedor})

@login_required
def listar_empleado(request):
    empleado = Empleado.objects.all()

    return render (request, 'empleado/lista.html', {'listar_empleado':empleado})

@login_required
def listar_clientes(request):
    cliente = Cliente.objects.select_related('empleado').all()

    return render (request, 'clientes/lista.html', {'listar_clientes':cliente})

@login_required
def listar_pedido(request):
    pedidos = Pedido.objects.select_related('cliente').all()

    return render (request, 'pedido/lista.html', {'listar_pedido':pedidos})

def listar_piezamotor(request):
    piezamotor = PiezaMotor.objects.prefetch_related('pedido','proveedor').all()

    return render (request, 'piezamotor/lista.html', {'listar_piezamotor':piezamotor})

@login_required
def listar_metodopago(request):
    metodopago = MetodoPago.objects.all()
    return render (request, 'metodopago/lista.html', {'listar_metodopago':metodopago})



#DELETE
@login_required
def eliminar_cliente(request,cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    try:
        cliente.delete()
        messages.success(request, "Se ha elimnado el usuario " + cliente.cliente +" correctamente")
    except Exception as error:
        print(error)
    
    #volvemos a la lista de clientes
    return redirect('listar_clientes')

@login_required
def eliminar_proveedor(request,proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    try:
        proveedor.delete()
        messages.success(request, "Se ha elimnado el usuario " + proveedor.proveedor +" correctamente")
    except Exception as error:
        print(error)
    
    #volvemos a la listar_proveedor
    return redirect('listar_proveedor')

@login_required
def eliminar_empleado(request,empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    try:
        empleado.delete()
        messages.success(request, "Se ha elimnado el usuario " + empleado.proveedor +" correctamente")
    except Exception as error:
        print(error)
    
    #volvemos a la lista
    return redirect('listar_empleado')

@login_required
def eliminar_pedido(request,pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    try:
        pedido.delete()
        messages.success(request, "Se ha elimnado el usuario " + pedido.proveedor +" correctamente")
    except Exception as error:
        print(error)
    
    #volvemos a la listar
    return redirect('listar_pedido')

@login_required
def eliminar_piezamotor(request,piezamotor_id):
    piezamotor = PiezaMotor.objects.get(id=piezamotor_id)
    try:
        piezamotor.delete()
        messages.success(request, "Se ha elimnado el usuario " + piezamotor.pieza +" correctamente")
    except Exception as error:
        print(error)
    
    #volvemos a la listar
    return redirect('listar_piezamotor')

@login_required
def eliminar_metodopago(request,metodopago_id):
    metodopago = MetodoPago.objects.get(id=metodopago_id)
    try:
        metodopago.delete()
        messages.success(request, "Se ha elimnado el usuario " + metodopago.nombre +" correctamente")
    except Exception as error:
        print(error)
    
    #volvemos a la listar
    return redirect('listar_metodopago')



#CREATE
@login_required
def clientes_create(request):
    if request.method == 'POST':
        form = clientesForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            messages.success(request, 'Cliente creado con éxito.')
            return redirect('listar_clientes')  # Redirige a la lista de clientes después de crear
        else:
            messages.error(request, 'Error al crear cliente: Formulario no válido.')
    else:
        form = clientesForm()  # Si la solicitud es GET, muestra el formulario vacío

    return render(request, 'clientes/clientes_form.html', {'form': form})

@login_required
def proveedor_create(request):
    if request.method == 'POST':
        form = proveedorForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            messages.success(request, 'Cliente creado con éxito.')
            return redirect('listar_clientes')  # Redirige a la lista de clientes después de crear
        else:
            messages.error(request, 'Error al crear cliente: Formulario no válido.')
    else:
        form = proveedorForm()  # Si la solicitud es GET, muestra el formulario vacío

    return render(request, 'proveedor/proveedor_form.html', {'form': form})

@login_required
def empleado_create(request):
    if request.method == 'POST':
        form = empleadoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            messages.success(request, 'empleado creado con éxito.')
            return redirect('listar_empleado') 
        else:
            messages.error(request, 'Error al crear empleado: Formulario no válido.')
    else:
        form = empleadoForm()  # Si la solicitud es GET, muestra el formulario vacío

    return render(request, 'empleado/empleado_form.html', {'form': form})

@login_required
def pedido_create(request):
    if request.method == 'POST':
        form = pedidoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la base de datos
            messages.success(request, 'pedido creado con éxito.')
            return redirect('listar_pedido') 
        else:
            messages.error(request, 'Error al crear pedido: Formulario no válido.')
    else:
        form = pedidoForm()  # Si la solicitud es GET, muestra el formulario vacío

    return render(request, 'pedido/pedido_form.html', {'form': form})

@login_required
def piezamotor_create(request):
    if request.method == 'POST':
        form = piezamotorForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'pedido creado con éxito.')
            return redirect('listar_piezamotor') 
        else:
            messages.error(request, 'Error al crear pedido: Formulario no válido.')
    else:
        form = piezamotorForm()  # Si la solicitud es GET, muestra el formulario vacío

    return render(request, 'piezamotor/piezamotor_form.html', {'form': form})

@permission_required('EmpresaVentaPiezasCoche.metodopago_create', raise_exception=True)
@login_required
def metodopago_create(request):
    if request.method == 'POST':
        form = metodo_pagoForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'metodo_pago creado con éxito.')
            return redirect('listar_metodopago') 
        else:
            messages.error(request, 'Error al crear metodo pago: Formulario no válido.')
    else:
        form = metodo_pagoForm()  # Si la solicitud es GET, muestra el formulario vacío

    return render(request, 'metodopago/metodopago_form.html', {'form': form})


#UPDATE
@login_required
def clientes_update(request, cliente_id):
    #obtenemos el registro del cliente que se pasa por parametro
    cliente = Cliente.objects.get(id=cliente_id)
    
    #Esta variable se usará para almacenar los datos del formulario si la solicitud es POST
    datosFormulario = None
    
    #Comprueba si la solicitud es de tipo POST (cuando se envía un formulario). 
    if request.method == "POST":
        #almacena los datos del formulario en datosFormulario
        datosFormulario = request.POST

    """
    Crea una instancia del formulario clientesForm. Si datosFormulario tiene datos 
    (es decir, si es una solicitud POST), el formulario se llena con esos datos. Además, 
    se pasa la instancia del libro para que el formulario sepa que está actualizando ese libro específico.
    """
    form = clientesForm(datosFormulario, instance= cliente)

    """
    

    Si hay un error al guardar, lo imprime en la consola.
    """
    
    if (request.method == "POST"): #Comprueba nuevamente si el método de la solicitud es POST.
        if form.is_valid(): #Si el formulario es válido (formulario.is_valid()), intenta guardar los cambios.
            try:
                # Guardamos los cambios del formulario
                form.save()
                
                #Si el guardado es exitoso, muestra un mensaje de éxito y redirige a la lista de libros.
                messages.success(request, f"Se ha actualizado el cliente {form.cleaned_data.get('cliente')} correctamente")
                
                # Redirigimos al usuario a la lista de usuarios
                return redirect('listar_clientes')
            
            except Exception as error:
                print(error)  
        else:
            print("Errores del formulario:", form.errors)

    # Renderizamos el formulario en caso de GET o si el formulario no es válido
    return render(request, 'clientes/actualizar_cliente.html', {'form': form, 'cliente': cliente})


@login_required
def proveedor_update(request, proveedor_id):
    
    proveedor = Proveedor.objects.get(id=proveedor_id)
    
    datosFormulario = None
    
    #Comprueba si la solicitud es de tipo POST (cuando se envía un formulario). 
    if request.method == "POST":
        #almacena los datos del formulario en datosFormulario
        datosFormulario = request.POST


    form = proveedorForm(datosFormulario, instance= proveedor)

    
    if (request.method == "POST"): #Comprueba nuevamente si el método de la solicitud es POST.
        if form.is_valid(): #Si el formulario es válido (formulario.is_valid()), intenta guardar los cambios.
            try:
                # Guardamos los cambios del formulario
                form.save()
                
                #Si el guardado es exitoso, muestra un mensaje de éxito y redirige a la lista de libros.
                messages.success(request, f"Se ha actualizado el proveedor {form.cleaned_data.get('proveedor')} correctamente")
                
                
                return redirect('listar_proveedor')
            
            except Exception as error:
                print(error)  
        else:
            print("Errores del formulario:", form.errors)

    return render(request, 'proveedor/actualizar_proveedor.html', {'form': form, 'proveedor': proveedor})

@login_required
def empleado_update(request, empleado_id):
    
    empleado = Empleado.objects.get(id=empleado_id)
    
    datosFormulario = None
    
    if request.method == "POST":
        #almacena los datos del formulario en datosFormulario
        datosFormulario = request.POST


    form = empleadoForm(datosFormulario, instance= empleado)

    
    if (request.method == "POST"): #Comprueba nuevamente si el método de la solicitud es POST.
        if form.is_valid(): #Si el formulario es válido (formulario.is_valid()), intenta guardar los cambios.
            try:
                # Guardamos los cambios del formulario
                form.save()
                
                #Si el guardado es exitoso, muestra un mensaje de éxito y redirige a la lista de libros.
                messages.success(request, f"Se ha actualizado el proveedor {form.cleaned_data.get('empleado')} correctamente")
                
                
                return redirect('listar_empleado')
            
            except Exception as error:
                print(error)  
        else:
            print("Errores del formulario:", form.errors)

    return render(request, 'empleado/actualizar_empleado.html', {'form': form, 'empleado': empleado})

@login_required
def pedido_update(request, pedido_id):
    
    pedido = Pedido.objects.get(id=pedido_id)
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST


    form = pedidoForm(datosFormulario, instance= pedido)

    
    if (request.method == "POST"):
        if form.is_valid(): 
            try:
                form.save()                
                messages.success(request, f"Se ha actualizado el pedido {form.cleaned_data.get('pedido')} correctamente")
                 
                return redirect('listar_pedido')
            
            except Exception as error:
                print(error)  
        else:
            print("Errores del formulario:", form.errors)

    return render(request, 'pedido/actualizar_pedido.html', {'form': form, 'pedido': pedido})

@login_required
def piezamotor_update(request, piezamotor_id):
    
    piezamotor = PiezaMotor.objects.get(id=piezamotor_id)
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST


    form = piezamotorForm(datosFormulario, instance= piezamotor)

    
    if (request.method == "POST"):
        if form.is_valid(): 
            try:
                form.save()                
                messages.success(request, f"Se ha actualizado el pedido {form.cleaned_data.get('piezamotor')} correctamente")
                 
                return redirect('listar_piezamotor')
            
            except Exception as error:
                print(error)  
        else:
            print("Errores del formulario:", form.errors)

    return render(request, 'piezamotor/actualizar_piezamotor.html', {'form': form, 'piezamotor': piezamotor})

@login_required
def metodopago_update(request, metodopago_id):
    
    metodo_pago = MetodoPago.objects.get(id=metodopago_id)
    
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST


    form = metodo_pagoForm(datosFormulario, instance= metodo_pago)

    
    if (request.method == "POST"):
        if form.is_valid(): 
            try:
                form.save()                
                messages.success(request, f"Se ha actualizado el metodo de pago {form.cleaned_data.get('metodo_pago')} correctamente")
                 
                return redirect('listar_metodopago')
            
            except Exception as error:
                print(error)  
        else:
            print("Errores del formulario:", form.errors)

    return render(request, 'metodopago/actualizar_metodopago.html', {'form': form, 'metodo_pago': metodo_pago})


#read clientes_busqueda
@login_required
def clientes_busqueda(request):
    # Si se ha enviado el formulario (request.GET contiene datos)
    if request.GET:
        formulario = BusquedaClienteForm(request.GET)

        if formulario.is_valid():
            mensaje_busqueda = "Se ha buscado por los siguientes filtros:\n"
            clientes = Cliente.objects.all()  # Empezamos con todos los Cliente

            # Obtenemos los valores de los campos filtrados
            cliente = formulario.cleaned_data.get('cliente')
            apellido = formulario.cleaned_data.get('apellido')
            correo = formulario.cleaned_data.get('correo')
            tipo_clientes = formulario.cleaned_data.get('tipo_clientes')
            direccion = formulario.cleaned_data.get('direccion')
            empleado = formulario.cleaned_data.get('empleado')


            # Filtro por nombre del cliente
            if cliente:
                clientes = clientes.filter(cliente__icontains=cliente)
                mensaje_busqueda += f"Nombre que contenga: {cliente}\n"

            # Filtro por apellido
            if apellido:
                clientes = clientes.filter(apellido__icontains=apellido)
                mensaje_busqueda += f"Apellido que contenga: {apellido}\n"

            # Filtro por correo
            if correo:
                clientes = clientes.filter(correo__icontains=correo)
                mensaje_busqueda += f"Correo que contenga: {correo}\n"

            # Filtro por tipo de cliente (Particular o Empresa)
            if tipo_clientes:
                clientes = clientes.filter(tipo_clientes=tipo_clientes)
                mensaje_busqueda += f"Tipo de cliente: {tipo_clientes}\n"

            # Filtro por dirección
            if direccion:
                clientes = clientes.filter(direccion__icontains=direccion)
                mensaje_busqueda += f"Dirección que contenga: {direccion}\n"

            # Filtro por empleado
            if empleado:
                clientes = clientes.filter(empleado__empleado__icontains=empleado) 
                mensaje_busqueda += f"Empleado que contenga: {empleado}\n"



            # Pasamos los clientes filtrados y el mensaje a la plantilla
            return render(request, 'clientes/lista.html', {
                'listar_clientes': clientes,
                'mensaje_busqueda': mensaje_busqueda
            })
    else:
        formulario = BusquedaClienteForm()

    return render(request, 'clientes/clientes_busqueda.html', {'formulario': formulario})



@login_required
def proveedor_busqueda(request):
    if request.GET:
        formulario = BusquedaProveedorForm(request.GET)

        if formulario.is_valid():
            mensaje_busqueda = "Se ha buscado por los siguientes filtros:\n"
            proveedores = Proveedor.objects.all()  # Empezamos con todos los Cliente

            proveedor = formulario.cleaned_data.get('proveedor')
            telefono = formulario.cleaned_data.get('telefono')
            correo = formulario.cleaned_data.get('correo')



            if proveedor:
                proveedores = proveedores.filter(proveedor__icontains=proveedor)
                mensaje_busqueda += f"Nombre que contenga: {proveedor}\n"

            
            if telefono:
                proveedores = proveedores.filter(telefono=telefono)
                mensaje_busqueda += f"Teléfono: {telefono}\n"



            # Filtro por correo
            if correo:
                proveedores = proveedores.filter(correo__icontains=correo)
                mensaje_busqueda += f"Correo que contenga: {correo}\n"

            
            return render(request, 'proveedor/lista.html', {
                'listar_proveedor': proveedores,
                'mensaje_busqueda': mensaje_busqueda
            })
    else:
        formulario = BusquedaProveedorForm()

    return render(request, 'proveedor/proveedor_busqueda.html', {'formulario': formulario})

@login_required
def empleado_busqueda(request):
    if request.GET:
        formulario = BusquedaEmpleadoForm(request.GET)

        if formulario.is_valid():
            mensaje_busqueda = "Se ha buscado por los siguientes filtros:\n"
            empleados = Empleado.objects.all()  

            empleado = formulario.cleaned_data.get('empleado')
            apellido = formulario.cleaned_data.get('apellido')
            cargo = formulario.cleaned_data.get('cargo')



            if empleado:
                empleados = empleados.filter(empleado__icontains=empleado)
                mensaje_busqueda += f"empleados que contenga: {empleados}\n"

            
            if apellido:
                empleados = empleados.filter(apellido__icontains=apellido)
                mensaje_busqueda += f"apellido: {apellido}\n"

            if cargo:
                empleados = empleados.filter(cargo__icontains=cargo)
                mensaje_busqueda += f"cargo que contenga: {cargo}\n"

            
            return render(request, 'empleado/lista.html', {
                'listar_empleado': empleados,
                'mensaje_busqueda': mensaje_busqueda
            })
    else:
        formulario = BusquedaEmpleadoForm()

    return render(request, 'empleado/empleado_busqueda.html', {'formulario': formulario})

@login_required
def pedido_busqueda(request):
    if request.GET:
        formulario = BusquedaPedidoForm(request.GET)

        if formulario.is_valid():
            mensaje_busqueda = "Se ha buscado por los siguientes filtros:\n"
            pedidos = Pedido.objects.all()  

            pedido = formulario.cleaned_data.get('pedido')
            fecha_pedido = formulario.cleaned_data.get('fecha_pedido')
            total_importe = formulario.cleaned_data.get('total_importe')



            if pedido:
                pedidos = pedidos.filter(pedido__icontains=pedido)
                mensaje_busqueda += f"pedido que contenga: {pedido}\n"

            
            if fecha_pedido:
                pedidos = pedidos.filter(fecha_pedido__icontains=fecha_pedido)
                mensaje_busqueda += f"fecha_pedido: {fecha_pedido}\n"

            if total_importe:
                pedidos = pedidos.filter(total_importe__icontains=total_importe)
                mensaje_busqueda += f"total_importe que contenga: {total_importe}\n"

            
            return render(request, 'pedido/lista.html', {
                'listar_pedido': pedidos,
                'mensaje_busqueda': mensaje_busqueda
            })
    else:
        formulario = BusquedaPedidoForm()

    return render(request, 'pedido/pedido_busqueda.html', {'formulario': formulario})


def piezamotor_busqueda(request):
    if request.GET:
        formulario = BusquedaPiezaMotorForm(request.GET)

        if formulario.is_valid():
            mensaje_busqueda = "Se ha buscado por los siguientes filtros:\n"
            piezasmotores = PiezaMotor.objects.all()  

            pieza = formulario.cleaned_data.get('pieza')
            precio_min = formulario.cleaned_data.get('precio_min')
            precio_max = formulario.cleaned_data.get('precio_max')


            if pieza:
                piezasmotores = piezasmotores.filter(pieza__icontains=pieza)
                mensaje_busqueda += f"pieza que contenga: {pieza}\n"

            # Filtro por precio mínimo
            if precio_min is not None:
                piezasmotores = piezasmotores.filter(precio__gte=precio_min)
                mensaje_busqueda += f"precio mayor o igual a: {precio_min}\n"

            # Filtro por precio máximo
            if precio_max is not None:
                piezasmotores = piezasmotores.filter(precio__lte=precio_max)
                mensaje_busqueda += f"precio menor o igual a: {precio_max}\n"


            return render(request, 'piezamotor/lista.html', {
                'listar_piezamotor': piezasmotores,
                'mensaje_busqueda': mensaje_busqueda
            })
    else:
        formulario = BusquedaPiezaMotorForm()

    return render(request, 'piezamotor/piezamotor_busqueda.html', {'formulario': formulario})

@login_required
def metodopago_busqueda(request):
    if request.GET:  
        formulario = BusquedaMetodoPagoForm(request.GET)

        if formulario.is_valid():
            mensaje_busqueda = "Se ha buscado por los siguientes filtros:\n"
            metodos_pago = MetodoPago.objects.all()

            
            nombre = formulario.cleaned_data.get('nombre')
            fecha_creacion = formulario.cleaned_data.get('fecha_creacion')
            fecha_ultima_actualizacion = formulario.cleaned_data.get('fecha_ultima_actualizacion')

           
            if nombre:
                metodos_pago = metodos_pago.filter(nombre__icontains=nombre)
                mensaje_busqueda += f"Nombre que contiene: {nombre}\n"

            
            if fecha_creacion:
                metodos_pago = metodos_pago.filter(fecha_creacion__date=fecha_creacion)
                mensaje_busqueda += f"Fecha de creación: {fecha_creacion}\n"

          
            if fecha_ultima_actualizacion:
                metodos_pago = metodos_pago.filter(fecha_ultima_actualizacion__date=fecha_ultima_actualizacion)
                mensaje_busqueda += f"Fecha de última actualización: {fecha_ultima_actualizacion}\n"

            return render(request, 'metodopago/lista.html', {
                'listar_metodopago': metodos_pago,
                'mensaje_busqueda': mensaje_busqueda
            })
    else:
        formulario = BusquedaMetodoPagoForm()

    return render(request, 'metodopago/metodo_pago_busqueda.html', {'formulario': formulario})

#sesiones
def registrar_usuario(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            rol = str(formulario.cleaned_data.get('rol'))
            
            if(rol == Usuario.CLIENTE):
                grupo = Group.objects.get(name='Clientes')
                grupo.user_set.add(user)
                cliente = Cliente.objects.create(usuario = user)
                cliente.save()
                
            elif(rol == Usuario.EMPLEADO):
                grupo = Group.objects.get(name='Empleado')
                grupo.user_set.add(user)
                empleado = Empleado.objects.create(usuario = user)
                empleado.save()
                

            login(request, user)
            return redirect('index')
    else:
        formulario = RegistroForm()
    return render(request, 'registration/signup.html', {'formulario': formulario})
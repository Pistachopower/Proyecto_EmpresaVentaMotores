
from django import forms
from .models import *
from datetime import date, datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required

class clientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cliente', 'apellido', 'correo', 'tipo_clientes', 'direccion','empleado']
        help_texts = {
            "cliente": "200 caracteres como máximo",
        }
        
    def clean(self):
        super().clean()
        
        cliente = self.cleaned_data.get('cliente')
        apellido = self.cleaned_data.get('apellido')
        correo = self.cleaned_data.get('correo')
        tipo_clientes = self.cleaned_data.get('tipo_clientes')
        direccion = self.cleaned_data.get('direccion')
        empleado = self.cleaned_data.get('empleado')
        
        destinoCliente = Cliente.objects.filter(cliente=cliente).first()
        if destinoCliente is not None:
            if self.instance is not None and destinoCliente.id == self.instance.id:
                pass
            else:
                self.add_error('cliente', 'Ya existe un cliente con ese nombre')
        
        if len(apellido) < 2:
            self.add_error('apellido', 'Al menos debes indicar 3 caracteres')
        
        if "@" not in correo or "." not in correo:
            self.add_error('correo', 'Por favor, introduce un correo válido.')
        
        return self.cleaned_data

class proveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['proveedor', 'telefono', 'correo', 'direccion']
        help_texts = {
            "proveedor": "200 caracteres como máximo",
        }

    def clean(self):
        super().clean()
        
        proveedor = self.cleaned_data.get('proveedor')
        telefono = self.cleaned_data.get('telefono')
        correo = self.cleaned_data.get('correo')
        tipo_clientes = self.cleaned_data.get('tipo_clientes')
        direccion = self.cleaned_data.get('direccion')
        
        destinoProveedor = Proveedor.objects.filter(proveedor=proveedor).first()
        if destinoProveedor is not None:
            if self.instance is not None and destinoProveedor.id == self.instance.id:
                pass
            else:
                self.add_error('proveedor', 'Ya existe un cliente con ese nombre')
        
        if len(proveedor) < 2:
            self.add_error('proveedor', 'Al menos debes indicar 3 caracteres')
            
        if len(telefono) < 8:
            self.add_error('telefono', 'Al menos debes colocar 8 caracteres')
        
        if "@" not in correo or "." not in correo:
            self.add_error('correo', 'Por favor, introduce un correo válido.')
            
        
        return self.cleaned_data        
  

class empleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['empleado', 'apellido', 'cargo', 'fecha_contratacion']
        help_texts = {
            "empleado": "200 caracteres como máximo",
        }
        widgets = {
            "fecha_contratacion":forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        }

    def clean(self):
        super().clean()
        
        empleado = self.cleaned_data.get('empleado')
        apellido = self.cleaned_data.get('apellido')
        cargo = self.cleaned_data.get('cargo')
        fecha_contratacion = self.cleaned_data.get('fecha_contratacion')
        
        destinoEmpleado = Empleado.objects.filter(empleado=empleado).first()
        if destinoEmpleado is not None:
            if self.instance is not None and destinoEmpleado.id == self.instance.id:
                pass
            else:
                self.add_error('empleado', 'Ya existe un cliente con ese nombre')
        
        if len(empleado) < 2:
            self.add_error('empleado', 'Al menos debes indicar 3 caracteres')
            
        if len(apellido) < 1:
            self.add_error('apellido', 'Al menos debes colocar 8 caracteres')
        

            
        #Comprobamos que la fecha de publicación sea mayor que hoy
        fechaHoy = date.today()
        if fechaHoy > fecha_contratacion:
            self.add_error('fecha_contratacion','La fecha de registro debe ser igual o mayor a Hoy')
            
        
        return self.cleaned_data   





class pedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['pedido', 'fecha_pedido', 'total_importe', 'estado', 'metodo_pago', 'cliente']
        help_texts = {
            "empleado": "100 caracteres como máximo",
        }
        widgets = {
            "fecha_pedido":forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        }

    def clean(self):
        super().clean()
        
        pedido = self.cleaned_data.get('pedido')
        fecha_pedido = self.cleaned_data.get('fecha_pedido')
        total_importe = self.cleaned_data.get('total_importe')
        estado = self.cleaned_data.get('estado')
        metodo_pago = self.cleaned_data.get('metodo_pago')
        cliente = self.cleaned_data.get('cliente')

        
        destinoPedido = Pedido.objects.filter(pedido=pedido).first()
        if destinoPedido is not None:
            if self.instance is not None and destinoPedido.id == self.instance.id:
                pass
            else:
                self.add_error('pedido', 'Ya existe un pedido con ese nombre')
        
        if len(pedido) < 0:
            self.add_error('pedido', 'El nombre del pedido debe tener al menos 1 caracteres')
        
            
        if total_importe < 0:
            self.add_error('total_importe', 'El importe total debe ser mayor que 0')

        
        # Validación de que la fecha de pedido no sea en el pasado
        fechaHoy = date.today()
        if fecha_pedido < fechaHoy:
            self.add_error('fecha_pedido', 'La fecha del pedido debe ser igual o mayor a hoy')

        return self.cleaned_data
            
      
class piezamotorForm(forms.ModelForm):
    class Meta:
        model = PiezaMotor
        fields = ['pieza', 'proveedor', 'pedido', 'precio', 'descripcion', 'stock_disponible']
        help_texts = {
            "pieza": "100 caracteres como máximo",
        }


    def clean(self):
        super().clean()
        
        pieza = self.cleaned_data.get('pieza')
        proveedor = self.cleaned_data.get('proveedor')
        pedido = self.cleaned_data.get('pedido')
        precio = self.cleaned_data.get('precio')
        descripcion = self.cleaned_data.get('descripcion')
        stock_disponible = self.cleaned_data.get('stock_disponible')

        
        destinopiezamotor = PiezaMotor.objects.filter(pieza=pieza).first()
        if destinopiezamotor is not None:
            if self.instance is not None and destinopiezamotor.id == self.instance.id:
                pass
            else:
                self.add_error('pieza', 'Ya existe un pieza con ese nombre')
        
        if len(pieza) < 0:
            self.add_error('pieza', 'El nombre de la pieza debe tener al menos 1 caracteres')
            
        return self.cleaned_data
    
    

class metodo_pagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['metodo_pago', 'nombre', 'tipo_pago', 'fecha_creacion', 'pagado']
        help_texts = {
            "metodo_pago": "100 caracteres como máximo",
        }
        widgets = {
            "fecha_creacion":forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),

        }


    def clean(self):
        super().clean()
        
        metodo_pago = self.cleaned_data.get('metodo_pago')
        nombre = self.cleaned_data.get('nombre')
        tipo_pago = self.cleaned_data.get('tipo_pago')
        fecha_creacion = self.cleaned_data.get('fecha_creacion')
        pagado = self.cleaned_data.get('pagado')

        
        destinoMetodo_pago = MetodoPago.objects.filter(metodo_pago=metodo_pago).first()
        if destinoMetodo_pago is not None:
            if self.instance is not None and destinoMetodo_pago.id == self.instance.id:
                pass
            else:
                self.add_error('metodo_pago', 'Ya existe un metodo_pago con ese nombre')
        
        if len(nombre) < 0:
            self.add_error('nombre', 'El nombre de la pieza debe tener al menos 1 caracteres')
            
        # Debemos hacer un casteo porque fechaHoy y fecha_creacion son tipos de datos diferentes
        # Usamos la zona horaria actual para la fecha de hoy (conscientes de la zona horaria)
        fechaHoy = date.today()  # Solo la fecha (sin hora)

        # Convertirmos la fecha_creacion a solo la parte de la fecha (sin la hora)
        fecha_creacion_date = fecha_creacion.date()  # Convertirmos a 'date' para comparar solo la parte de la fecha

        # Validamos que la fecha_creacion no sea menor que la fecha actual
        if fecha_creacion_date < fechaHoy:
            self.add_error('fecha_creacion', 'La fecha de creación no puede ser anterior a hoy')
            
        return self.cleaned_data
    
    
    
#read
class BusquedaClienteForm(forms.Form):
    # Campo de búsqueda por nombre del cliente
    cliente = forms.CharField(required=False, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce nombre cliente'}))    
    # Campo de búsqueda por apellido del cliente
    apellido = forms.CharField(required=False, label="Apellido")

    # Campo de búsqueda por correo electrónico
    correo = forms.EmailField(required=False, label="Correo Electrónico")

    # Campo para tipo de cliente (Particular o Empresa)
    tipo_clientes = forms.ChoiceField(choices=[('', 'Elige un tipo'), ('P', 'Particular'), ('E', 'Empresa')], required=False, label="Tipo de Cliente")

    # Campo para búsqueda por dirección
    direccion = forms.CharField(required=False, label="Dirección")

    # Campo para filtrar por empleado (relacionado con otro modelo "Empleado")
    empleado = forms.CharField(required=False, label="Empleado")



    def clean(self):
        # Llamamos al método clean de la clase base para validar el formulario
        cleaned_data = super().clean()

        # Obtenemos los valores de los campos
        cliente = cleaned_data.get('cliente')
        apellido = cleaned_data.get('apellido')
        correo = cleaned_data.get('correo')
        tipo_clientes = cleaned_data.get('tipo_clientes')
        direccion = cleaned_data.get('direccion')
        empleado = cleaned_data.get('empleado')


        # Verificamos que al menos un campo tenga un valor (si ninguno tiene informacion muestra mensaje de error)
        if not cliente and not apellido and not correo and not tipo_clientes and not direccion and not empleado:
            
            self.add_error('cliente', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('apellido', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('correo', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('tipo_clientes', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('direccion', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('empleado', 'Debe introducir al menos un valor en un campo del formulario')

        if correo and "@" not in correo:
            self.add_error('correo', 'El correo debe ser válido')

        return cleaned_data
    
    

class BusquedaProveedorForm(forms.Form):
    proveedor = forms.CharField(required=False, label="Nombre del proveedor", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el nombre del proveedor'}))
    
    telefono = forms.CharField(required=False, label="Teléfono", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el teléfono'}))
    
    correo = forms.EmailField(required=False, label="Correo Electrónico", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el correo electrónico'}))
    
    def clean(self):
        cleaned_data = super().clean()

        proveedor = cleaned_data.get('proveedor')
        telefono = cleaned_data.get('telefono')
        correo = cleaned_data.get('correo')


        if not proveedor and not telefono and not correo:
            self.add_error('proveedor', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('telefono', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('correo', 'Debe introducir al menos un valor en un campo del formulario')

        # Validamos el correo si se ha ingresado
        if correo and "@" not in correo:
            self.add_error('correo', 'El correo debe ser válido')

        return cleaned_data

class BusquedaEmpleadoForm(forms.Form):
    empleado = forms.CharField(required=False, label="Nombre del empleado", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el nombre del empleado'}))
    
    apellido = forms.CharField(required=False, label="apellido", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el apellido'}))
    
    cargo = forms.CharField(required=False, label="cargo")
    
    def clean(self):
        cleaned_data = super().clean()

        empleado = cleaned_data.get('empleado')
        apellido = cleaned_data.get('apellido')
        cargo = cleaned_data.get('cargo')


        if not empleado and not apellido and not cargo:
            self.add_error('empleado', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('apellido', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('cargo', 'Debe introducir al menos un valor en un campo del formulario')

        if empleado and len(empleado) < 3:
                self.add_error('empleado', 'El empleado debe tener al menos 3 caracteres')

        return cleaned_data
    
class BusquedaPedidoForm(forms.Form):
    pedido = forms.CharField(required=False, label="Nombre del pedido", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el nombre del pedido'}))
    
    fecha_pedido = forms.DateField(required=False, label="fecha_pedido", widget=forms.DateInput(attrs={'type': 'date'}))
    
    total_importe = forms.IntegerField(required=False, label="total_importe")
    
    def clean(self):
        cleaned_data = super().clean()

        pedido = cleaned_data.get('pedido')
        fecha_pedido = cleaned_data.get('fecha_pedido')
        total_importe = cleaned_data.get('total_importe')


        if not pedido and not fecha_pedido and not total_importe:
            self.add_error('pedido', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('fecha_pedido', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('total_importe', 'Debe introducir al menos un valor en un campo del formulario')


        return cleaned_data
    
class BusquedaPiezaMotorForm(forms.Form):
    pieza= forms.CharField(required=False, label="Nombre del pieza", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduce el nombre del pieza'}))
    
    
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

    
    def clean(self):
        cleaned_data = super().clean()

        pieza = cleaned_data.get('pieza')
        precio_min = cleaned_data.get('precio_min')
        precio_max = cleaned_data.get('precio_max')


        if not pieza and not precio_min and not precio_max:
            self.add_error('pieza', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('precio_min', 'Debe introducir al menos un valor en un campo del formulario')
            self.add_error('precio_max', 'Debe introducir al menos un valor en un campo del formulario')
           
        return cleaned_data
    

class BusquedaMetodoPagoForm(forms.Form):
    nombre = forms.CharField(
        required=False,
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Introduce el nombre del método de pago'
        })
    )
    
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

    
    def clean(self):
        cleaned_data = super().clean()

        nombre = cleaned_data.get('nombre')
        fecha_creacion = cleaned_data.get('fecha_creacion')
        fecha_ultima_actualizacion = cleaned_data.get('fecha_ultima_actualizacion')

        if not nombre and not fecha_creacion and not fecha_ultima_actualizacion:
            raise forms.ValidationError("Debe proporcionar al menos un campo para realizar la búsqueda.")

        return cleaned_data
    
    #Sesiones 
    
    
class RegistroForm(UserCreationForm):
    roles = (
            ("", "NINGUNO"),
            (Usuario.CLIENTE, 'cliente'),
            (Usuario.EMPLEADO, 'empleado'),
        )

    role = forms.ChoiceField(choices=roles)

    class Meta:
        model = Usuario
        fields = ('nombre', 'username', 'correo', 'telefono', 'password1', 'password2', 'rol')
    





from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser #agregamos estos para la autenticacion


class Usuario(AbstractUser):
    #clave-valor: 
    #abajo están los usuarios que vamos a crear
    ADMINISTRADOR = 1
    EMPLEADO = 2
    CLIENTE = 3
    ROLES = [
        (ADMINISTRADOR, 'administrador'),
        (EMPLEADO, 'empleado'),
        (CLIENTE, 'cliente'),
    ]
   
    rol = models.PositiveSmallIntegerField(choices=ROLES, default=1)

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    correo = models.EmailField(unique=True, max_length=254)


#tablas independientes
#empleado hereda de usuario
class Empleado(models.Model):
    empleadoUsuario= models.OneToOneField(Usuario, on_delete=models.CASCADE)
    empleado = models.CharField(max_length=100)
    apellido = models.TextField()
    cargo = models.CharField(max_length=100)
    fecha_contratacion = models.DateField(null=True, blank=True) #Fecha de contratación 

    def __str__(self):
        return f"{self.empleado} {self.apellido}" 

class Proveedor(models.Model):
    proveedor = models.CharField(max_length=100) #los id se ponen a 100 porque puede incrementar los registros
    telefono = models.TextField()
    correo = models.CharField(max_length=100, unique=True) #Texto y  único
    direccion = models.TextField()

    def __str__(self):
        return self.proveedor
    
#cliente hereda de usuario
class Cliente(models.Model):
    clienteUsuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='clienteUsuario')
    TIPO_CLIENTES = [('P', 'Particular'), ('E', 'Empresa')]
    cliente = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, unique=True)
    tipo_clientes = models.CharField(max_length=2, choices=TIPO_CLIENTES)
    direccion = models.TextField(null=True, blank=True) #puede existir registos de clientes sin correo
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente} {self.apellido}"



class MetodoPago(models.Model):
    metodo_pago = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    tipo_pago = models.CharField(max_length=100)
    
    #los atributos fecha_Creacion y fecha_Ultima_Actualizacion  hacen referencia 
    #a registrar cuándo se creo y se actualizó cada metodo de pago
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_ultima_actualizacion = models.DateTimeField(auto_now=True) #se usa este parametro para poder manejar la fecha exacta de que se actualizó algún campo en el modelo MetodoPago
    #nuevo atributo
    pagado = models.CharField(max_length=100) # Valor por defecto si no se proporciona)
 
    def __str__(self):
        return self.metodo_pago


class Pedido(models.Model):
    ESTADO = [('P', 'Pendiente'), ('ENV', 'Enviado'), ('ENTR', 'Entregado')]

    pedido = models.CharField(max_length=100)
    fecha_pedido = models.DateField()
    total_importe = models.IntegerField()
    estado = models.CharField(max_length=4, choices=ESTADO)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    
    #related_name='pedido_cliente': se crea una relacion inversa entre cliente y pedido. Tambiens e usa para poder obtener los todos los pedidos de un cliente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedido_cliente')

     #relacion pedido con usuario: Many to one: un usuario puede hacer varios pedidos
     # pero un pedido solo puede ser de un usuario
    usuario_Pedido= models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.pedido

#tabla intermedia 
class PiezaMotor(models.Model):
    pieza = models.CharField(max_length=100)
    proveedor = models.ManyToManyField(Proveedor)
    pedido = models.ManyToManyField(Pedido, through='PiezaMotor_Pedido') #tabla intermedia entre pedido y piezaMotor
    precio = models.DecimalField(max_digits=10, decimal_places=2) #se permite 10 digitos en total de los cuales 2 pueden esta en el punto decimal
    descripcion = models.TextField()
    stock_disponible = models.IntegerField(null=True, blank=True) #se permite que este campo este vacio

    def __str__(self):
        return self.pieza

#tabla intermedia
class PiezaMotor_Pedido(models.Model):
    pieza = models.ForeignKey(PiezaMotor, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True, blank=True) #se pone estos parametros para evitar el el error que no pueda ser nulo el valor
    precioTotal = models.FloatField(default=0.0) #se agrega este parametros para evitar error: Internal error: NOT NULL constraint failed












from django.contrib import admin
from .models import Proveedor, Empleado, Cliente, MetodoPago, Pedido, PiezaMotor, PiezaMotor_Pedido, Usuario

admin.site.register(Proveedor)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(MetodoPago)
admin.site.register(Pedido)
admin.site.register(PiezaMotor)
admin.site.register(PiezaMotor_Pedido)
admin.site.register(Usuario)

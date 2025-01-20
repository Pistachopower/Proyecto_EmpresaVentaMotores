from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#recuperacion passw
from django.urls import path 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/listar', views.listar_clientes, name='listar_clientes'),
    path('proveedor/listar', views.listar_proveedor, name='listar_proveedor'),
    path('empleado/listar', views.listar_empleado, name='listar_empleado'),
    path('pedido/listar', views.listar_pedido, name='listar_pedido'),
    path('piezamotor/listar', views.listar_piezamotor, name='listar_piezamotor'),
    path('metodopago/listar', views.listar_metodopago, name='listar_metodopago'),
    
    #delete
    path('clientes/eliminar/<int:cliente_id>', views.eliminar_cliente, name='eliminar_cliente'),
    path('proveedor/eliminar/<int:proveedor_id>', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('empleado/eliminar/<int:empleado_id>', views.eliminar_empleado, name='eliminar_empleado'),
    path('pedido/eliminar/<int:pedido_id>', views.eliminar_pedido, name='eliminar_pedido'),
    path('piezamotor/eliminar/<int:piezamotor_id>', views.eliminar_piezamotor, name='eliminar_piezamotor'),
    path('metodopago/eliminar/<int:metodopago_id>', views.eliminar_metodopago, name='eliminar_metodopago'),
    
    #create
    path('clientes/crear/', views.clientes_create, name='clientes_create'),
    path('proveedor/crear/', views.proveedor_create, name='proveedor_create'),
    path('empleado/crear/', views.empleado_create, name='empleado_create'),
    path('pedido/crear/', views.pedido_create, name='pedido_create'),
    path('piezamotor/crear/', views.piezamotor_create, name='piezamotor_create'),
    path('metodopago/crear/', views.metodopago_create, name='metodopago_create'),


    
    
    #update
    path('clientes/editar/<int:cliente_id>', views.clientes_update, name='clientes_update'),
    path('proveedor/editar/<int:proveedor_id>', views.proveedor_update, name='proveedor_update'),
    path('empleado/editar/<int:empleado_id>', views.empleado_update, name='empleado_update'),
    path('pedido/editar/<int:pedido_id>', views.pedido_update, name='pedido_update'),
    path('piezamotor/editar/<int:piezamotor_id>', views.piezamotor_update, name='piezamotor_update'),
    path('metodopago/editar/<int:metodopago_id>', views.metodopago_update, name='metodopago_update'),
         
    #read 
    path('clientes/busqueda-avanzada/', views.clientes_busqueda, name='clientes_busqueda'),
    path('proveedor/busqueda-avanzada/', views.proveedor_busqueda, name='proveedor_busqueda'),
    path('empleado/busqueda-avanzada/', views.empleado_busqueda, name='empleado_busqueda'),
    path('pedido/busqueda-avanzada/', views.pedido_busqueda, name='pedido_busqueda'),
    path('piezamotor/busqueda-avanzada/', views.piezamotor_busqueda, name='piezamotor_busqueda'),
    path('metodopago/busqueda-avanzada/', views.metodopago_busqueda, name='metodopago_busqueda'),


    #sesiones
    path('registrar',views.registrar_usuario,name='registrar_usuario'),
    
    

    # Ruta para solicitar el restablecimiento de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name='password_reset'),
    
    # Ruta para notificar que se ha enviado el correo
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    
    # Ruta para ingresar la nueva contraseña (incluye el token)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    
    # Ruta para notificar que la contraseña se ha cambiado correctamente
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),


]
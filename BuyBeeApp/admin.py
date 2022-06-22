from django.contrib import admin

from BuyBeeApp.models import Categoria, DetallePedido, Envio, EstadoEnvio, EstadoPedido, ProductoImagen, ProductoVenta, Usuario, Pedido

# Register your models here.
class admUsuario(admin.ModelAdmin):
    list_display=["rut", "nombres", "apellidos", "email", "numero", "foto_perfil", "suscrito"]
    list_editable=["nombres", "apellidos", "email", "numero", "foto_perfil", "suscrito"]
    
    class Meta:
        model= Usuario

class admProductoVenta(admin.ModelAdmin):
    list_display=["vendedor", "categoria", "id", "nombre", "descripcion", "precio", "stock",
                "fecha_publicacion", "vistas", "compras"]
    list_editable=["categoria", "nombre", "descripcion", "precio", "stock"]
    
    class Meta:
        model= ProductoVenta

class admProductoImagen(admin.ModelAdmin):
    list_display=["id", "imagen"]
    list_editable=["imagen"]
    
    class Meta:
        model= ProductoImagen

class admCategoria(admin.ModelAdmin):
    list_display=["id", "nombre"]
    list_editable=["nombre"]
    
    class Meta:
        model= Categoria

class admPedido(admin.ModelAdmin):
    list_display=["comprador", "estado", "id", "fecha", "total"]
    list_editable=["estado", "total"]
    
    class Meta:
        model= Pedido

class admEstadoPedido(admin.ModelAdmin):
    list_display=["id", "nombre"]
    list_editable=["nombre"]
    
    class Meta:
        model= EstadoPedido

class admDetallePedido(admin.ModelAdmin):
    list_display=["id", "cantidad", "subtotal", "pedido_id"]
    list_editable=["cantidad", "subtotal"]

    class Meta:
        model= DetallePedido

class admEnvio(admin.ModelAdmin):
    list_display=["comprador", "vendedor", "pedido", "estado", "id", "fecha_emision", "fecha_actualizacion"]
    list_editable=["fecha_actualizacion"]

    class Meta:
        model= Envio

class admEstadoEnvio(admin.ModelAdmin):
    list_display=["id", "nombre"]
    list_editable=["nombre"]

    class Meta:
        model = EstadoEnvio

register = [Usuario, ProductoVenta, ProductoImagen, Categoria, Pedido, EstadoPedido, DetallePedido, Envio, EstadoEnvio]
classes = [admUsuario, admProductoVenta, admProductoImagen, admCategoria, admPedido, admEstadoPedido, admDetallePedido, admEnvio, admEstadoEnvio]
for x in range(0, len(register), 1):
    admin.site.register(register[x], classes[x])

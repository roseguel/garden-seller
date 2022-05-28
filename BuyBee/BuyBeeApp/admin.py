from django.contrib import admin

from BuyBeeApp.models import Categoria, ProductoImagen, ProductoVenta, Usuario

# Register your models here.
class admUsuario(admin.ModelAdmin):
    list_display=["rut", "nombres", "apellidos", "email", "numero", "foto_perfil"]
    list_editable=["nombres", "apellidos", "email", "numero", "foto_perfil"]
    
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

register = [Usuario, ProductoVenta, ProductoImagen, Categoria]
classes = [admUsuario, admProductoVenta, admProductoImagen, admCategoria]
for x in range(0, len(register), 1):
    admin.site.register(register[x], classes[x])

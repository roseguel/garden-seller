from email.policy import default
from BuyBee.urls import path
from BuyBeeApp.views import carrito, categoria, detallePedidoViewSet, AgregarUsuario, ModificarUsuario, AgregarCategoria,ModificarCategoria, AgregarEnvio,ModificarEnvio,AgregarPedido,ModificarPedido,AgregarProducto,ModificarProducto, envioViewSet, estadoEnvioViewSet, estadoPedidoViewSet, home, informacionEnvio, pedidoViewSet, productoImagenViewSet, productoVentaViewSet, publicarProducto, envio, quienesSomos, ayuda, perfil, producto, iniciarSesion, registrarse, registropersonal, suscripcion, usuarioViewSet, vendedor
from django.contrib.auth.views import LoginView
from django.urls import path, include

from rest_framework import routers

router = routers.DefaultRouter()
nombres = ["productoventa", "productoimagen", "estadopedido", "pedido", "estadoenvio", "envio", "detallepedido", "usuario"]
viewSet = [productoVentaViewSet, productoImagenViewSet, estadoPedidoViewSet, pedidoViewSet, estadoEnvioViewSet, envioViewSet, detallePedidoViewSet, usuarioViewSet]
for x in range(0, len(nombres), 1):
    router.register(nombres[x], viewSet[x])

# Patterns
urlpatterns = [
    path('', home, name="home"),
    path('quienes-somos', quienesSomos, name="quienes-somos"),
    path('suscripcion', suscripcion, name="suscripcion"),
    path('ayuda', ayuda, name="ayuda"),
    path('iniciar-sesion', LoginView.as_view(template_name="BuyBeeApp/iniciar-sesion.html"), name="iniciar-sesion"),
    path('registrarse', registrarse, name="registrarse"),
    path('registro-personal', registropersonal, name="registro-personal"),
    path('perfil', perfil, name="perfil"),
    path('producto/<id_producto>', producto, name="producto"),
    path('vendedor/<vendedor>', vendedor, name="vendedor"),
    path('categoria/<id_categoria>', categoria, name="categoria"),
    path('carrito', carrito, name="carrito"),
    path('publicar-producto', publicarProducto, name="publicar-producto"),
    path('envio', envio, name="envio"),
    path('informacion-envio/<id_envio>', informacionEnvio, name="informacion-envio"),

    path('agregar-usuario', AgregarUsuario, name="agregar-usuario"),
    path('modificar-usuario/<id>/', ModificarUsuario, name="modificar-usuario"),
    
    path('agregar-pedido', AgregarPedido, name="agregar-pedido"),
    path('modificar-pedido/<id>/', ModificarPedido, name="modificar-pedido"),
    
    path('agregar-envio', AgregarEnvio, name="agregar-envio"),
    path('modificar-envio/<id>/', ModificarEnvio, name="modificar-envio"),

    path('agregar-producto', AgregarProducto, name="agregar-producto"),
    path('modificar-producto/<id>/', ModificarProducto, name="modificar-producto"),

    path('agregar-categoria', AgregarCategoria, name="agregar-categoria"),
    path('modificar-categoria/<id>/', ModificarCategoria, name="modificar-categoria"),

    path('api/', include(router.urls)),
]
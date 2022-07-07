from email.policy import default
from BuyBee.urls import path
from BuyBeeApp.views import administracion, carrito, categoria, detallePedidoViewSet, editarProducto, envioViewSet, estadoEnvioViewSet, estadoPedidoViewSet, home, informacionEnvio, pedidoViewSet, productoImagenViewSet, productoVentaViewSet, publicarProducto, quienesSomos, ayuda, perfil, producto, iniciarSesion, registrarse, registropersonal, suscripcion, usuarioViewSet, vendedor
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
    path('informacion-envio/<id_envio>', informacionEnvio, name="informacion-envio"),
    path('editar-producto/<id_producto>', editarProducto, name="editar-producto"),
    path('administracion/', administracion, name="administracion"),
    path('administracion/<tipo>', administracion, name="administracion"),
    path('api/', include(router.urls)),
]
from BuyBee.urls import path
from BuyBeeApp.views import formProd, home, quienesSomos, ayuda, perfil, producto, vendedor, iniciarSesion, agradecimiento, categoria, envio, carrito, registrarse, registropersonal, suscripcion, historialCompras, formProd
from django.contrib.auth.views import LoginView
from django.urls import path, include

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
    path('historial', historialCompras, name="historial"),
    path('vendedor', vendedor, name="vendedor"),
    path('agregar-producto', formProd, name="agregar-producto"),
    path('carrito', carrito, name="carrito"),
    path('envio', envio, name="envio"),
    path('gracias', agradecimiento, name="gracias"),
    path('categoria', categoria, name="categoria"),
]
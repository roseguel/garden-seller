from BuyBee.urls import path
from BuyBeeApp.views import home, quienesSomos, ayuda, producto

# Patterns
urlpatterns = [
    path('', home, name="home"),
    path('quienes-somos', quienesSomos, name="quienes-somos"),
    path('ayuda', ayuda, name="ayuda"),
    path('producto/<id_producto>', producto, name="producto"),
]
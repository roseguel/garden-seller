from math import prod
from django.shortcuts import render, get_object_or_404, redirect

from BuyBeeApp.models import ProductoImagen, ProductoVenta

# Create your views here.
def home(r):
    prod_rec = ProductoVenta.objects.order_by('-vistas', '-compras').values()[:10]
    for x in prod_rec:
        x["nombre"] = x["nombre"][:13]
        x["imagen"] = ProductoImagen.objects.filter(producto_id=x["id"]).values()[0]
    contexto={
        "productos_recomendados": prod_rec
    }
    return render(r, "BuyBeeApp/home.html", contexto)

def quienesSomos(r):
    return render(r, "BuyBeeApp/quienes-somos.html")
    
def ayuda(r):
    return render(r, "BuyBeeApp/ayuda.html")

def producto(r, id_producto):
    producto = get_object_or_404(ProductoVenta, id=id_producto)
    imagenes = ProductoImagen.objects.filter(producto_id=producto.id).values()

    contexto = {
        "producto": producto,
        "imagenes": imagenes,
        "activa": imagenes[0]["id"]
    }

    return render(r, "BuyBeeApp/producto.html", contexto)
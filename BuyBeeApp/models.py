from tkinter import CASCADE
from typing import Optional
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombreusuario = models.CharField(max_length=128)
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    email = models.EmailField()
    numero = models.IntegerField(null=True)
    foto_perfil = models.ImageField(upload_to="fotosPerfil", null=True)
    suscrito = models.BooleanField(default=False)

    def __str__(self):
        return self.nombres

class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=32)
    foto = models.ImageField(upload_to="categorias", null=True)

    def __str__(self):
        return self.nombre

class ProductoVenta(models.Model):
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=1024, blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha_publicacion = models.DateField()
    # Para recomendados
    vistas = models.IntegerField()
    compras = models.IntegerField()

    def __str__(self):
        return self.nombre

class ProductoImagen(models.Model):
    producto = models.ForeignKey(ProductoVenta, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    imagen = models.ImageField(upload_to="productosImagenes")

class Carrito(models.Model):
    total = models.IntegerField()
    cupon = models.CharField(max_length=12)
    duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.duenio.rut

class EstadoPedido(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoPedido, on_delete=models.DO_NOTHING)
    id = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    producto = models.ManyToManyField(ProductoVenta)
    id = models.BigAutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()

    def __str__(self):
        return str(self.cantidad)

class EstadoEnvio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre

class Envio(models.Model):
    comprador = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    vendedor = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='vendedor')
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoEnvio, on_delete=models.DO_NOTHING)
    id = models.BigAutoField(primary_key=True)
    fecha_emision = models.DateField()
    fecha_actualizacion = models.DateField()

    def __str__(self):
        return str(self.id)

class ProductoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(ProductoVenta, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.producto.nombre
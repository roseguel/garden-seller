from rest_framework import serializers
from BuyBeeApp.models import DetallePedido, Envio, EstadoEnvio, EstadoPedido, Pedido, ProductoImagen, ProductoVenta, Usuario
from django.shortcuts import get_object_or_404

class UsuarioSrlz(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProductoSrlz(serializers.ModelSerializer):
    # Esto es para obtener el field en base a un método. En este caso sería get_<nombre_variable>, es decir, get_imagenes
    imagenes = serializers.SerializerMethodField()
    vendedor = UsuarioSrlz(read_only=True)
    categoria = serializers.CharField(read_only=True, source="categoria.nombre")
    class Meta:
        model = ProductoVenta
        #fields = '__all__' #['__all__']
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'fecha_publicacion', 'vistas', 'compras', 'vendedor', 'categoria', 'imagenes']

    def get_imagenes(self, producto):
        imagenesRaw = ProductoImagen.objects.filter(producto=producto.id).values_list("imagen")
        imagenes = [x[0] for x in imagenesRaw]
        return imagenes

class PedidoSrlz(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__' #['__all__']

class EnvioSrlz(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = '__all__' #['__all__']

class DetallePedidoSrlz(serializers.ModelSerializer):
    producto = ProductoSrlz(read_only=True)
    pedido = PedidoSrlz(read_only=True)
    envio = serializers.SerializerMethodField()
    class Meta:
        model = DetallePedido
        #fields = '__all__'
        fields = ['id', 'cantidad', 'subtotal', 'producto', 'pedido', 'envio']

    def get_envio(self, detalle):
        envio = Envio.objects.filter(pedido=detalle).values()
        for x in envio:
            estado_envio = get_object_or_404(EstadoEnvio, id=x["estado_id"])
            x["estado"] = estado_envio.nombre
            comprador = Usuario.objects.filter(rut=x["comprador_id"]).values()[0]
            x["comprador"] = comprador
        return envio

class ProductoImagenSrlz(serializers.ModelSerializer):
    class Meta:
        model = ProductoImagen
        fields = '__all__' #['__all__']

class EstadoPedidoSrlz(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__' #['__all__']

class EstadoEnvioSrlz(serializers.ModelSerializer):
    class Meta:
        model = EstadoEnvio
        fields = '__all__' #['__all__']
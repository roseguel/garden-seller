from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from BuyBeeApp.forms import registrarUsuario, registroPersonal
from scripts.metodos import formatNumberToPrice, normalizeName, shrinkProdName
from django.contrib.auth import login, authenticate
from django.http import QueryDict
from django.db.models import Q

from BuyBeeApp.models import DetallePedido, Envio, EstadoEnvio, Pedido, ProductoImagen, ProductoVenta, Usuario, Categoria

# Create your views here.
def home(r):
    prod_rec = ProductoVenta.objects.order_by('-vistas', '-compras').values()[:15]
    categorias1 = Categoria.objects.values()[:4]
    categorias2 = Categoria.objects.values()[4:8]
    for x in prod_rec:
        x["nombre"] = shrinkProdName(x["nombre"], 10)
        x["imagen"] = ProductoImagen.objects.filter(producto_id=x["id"]).values()[0]
        x["precio"] = formatNumberToPrice(x["precio"])
    contexto={
        "productos_recomendados": prod_rec,
        "categorias1": categorias1,
        "categorias2": categorias2,
    }
    return render(r, "BuyBeeApp/home.html", contexto)

def quienesSomos(r):
    return render(r, "BuyBeeApp/quienes-somos.html")

@login_required(login_url="iniciar-sesion")
def ayuda(r):
    return render(r, "BuyBeeApp/ayuda.html")
    
def iniciarSesion(r):
    return render(r, "BuyBeeApp/iniciar-sesion.html")

@login_required(login_url="iniciar-sesion")
def perfil(r):
    # Obtengo el usuario y el nombre completo formateado
    usuario = get_object_or_404(Usuario, nombreusuario=r.user.username)
    nombrecompleto = normalizeName(usuario.nombres, usuario.apellidos)
    # Obtengo los productos con el filtro de que el vendedor sea el usuario
    productos_venta = ProductoVenta.objects.filter(vendedor_id=usuario.rut).values()
    for x in productos_venta:
        x["imagen"] = ProductoImagen.objects.filter(producto_id=x["id"]).values()[0]
        x["precio"] = formatNumberToPrice(x["precio"])
    # Obtengo los envios que tiene pendiente el Usuario
    envios = Envio.objects.filter(Q(comprador=usuario.rut) | Q(vendedor=usuario.rut)).values()
    for x in envios:
        receptor = Usuario.objects.filter(rut=x["comprador_id"]).values()[0]
        x["receptor"] = receptor["rut"]
        x["receptor_nombre"] = normalizeName(receptor["nombres"], receptor["apellidos"])
        emisor = Usuario.objects.filter(rut=x["vendedor_id"]).values()[0]
        x["emisor"] = emisor["rut"]
        x["emisor_nombre"] = normalizeName(emisor["nombres"], emisor["apellidos"])
        # Obtengo el estado del envio
        x["estado_nombre"] = get_object_or_404(EstadoEnvio, id=x["estado_id"]).nombre
        x["estado_nombre_raw"] = get_object_or_404(EstadoEnvio, id=x["estado_id"]).nombre.replace(" ", "-")
        # Obtengo la primera imagen del pedido involucrado en el envio.
        rawPedido = get_object_or_404(Pedido, id=x["pedido_id"])
        rawDetalle = DetallePedido.objects.filter(pedido_id=rawPedido.id)[0]
        rawProducto = ProductoVenta.objects.filter(id=rawDetalle.producto.values()[0]["id"])
        rawImagen = ProductoImagen.objects.filter(producto_id=rawProducto.values("id")[0]["id"]).values()[0]
        x["imagen_producto"] = rawImagen["imagen"]
    # Obtengo los pedidos que ha realizado el vendedor
    pedidos = Pedido.objects.filter(comprador=usuario.rut).values()
    for x in pedidos:
        detalle_pedidos = DetallePedido.objects.filter(pedido=x["id"])
        cantidad = 0
        for y in detalle_pedidos:
            # Sumo la cantidad de productos del detalle a
            cantidad += y.cantidad
            # Obtengo la imagen del primer producto iterado
            imagen = ProductoImagen.objects.filter(producto_id=y.id).values()[0]
            if "imagen" not in x.keys():
                x["imagen"] = imagen["imagen"]
        x["cantidad_productos"] = cantidad
    contexto = {
        "usuario": usuario,
        "nombrecompleto": nombrecompleto,
        "pedidos": pedidos,
        "envios": envios,
        "productos": productos_venta,
    }

    if r.method == "POST":
        if (len(r.FILES) > 0):
            usuario.foto_perfil = r.FILES["profilePicture"]
            usuario.save()
        else:
            cambio = []
            if (usuario.nombres != r.POST["nombres"] and r.POST["nombres"] != None):
                usuario.nombres = r.POST["nombres"]
                cambio.append("nombres")
            if (usuario.apellidos != r.POST["apellidos"] and r.POST["apellidos"] != None):
                usuario.apellidos = r.POST["apellidos"]
                cambio.append("apellidos")
            if (usuario.email != r.POST["email"] and r.POST["email"] != None):
                usuario.email = r.POST["email"]
                cambio.append("email")
            if (usuario.numero != r.POST["numero"] and r.POST["numero"] != None or 0):
                usuario.numero = r.POST["numero"]
                cambio.append("numero")
            if (r.POST["password1"] != None and r.POST["password1"] != "" and r.POST["password1"] != " "):
                if (r.user.check_password(r.POST["password1"]) == False):
                    r.user.set_password(r.POST["password1"])
                    r.user.save()
            if (len(cambio) > 0):
                confirmar = True
                if ("email" in cambio):
                    if ("@" not in usuario.email):
                        confirmar = False
                if ("numero" in cambio):
                    if (len(str(usuario.numero)) != 9):
                        confirmar = False
                if (confirmar):
                    usuario.save()
                    return redirect(to="perfil")

    return render(r, "BuyBeeApp/perfil.html", contexto)

def producto(r, id_producto):
    producto = get_object_or_404(ProductoVenta, id=id_producto)
    producto.vistas += 1
    producto.save()
    producto.precio = formatNumberToPrice(producto.precio)
    imagenes = ProductoImagen.objects.filter(producto_id=producto.id).values()

    vendedor = get_object_or_404(Usuario, rut=producto.vendedor_id)

    contexto = {
        "producto": producto,
        "imagenes": imagenes,
        "activa": imagenes[0]["id"],
        "vendedor": vendedor,
    }

    return render(r, "BuyBeeApp/producto.html", contexto)

def registrarse(request):
    if request.method=="POST":
        usuario = registrarUsuario(data=request.POST)
        if usuario.is_valid():
            usuario.save()
            # Obtengo los datos limpios del usuario y contraseña, para poder logear al usuario
            username = usuario.cleaned_data.get('username')
            raw_password = usuario.cleaned_data.get('password1')
            # Creo una instancia de usuario autenticado con los parametros de arriba
            user = authenticate(username=username, password=raw_password)
            # Logeo a la instancia que creé antes utilizando el Request (la petición del cliente) y la instancia
            # del usuario creado anteriormente
            login(request, user)
            return redirect(to = "registro-personal")
    return render(request, "BuyBeeApp/registrarse.html")
    
def suscripcion(request):
    persona = get_object_or_404(Usuario, nombreusuario=request.user.username)
    contexto = {
        "usuario": persona
    }
    if request.method == "POST":
        persona.suscrito = True if persona.suscrito is False else False
        persona.save()
        return redirect(to="perfil")
    return render(request,"BuyBeeApp/suscripcion.html", contexto)

@login_required(login_url="iniciar-sesion")
def registropersonal(request):
    if request.method=="POST":
        # Obtengo al usuario logeado en la request.
        usuario = request.user
        # Creo un diccionario, para posteriormente crear un QueryDict, para usarlos como data para el Form.
        diccionarioQuery = {
            'rut': request.POST["rut"], 
            'nombreusuario': usuario.username,
            'nombres': request.POST["nombres"],
            'apellidos': request.POST["apellidos"],
            'email': usuario.email}
        # Creo un queryDict vacio y mutable (el atributo mutable es para poder cambiar los datos)
        datos = QueryDict('', mutable=True)
        # actualizo el queryDict con el diccionario que creé arriba
        datos.update(diccionarioQuery)
        user = registroPersonal(data=datos)
        if user.is_valid():
            user.save()
            return redirect(to = "perfil")
    return render(request, "BuyBeeApp/registro-personal.html")

def historialCompras(r):
    return render(r, "BuyBeeApp/historial.html")

def vendedor(r, vendedor):
    usuario = get_object_or_404(Usuario, nombreusuario=vendedor)
    productos = ProductoVenta.objects.filter(vendedor=usuario.rut).values()
    productos_vendidos = 0
    for x in productos:
        x["imagen"] = ProductoImagen.objects.filter(producto_id=x["id"]).values()[0]
        productos_vendidos += DetallePedido.objects.filter(producto=x["id"]).count()
    contexto = {
        "vendedor": usuario,
        "vendedor_nombre": normalizeName(usuario.nombres, usuario.apellidos),
        "productos": productos,
        "productos_vendidos": productos_vendidos,
    }
    return render(r, "BuyBeeApp/vendedor.html", contexto)
# Obtener información desde el servidor xd

def categoria(r, id_categoria):
    categoria = get_object_or_404(Categoria, id=id_categoria)
    productos = ProductoVenta.objects.filter(categoria=id_categoria)
    contexto = {
        "categoria": categoria,
        "productos": productos,
    }
    return render(r, "BuyBeeApp/categoria.html", contexto)

def envio(r):
    return render(r, "BuyBeeApp/envio.html")
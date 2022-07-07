# se debe editar el redirect de todos los formularios (estos estan redireccionando al home)

from datetime import datetime
from math import prod
from django import views
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from BuyBeeApp.forms import registrarUsuario, registroPersonal, UsuariosForm, PedidosForm, EnviosForm, ProductosForm, CategoriasForm
from scripts.metodos import formatNumberToPrice, normalizeName, shrinkProdName
from django.contrib.auth import login, authenticate
from django.http import QueryDict
from django.db.models import Q

from BuyBeeApp.models import Carrito, DetallePedido, Envio, EstadoEnvio, EstadoPedido, Pedido, ProductoCarrito, ProductoImagen, ProductoVenta, Usuario, Categoria

from rest_framework import viewsets
from BuyBeeApp.serializers import DetallePedidoSrlz, EnvioSrlz, EstadoEnvioSrlz, EstadoPedidoSrlz, PedidoSrlz, ProductoImagenSrlz, ProductoSrlz, UsuarioSrlz

# Create your views here.
def AgregarUsuario(r):
    usuarios = Usuario.objects.all()
    data = {
        'form': UsuariosForm(),
        'usuarios': usuarios
    }

    if r.method == 'POST':
        formulario = UsuariosForm(data = r.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Usuario ingresado"
            return redirect(to="home") # se debe editar este para volver al crud
        else:
            data["form"] = formulario
            data["mensaje"] = "No se ha ingresado el usuario"

    return render(r, "BuyBeeApp/cruds/agregar.html", data)

def ModificarUsuario(r, id):
    usuario = get_object_or_404(Usuario, id=id)
    data = {
        'form': UsuariosForm(instance=usuario),
    }
    if r.method == 'POST':
        formulario = UsuariosForm(data = r.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Modificacion exitosa"
            return redirect(to="home") # cuando hacemos algo y queremos redirijir a otra pagina usamos este
        else:
            data["form"] = formulario
            data["mensaje"] = "No se ha guardado el formulario"

    return render(r, "BuyBeeApp/cruds/modificar.html", data)

def AgregarPedido(r):
    pedidos = Pedido.objects.all()
    data = {
        'form': PedidosForm(),
        'pedidos': pedidos
    }

    if r.method == 'POST':
        formulario = PedidosForm(data = r.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "pedido ingresado"
            return redirect(to="home") # se debe editar este para volver al crud
        else:
            data["form"] = formulario
            data["mensaje"] = "No se ha ingresado el pedido"

    return render(r, "BuyBeeApp/cruds/agregar.html", data)

def ModificarPedido(r, id):
    pedido = get_object_or_404(Pedido, id=id)
    data = {
        'form': UsuariosForm(instance=pedido),
    }
    if r.method == 'POST':
        formulario = UsuariosForm(data = r.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Modificacion exitosa"
            return redirect(to="home") # cuando hacemos algo y queremos redirijir a otra pagina usamos este
        else:
            data["form"] = formulario
            data["mensaje"] = "No se ha guardado el formulario"

    return render(r, "BuyBeeApp/cruds/modificar.html", data)

def AgregarEnvio(r):
    envios = Envio.objects.all()
    data = {
        'form': EnviosForm(),
        'envios': envios
    }

    if r.method == 'POST':
        formulario = EnviosForm(data = r.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "envio ingresado"
            return redirect(to="home") # se debe editar este para volver al crud
        else:
            data["form"] = formulario
            data["mensaje"] = "No se ha ingresado el envio"

    return render(r, "BuyBeeApp/cruds/agregar.html", data)

def ModificarEnvio(r, id):
    envio = get_object_or_404(Envio, id=id)
    data = {
        'form': EnviosForm(instance=envio),
    }
    if r.method == 'POST':
        formulario = EnviosForm(data = r.POST, instance=envio)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Modificacion exitosa"
            return redirect(to="home") # cuando hacemos algo y queremos redirijir a otra pagina usamos este
        else:
            data["form"] = formulario
            data["mensaje"] = "No se ha guardado el formulario"

    return render(r, "BuyBeeApp/cruds/modificar.html", data)

def AgregarProducto(r):
    productos = ProductoVenta.objects.all()
    data = {
        'form': ProductosForm(),
        'productos': productos
    }

    if r.method == 'POST':
        formulario = ProductosForm(data = r.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "producto ingresado"
            return redirect(to="home") # se debe editar este para volver al crud
        else:
            data["form"] = formulario
            data["mensaje"] = "No se ha ingresado el producto"

    return render(r, "BuyBeeApp/cruds/agregar.html", data)

def ModificarProducto(r, id):
    producto = get_object_or_404(ProductoVenta, id=id)
    data = {
        'form': ProductosForm(instance=producto),
    }
    if r.method == 'POST':
        formulario = ProductosForm(data = r.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Modificacion exitosa"
            return redirect(to="home") # cuando hacemos algo y queremos redirijir a otra pagina usamos este
        else:
            data["form"] = formulario
            data["mensaje"] = "No se ha guardado el formulario"

    return render(r, "BuyBeeApp/cruds/modificar.html", data)

def AgregarCategoria(r):
    categorias = Categoria.objects.all()
    data = {
        'form': CategoriasForm(),
        'categorias': categorias
    }

    if r.method == 'POST':
        formulario = CategoriasForm(data = r.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "categoria ingresada"
            return redirect(to="home") # se debe editar este para volver al crud
        else:
            data["form"] = formulario
            data["mensaje"] = "No se ha ingresado la categoria"

    return render(r, "BuyBeeApp/cruds/agregar.html", data)

def ModificarCategoria(r, id):
    categoria = get_object_or_404(Categoria, id=id)
    data = {
        'form': CategoriasForm(instance=categoria),
    }
    if r.method == 'POST':
        formulario = CategoriasForm(data = r.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Modificacion exitosa"
            return redirect(to="home") # cuando hacemos algo y queremos redirijir a otra pagina usamos este
        else:
            data["form"] = formulario
            data["mensaje"] = "No se ha guardado el formulario"

    return render(r, "BuyBeeApp/cruds/modificar.html", data)

def home(r):
    prod_rec = ProductoVenta.objects.order_by('-vistas', '-compras').values()[:15]
    for x in prod_rec:
        x["nombre"] = shrinkProdName(x["nombre"], 10)
        x["imagen"] = ProductoImagen.objects.filter(producto_id=x["id"]).values()[0]
        x["precio"] = formatNumberToPrice(x["precio"])
    prod_recientes = ProductoVenta.objects.order_by('-fecha_publicacion').values()[:15]
    for x in prod_recientes:
        x["nombre"] = shrinkProdName(x["nombre"], 10)
        x["imagen"] = ProductoImagen.objects.filter(producto_id=x["id"]).values()[0]
        x["precio"] = formatNumberToPrice(x["precio"])
    categorias1 = Categoria.objects.values()[:4]
    categorias2 = Categoria.objects.values()[4:8]
    contexto={
        "productos_recomendados": prod_rec,
        "prod_recientes": prod_recientes,
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
    envios = Envio.objects.filter(comprador=usuario.rut).values()
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
        rawPedido = get_object_or_404(DetallePedido, id=x["pedido_id"])
        rawProducto = ProductoVenta.objects.filter(id=rawPedido.producto.id)
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
            imagen = ProductoImagen.objects.filter(producto_id=y.producto).values()[0]
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
    usuario = get_object_or_404(Usuario, nombreusuario=r.user.username)
    producto = get_object_or_404(ProductoVenta, id=id_producto)
    producto.vistas += 1
    producto.save()
    producto.precio = formatNumberToPrice(producto.precio)
    imagenes = ProductoImagen.objects.filter(producto_id=producto.id).values()

    vendedor = get_object_or_404(Usuario, rut=producto.vendedor_id)
    es_vendedor = True if usuario.rut == vendedor.rut else False

    carrito = Carrito.objects.filter(duenio=usuario.rut).values()
    if len(carrito) < 1:
        carritoObject = Carrito(total=0, cupon="", duenio=usuario)
        carritoObject.save()
        carrito = carritoObject
    carrito = get_object_or_404(Carrito, duenio=usuario.rut)
    productos_carrito = ProductoCarrito.objects.filter(carrito=carrito.id).values()
    en_carrito = False
    for x in productos_carrito:
        if x["producto_id"] is producto.id:
            producto_carrito = x
            en_carrito = True
            break;
    contexto = {
        "producto": producto,
        "imagenes": imagenes,
        "activa": imagenes[0]["id"],
        "vendedor": vendedor,
        "en_carrito": en_carrito,
        "es_vendedor": es_vendedor,
    }

    if r.method == "POST":
        if en_carrito is False:
            productoCarrito = ProductoCarrito(carrito=carrito, producto=producto, cantidad=1)
            productoCarrito.save()
            return redirect(to="carrito")
        else:
            productoCarrito = get_object_or_404(ProductoCarrito, id=producto_carrito["id"])
            productoCarrito.delete()
            return redirect(to="carrito")

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
    for x in productos:
        x.imagen = ProductoImagen.objects.filter(producto_id=x.id).values()[0]
        x.precio_producto = formatNumberToPrice(x.precio)
    contexto = {
        "categoria": categoria,
        "productos": productos,
    }
    return render(r, "BuyBeeApp/categoria.html", contexto)

@login_required(login_url="iniciar-sesion")
def carrito(r):
    usuario = get_object_or_404(Usuario, nombreusuario=r.user.username)
    carrito = Carrito.objects.filter(duenio=usuario.rut).values()
    if len(carrito) < 1:
        carritoObject = Carrito(total=0, cupon="", duenio=usuario)
        carritoObject.save()
        carrito = carritoObject
    carrito = Carrito.objects.filter(duenio=usuario.rut).values()[0]
    productos_carrito = ProductoCarrito.objects.values()
    productos = []
    cantidad = {}
    for x in productos_carrito:
        if x["carrito_id"] is carrito["id"]:
            productos.append(get_object_or_404(ProductoVenta, id=x["producto_id"]))
            cantidad[x["producto_id"]] = x["cantidad"]
    total = 0
    for x in productos:
        x.imagen = ProductoImagen.objects.filter(producto_id=x.id).values()[0]
        total += x.precio
        x.precio = formatNumberToPrice(x.precio)
        x.cantidad = cantidad[x.id]
    contexto = {
        "usuario": usuario,
        "productos": productos,
        "total": total,
    }

    if r.method == "POST":
        try:
            producto_a_eliminarPost = int(r.POST['productoAEliminar'])
        except:
            producto_a_eliminarPost = 0
        if producto_a_eliminarPost > 0:
            producto_a_eliminar = get_object_or_404(ProductoCarrito, producto=producto_a_eliminarPost)
            producto_a_eliminar.delete()
            return redirect(to="carrito")
        else:
            productosRaw = r.POST.getlist("producto")
            cantidadesRaw = r.POST.getlist("cantidad")
            productosCarrito = []
            # Reviso si los productos son los que están en el carrito
            for x in productosRaw:
                productoRaw = ProductoCarrito.objects.filter(Q(carrito=carrito["id"]) & Q(producto=x)).values("producto")
                if len(productoRaw.values()) == 0:
                    contexto["error"] = "no_such_product"
                    render(r, "BuyBeeApp/carrito.html", contexto)
                    break;
                else:
                    producto = get_object_or_404(ProductoVenta, id=x)
                    productosCarrito.append(producto)
            c = -1
            total = 0
            # Obtengo el estado
            estadoPedidoRealizado = get_object_or_404(EstadoPedido, id=1)
            # Creo el Pedido
            pedidoRealizado = Pedido(comprador=usuario, estado=estadoPedidoRealizado, fecha=datetime.now().strftime("%Y-%m-%d"), total=0)
            pedidoRealizado.save()
            for x in productosCarrito:
                c += 1
                if x.stock >= int(cantidadesRaw[c]):
                    # Aumento el Total
                    total += x.precio
                    # Aumento los comprados y disminuyo el Stock
                    x.compras += int(cantidadesRaw[c])
                    x.stock -= int(cantidadesRaw[c])
                    x.save()
                    # Creo el detalle del pedido
                    detallePedidoRealizado = DetallePedido(pedido=pedidoRealizado, producto=x, cantidad=int(cantidadesRaw[c]), subtotal=int(cantidadesRaw[c]) * x.precio)
                    detallePedidoRealizado.save()
                    # Creo el estado del Envio
                    estadoEnvioRealizado = get_object_or_404(EstadoEnvio, id=1)
                    # Creo el Envio
                    vendedorProd = get_object_or_404(Usuario, rut=x.vendedor.rut)
                    envioRealizado = Envio(comprador=usuario, vendedor=vendedorProd, pedido=detallePedidoRealizado, estado=estadoEnvioRealizado,
                                            fecha_emision=datetime.now().strftime("%Y-%m-%d"), fecha_actualizacion=datetime.now().strftime("%Y-%m-%d"))
                    envioRealizado.save()
                    
            pedidoRealizado.total = total
            pedidoRealizado.save()
            carritoEditar = get_object_or_404(Carrito, duenio=usuario.rut)
            ProductoCarrito.objects.filter(carrito=carritoEditar).delete()
            return redirect(to="perfil")
    return render(r, "BuyBeeApp/carrito.html", contexto)

@login_required(login_url="iniciar-sesion")
def publicarProducto(r):
    usuario = get_object_or_404(Usuario, nombreusuario=r.user.username)
    categorias = Categoria.objects.values()
    contexto = {
        "usuario": usuario,
        "categorias": categorias,
    }
    if r.method == "POST":
        nombre = r.POST["nombre"]
        categoria = get_object_or_404(Categoria, id=int(r.POST["categoria"]))
        descripcion = r.POST["descripcion"]
        precio = r.POST["precio"]
        stock = r.POST["stock"]
        fecha = datetime.now().strftime("%Y-%m-%d")
        producto = ProductoVenta(vendedor=usuario, categoria=categoria, nombre=nombre, descripcion=descripcion, precio=precio, stock=stock,
                                fecha_publicacion=fecha, vistas=0, compras=0)
        if len(r.FILES.getlist('imagen')) > 0:
            producto.save()
            for imagen in r.FILES.getlist('imagen'):
                productoImagen = ProductoImagen(producto=producto, imagen=imagen)    
                productoImagen.save()
        return redirect(to=f"producto/{producto.id}")

    return render(r, "BuyBeeApp/subir-producto.html", contexto)

def envio(r):
    return render(r,"BuyBeeApp/envio.html")

@login_required(login_url="iniciar-sesion")
def informacionEnvio(r, id_envio):
    envio = get_object_or_404(Envio, id=id_envio)
    #envio = Envio.objects.filter(id=id_envio).values()[0]
    comprador = Usuario.objects.filter(rut=envio.comprador_id).values()[0]
    comprador["nombre_completo"] = normalizeName(comprador["nombres"], comprador["apellidos"])
    vendedor = Usuario.objects.filter(rut=envio.vendedor_id).values()[0]
    if r.user.username == vendedor["nombreusuario"]:
        estado_envio = EstadoEnvio.objects.filter(id=envio.estado_id).values()[0]
        estados_envios = EstadoEnvio.objects.values()
        pedido = DetallePedido.objects.filter(id=envio.pedido_id).values()[0]
        producto = ProductoVenta.objects.filter(id=pedido["producto_id"]).values()[0]
        imagenes = ProductoImagen.objects.filter(producto=producto["id"]).values()
        contexto = {
            "envio": envio,
            "estado_envio": estado_envio,
            "estados_envios": estados_envios,
            "comprador": comprador,
            "pedido": pedido,
            "producto": producto,
            "imagenes": imagenes,
            "activa": imagenes[0]["id"],
        }
        if r.method == "POST":
            if int(r.POST["estado_envio"]) != estado_envio["id"]:
                envio.estado_id = int(r.POST["estado_envio"])
                envio.save()
                return redirect(to="perfil")
        return render(r, "BuyBeeApp/informacion-envio.html", contexto)
    return redirect(to="perfil")

# ViewSet
class productoVentaViewSet(viewsets.ModelViewSet):
    queryset = ProductoVenta.objects.all()
    serializer_class = ProductoSrlz

    def get_queryset(self):
        nombre = self.request.GET.get('nombre')
        id = self.request.GET.get('id')
        vendedor = self.request.GET.get('vendedor')
        categoria = self.request.GET.get('categoria')
        if nombre != None:
            #productos = ProductoVenta.objects.filter(nombre=nombre)
            return ProductoVenta.objects.filter(nombre=nombre)
        elif id != None:
            #productos = ProductoVenta.objects.filter(id=id)
            return ProductoVenta.objects.filter(id=id)
        elif vendedor != None:
            #productos = ProductoVenta.objects.filter(vendedor=vendedor)
            return ProductoVenta.objects.filter(vendedor=vendedor)
        elif categoria != None:
            return ProductoVenta.objects.filter(categoria=categoria)
        else:
            return ProductoVenta.objects.all()

class productoImagenViewSet(viewsets.ModelViewSet):
    queryset = ProductoImagen.objects.all()
    serializer_class = ProductoImagenSrlz

class estadoPedidoViewSet(viewsets.ModelViewSet):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoSrlz

class pedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSrlz

class estadoEnvioViewSet(viewsets.ModelViewSet):
    queryset = EstadoEnvio.objects.all()
    serializer_class = EstadoEnvioSrlz

class envioViewSet(viewsets.ModelViewSet):
    queryset = Envio.objects.all()
    serializer_class = EnvioSrlz

class detallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSrlz

    def get_queryset(self):
        pedido = self.request.GET.get('pedido')
        producto = self.request.GET.get('producto')
        if pedido != None:
            return DetallePedido.objects.filter(pedido=pedido)
        elif producto != None:
            return DetallePedido.objects.filter(producto=producto)
        else:
            return DetallePedido.objects.all()

class usuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSrlz


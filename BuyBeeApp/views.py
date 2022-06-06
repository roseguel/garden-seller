from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from BuyBeeApp.forms import registrarUsuario, registroPersonal
from scripts.metodos import formatNumberToPrice, shrinkProdName
from django.contrib.auth import login, authenticate
from django.http import QueryDict

from BuyBeeApp.models import ProductoImagen, ProductoVenta, Usuario, Categoria

# Create your views here.
def home(r):
    prod_rec = ProductoVenta.objects.order_by('-vistas', '-compras').values()[:15]
    categorias1 = Categoria.objects.values()[:4]
    categorias2 = Categoria.objects.values()[4:8]
    for x in prod_rec:
        x["nombre"] = shrinkProdName(x["nombre"])
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
    usuario = get_object_or_404(Usuario, nombreusuario=r.user.username)
    contexto = {
        "usuario": usuario
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
        "vendedor": vendedor
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
    return render(request,"BuyBeeApp/suscripcion.html")

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

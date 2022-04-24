logged = false;

function irAPagina(pagina) {
    switch (pagina) {
        case 'publicarproducto':
            url = logged == true ? "fmproductos.html" : "iniciar-sesion.html";
            break;
        case 'perfil':
            url = logged == true ? "perfil.html" : "iniciar-sesion.html";
            break;
        case 'carrito':
            url = logged == true ? "carrito.html" : "iniciar-sesion.html";
            break;
        case 'guardados':
            url = logged == true ? "guardados.html" : "iniciar-sesion.html";
            break;
        default:
            url = "404.html";
    }
    window.open(url, "_self")
}
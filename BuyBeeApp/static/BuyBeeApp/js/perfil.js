foto = new DataTransfer();

function cambiarFoto() {
    imagen = document.getElementById("imagenForm").files.item(0)
    url = URL.createObjectURL(imagen);
    document.getElementById("sinFotoDePerfil").style.display = "none";
    document.getElementById("fotoDePerfil").src = url;
    document.getElementById("conFotoDePerfil").style.display = "flex";
}

function cambiarInfo(e) {
    if (!document.getElementById(e).classList.contains("activa")) {
        id = document.getElementsByClassName("activa")[0].id
        document.getElementById(id).style.display = "none";
        document.getElementsByClassName("activa")[0].classList.remove("activa");
        document.getElementById(e).style.display = "flex";
        document.getElementsByClassName(e)[0].classList.add("activa");
    }
}
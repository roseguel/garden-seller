foto = new DataTransfer();

function cambiarFoto() {
    imagen = document.getElementById("imagenForm").files.item(0)
    url = URL.createObjectURL(imagen);
    document.getElementById("sinFotoDePerfil").style.display = "none";
    document.getElementById("fotoDePerfil").src = url;
    document.getElementById("conFotoDePerfil").style.display = "flex";
}
function cambiarImagenTest() {
    // Datos imagen
    // Obtengo el último archivo subido
    imagen = document.getElementById("formFileSm").files.item(document.getElementById("formFileSm").files.size - 1)
    // Creo una URL del último archivo subido
    url = URL.createObjectURL(imagen);
    // Uso operador ternario para evitar IF, y evito que los nombres sobrepasen los 10 carácteres.
    nombre = imagen.name.length > 10 ? imagen.name.substr(0, 10) : imagen.name;
    // Creo un Child
    const nombreImagen = document.createElement('div');
    nombreImagen.style = "background: #95D6C2; border-radius: 31.5px;";
    nombreImagen.innerHTML = nombre
    // Agrego el Child a placeHoldersFotos
    document.getElementById("placeHoldersFotos").appendChild(nombreImagen)
    // Asigno la imagen a la última añadida.
    document.getElementsByClassName("phproduct")[0].src = url;
    document.getElementsByClassName("phproduct")[0].style.filter = "none";
}
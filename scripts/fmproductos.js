const files = new DataTransfer()

function cambiarImagenTest() {
    // Datos imagen
    // Obtengo el último archivo subido
    imagen = document.getElementById("formFileSm").files.item(0)
    if (imagen != undefined) {
        files.items.add(imagen)
        // Creo una URL del último archivo subido
        url = URL.createObjectURL(imagen);
        // Uso operador ternario para evitar IF, y evito que los nombres sobrepasen los 10 carácteres.
        nombre = imagen.name.length > 10 ? imagen.name.substr(0, 10) + ".." + imagen.type.replace("image/", ".") : imagen.name + imagen.type.replace("image/", ".");
        // Creo un Child
        const eliminarImagen = document.createElement('img');
        eliminarImagen.className = "eliminarImagen";
        eliminarImagen.src = "assets/images/Eliminar.png";
        eliminarImagen.setAttribute('onclick','eliminarImagenTest(event)')
        eliminarImagen.id = `eliminar${files.items.length}`;

        const nombreImagen = document.createElement('div');
        nombreImagen.className = "archivo_subido";
        nombreImagen.id = `nombreImagen${files.items.length}`;
        nombreImagen.appendChild(eliminarImagen);
        nombreImagen.append(nombre);
        // Agrego el Child a placeHoldersFotos
        document.getElementById("placeHoldersFotos").appendChild(nombreImagen)
        // Asigno la imagen a la última añadida.
        document.getElementsByClassName("phproduct")[0].src = url;
        document.getElementsByClassName("phproduct")[0].style.filter = "none";
    }
}

function eliminarImagenTest(e) {
    id = e.target.id;
    files.items.remove(parseInt(id.replace("eliminar", "")) - 1);
    for (x of document.getElementById("placeHoldersFotos").childNodes) {
        if (x.id != undefined && x.id == id.replace("eliminar", "nombreImagen")) {
            document.getElementById(id).remove();
            document.getElementById(x.id).remove();
        }
    }
}
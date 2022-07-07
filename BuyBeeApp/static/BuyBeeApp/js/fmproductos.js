function cambiarImagenes(firstLoad) {
    document.getElementById("inner-carousel").innerHTML = ""
    if (!firstLoad) {
        imagenes = document.getElementById("formFileSm").files;
        for (c = 0; c < imagenes.length; c++) {
            imagen = imagenes.item(c)
            url = URL.createObjectURL(imagen)
            if (c == 0) {
                document.getElementById("inner-carousel").innerHTML += `
                <div id="item" class="carousel-item active">
                    <img class="carrusel-imagen" src="${url}">
                </div>`
                document.getElementsByClassName("carousel-indicators")[0].innerHTML += `
                <button type="button" data-bs-target="#imagenes" data-bs-slide-to="${c}" class="active" aria-current="true" aria-label="Slide ${c + 1}">
                </button>`
            } else {
                document.getElementById("inner-carousel").innerHTML += `
                <div id="item" class="carousel-item">
                    <img class="carrusel-imagen" src="${url}">
                </div>`
                document.getElementsByClassName("carousel-indicators")[0].innerHTML += `
                <button type="button" data-bs-target="#imagenes" data-bs-slide-to="${c}" aria-label="Slide ${c + 1}">
                </button>`
            }
        }
        if (imagenes.length > 1) {
            document.getElementById("inner-carousel").innerHTML += `
            <button class="carousel-control-prev carrusel-boton" type="button" data-bs-target="#imagenes" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next carrusel-boton" type="button" data-bs-target="#imagenes" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>`
        }
    } else {
        document.getElementById("inner-carousel").innerHTML = `
        <div id="item" class="carousel-item active">
            <img class="carrusel-imagen" src="http://127.0.0.1:8000/static/BuyBeeApp/assets/images/florazul.jpg" style="filter: grayscale(100%)">
        </div>`
    }
}

function validarForm(e) {
    if (document.getElementById("formFileSm").files.length < 1) {
        e.preventDefault();
        document.getElementById("error").style.display = "flex";
        document.getElementById("error-msg").innerText = "Por favor selecciona una imagen o imágenes para el Producto";
        return false;
    }
    if (document.getElementById("categoria").value == 'default') {
        e.preventDefault();
        document.getElementById("error").style.display = "flex";
        document.getElementById("error-msg").innerText = "Por favor selecciona una categoría para el Producto";
        return false;
    }
}

function cargarImagenes(id) {
    document.getElementById("inner-carousel").innerHTML = ""
    var imagenesRaw = {"url": `http://127.0.0.1:8000/api/productoventa/${id}`, "method": "GET", "timeout": 0};
    $.getJSON(imagenesRaw).done(function (imagenesRawData) {
        imagenes = imagenesRawData["imagenes"];
        for (c = 0; c < imagenes.length; c++) {
            if (c == 0) {
                document.getElementById("inner-carousel").innerHTML += `
                <div id="item" class="carousel-item active">
                    <img class="carrusel-imagen" src="/media/${imagenes[c]}">
                </div>`
                document.getElementsByClassName("carousel-indicators")[0].innerHTML += `
                <button type="button" data-bs-target="#imagenes" data-bs-slide-to="${c}" class="active" aria-current="true" aria-label="Slide ${c + 1}">
                </button>`
            } else {
                document.getElementById("inner-carousel").innerHTML += `
                <div id="item" class="carousel-item">
                    <img class="carrusel-imagen" src="/media/${imagenes[c]}">
                </div>`
                document.getElementsByClassName("carousel-indicators")[0].innerHTML += `
                <button type="button" data-bs-target="#imagenes" data-bs-slide-to="${c}" aria-label="Slide ${c + 1}">
                </button>`
            }
        }
        if (imagenes.length > 1) {
            document.getElementById("inner-carousel").innerHTML += `
            <button class="carousel-control-prev carrusel-boton" type="button" data-bs-target="#imagenes" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next carrusel-boton" type="button" data-bs-target="#imagenes" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>`
        }
    });
}
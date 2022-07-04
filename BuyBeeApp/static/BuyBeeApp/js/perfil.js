function cambiarInfo(e) {
    if (!document.getElementById(e).classList.contains("activa")) {
        id = document.getElementsByClassName("activa")[0].classList[0]
        document.getElementById(id).style.display = "none";
        document.getElementsByClassName("activa")[0].classList.remove("activa");
        document.getElementById(e).style.display = "flex";
        document.getElementsByClassName(e)[0].classList.add("activa");
    }
}

function displayModal(modal, elemento) {
    switch(modal) {
        case 'pedido':
            document.getElementById("mdl-ped-right-info").innerHTML = "";
            pedido = elemento.attr("id").replace("pedido-", "")
            // request
            var pedidoRaw = {"url": `http://127.0.0.1:8000/api/pedido/${pedido}`, "method": "GET", "timeout": 0};
            $.getJSON(pedidoRaw).done(function (response) {
                document.getElementById("numeropedido").textContent = document.getElementById("numeropedido").textContent.replace("{numeropedido}", response["id"])
                document.getElementById("fechapedido").textContent = document.getElementById("fechapedido").textContent.replace("{fechapedido}", response["fecha"])
                document.getElementById("estadopedido").textContent = document.getElementById("estadopedido").textContent.replace("{estadopedido}", response["estado"])
                document.getElementById("totalpedido").textContent = document.getElementById("totalpedido").textContent.replace("{totalpedido}", response["total"])
            });
            // Detalles Pedidos
            var detallePedido = {"url": `http://127.0.0.1:8000/api/detallepedido/?pedido=${pedido}`, "method": "GET", "timeout": 0}
            $.getJSON(detallePedido).done(function (detalle) {
                console.log()
                document.getElementById("mdl-ped-right-info").innerHTML += `<div class="pedido-producto-data">
                <img src="media/${detalle[0]["producto"]["imagenes"][0]}">
                <div class="pedido-producto-info">
                    <a class="pedido-producto-title" href="http://127.0.0.1:8000/producto/${detalle[0]["producto"]["id"]}">${detalle[0]["producto"]["nombre"]}</a>
                    <span>Cantidad: ${detalle[0]["cantidad"]}</span>
                    <span>Subtotal: ${detalle[0]["subtotal"]}</span>
                </div>
            </div>`
            })
            document.getElementById("mdl-ped").style.display = "flex";
            break;
        case 'producto':
            document.getElementById("mdl-prod-right-info").innerHTML = ""
            idProducto = elemento.attr("name")
            // Left Side
            var productoRaw = {"url": `http://127.0.0.1:8000/api/productoventa/?id=${idProducto}`, "method": "GET", "timeout": 0};
            $.getJSON(productoRaw).done(function (productoRawData) {
                document.getElementById("mdl-prod-figure-img").src = `media/${productoRawData[0]["imagenes"][0]}`;
                document.getElementById("mdl-prod-figure-title").textContent = productoRawData[0]["nombre"]
                document.getElementById("mdl-prod-figure-precio").textContent = `Precio: ${productoRawData[0]["precio"]}`
                document.getElementById("mdl-prod-figure-stock").textContent = `Stock: ${productoRawData[0]["stock"]}`
                document.getElementById("mdl-prod-figure-fecha").textContent = `Publicación: ${productoRawData[0]["fecha_publicacion"]}`
                document.getElementById("mdl-prod-figure-vistas").textContent = `Vistas: ${productoRawData[0]["vistas"]}`
                document.getElementById("mdl-prod-figure-compras").textContent = `Compras: ${productoRawData[0]["compras"]}`
                document.getElementById("mdl-prod-button").onclick = function() {
                    window.open("http://127.0.0.1:8000/producto/" + idProducto, "_self")
                }
            });
            // Right Side
            var detallesRaw = {"url": `http://127.0.0.1:8000/api/detallepedido/?producto=${idProducto}`, "method": "GET", "timeout": 0};
            $.getJSON(detallesRaw).done(function (detallesRawData) {
                detallesRawData.forEach(detalle => {
                    document.getElementById("mdl-prod-right-info").innerHTML += `
                    <div class="mdl-prod-right-info-data">
                        <span class="info-data-user">${detalle["envio"][0]["comprador"]["nombres"].split(" ")[0]} ${detalle["envio"][0]["comprador"]["apellidos"].split(" ")[0]}</span>
                        <span class="info-data-fecha">Fecha Pedido: ${detalle["pedido"]["fecha"]}</span>
                        <span class="info-data-user">Cantidad: ${detalle["cantidad"]}</span>
                        <span class="info-data-envio">Estado Envio:</span>
                        <span class="info-data-estadoenvio">${detalle["envio"][0]["estado"]} <img class="info-data-editarenvio" src="http://127.0.0.1:8000/static/BuyBeeApp/assets/images/Editar.png" onclick="window.open('http://127.0.0.1:8000/informacion-envio/${detalle["envio"][0]["id"]}', '_self')"></span>
                    </div>`
                });
            });
            document.getElementById("mdl-prod").style.display = "flex";
            break;
        default:
            break;
    }
}

function salirModal(modal) {
    switch(modal) {
        case 'producto':
            document.getElementById("mdl-prod").style.display = "none";
            document.getElementById("mdl-prod-figure-img").src = "";
            document.getElementById("mdl-prod-figure-title").textContent = ""
            document.getElementById("mdl-prod-figure-precio").textContent = ""
            document.getElementById("mdl-prod-figure-stock").textContent = ""
            document.getElementById("mdl-prod-figure-fecha").textContent = ""
            document.getElementById("mdl-prod-figure-vistas").textContent = ""
            document.getElementById("mdl-prod-figure-compras").textContent = ""
            document.getElementById("mdl-prod-button").onclick = ""
        default:
            break;
    }
}
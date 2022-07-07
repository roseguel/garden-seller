function cambiarFiltro(elemento, tipoCrud) {
    tipoFiltro = elemento.id.replace("filtro-", "")
    if (tipoCrud == "usuarios") {
        document.getElementById("cuerpo-tablas").innerHTML = "";
        usuariosRaw = elemento.classList.contains("activo") ? {"url": `http://127.0.0.1:8000/api/usuario/?order=${tipoFiltro}`, "method": "GET", "timeout": 0} : {"url": `http://127.0.0.1:8000/api/usuario/?order=-${tipoFiltro}`, "method": "GET", "timeout": 0}
        $.getJSON(usuariosRaw).done(function (usuarios) {
            usuarios.forEach(usuario => {
                html = `<tr>
                    <th class="text-center" scope="row">${usuario["rut"]}</th>
                    <td>${usuario["nombreusuario"]}</td>
                    <td>${usuario["nombres"]} ${usuario["apellidos"]}</td>
                    <td>${usuario["email"]}</td>
                    <td class="text-center">`
                if (usuario["suscrito"]) {
                    html += `<img class="imagen si" src="http://127.0.0.1:8000/static/BuyBeeApp/assets/images/Admin/Si.png">`
                } else {
                    html += `<img class="imagen no" src="http://127.0.0.1:8000/static/BuyBeeApp/assets/images/Admin/No.png">`
                }
                html += `</td>
                        <td>
                            <img class="imagen accion editar" src="http://127.0.0.1:8000/static/BuyBeeApp/assets/images/Admin/Editar.png">
                            <img class="imagen accion eliminar" src="http://127.0.0.1:8000/static/BuyBeeApp/assets/images/Admin/Eliminar.png">
                        </td>
                    </tr>`;
                document.getElementById("cuerpo-tablas").innerHTML += html;
            });
        });
    } else if (tipoCrud == "pedidos") {
        document.getElementById("cuerpo-tablas").innerHTML = "";
        pedidosRaw = elemento.classList.contains("activo") ? {"url": `http://127.0.0.1:8000/api/pedido/?order=${tipoFiltro}`, "method": "GET", "timeout": 0} : {"url": `http://127.0.0.1:8000/api/pedido/?order=-${tipoFiltro}`, "method": "GET", "timeout": 0}
        $.getJSON(pedidosRaw).done(function (pedidos) {
            pedidos.forEach(pedido => {
                document.getElementById("cuerpo-tablas").innerHTML += `<tr>
                    <th class="text-center" scope="row">${pedido["id"]}</th>
                    <td>${pedido["comprador"]["nombres"]} ${pedido["comprador"]["apellidos"]}</td>
                    <td>${pedido["estado"]["nombre"]}</td>
                    <td>${pedido["fecha"]}</td>
                    <td>${pedido["total"]}</td>
                    <td>
                        <img class="imagen accion editar" src="http://127.0.0.1:8000/static/BuyBeeApp/assets/images/Admin/Editar.png">
                        <img class="imagen accion eliminar" src="http://127.0.0.1:8000/static/BuyBeeApp/assets/images/Admin/Eliminar.png">
                    </td>
                    </tr>`;
            });
        });
    } else if (tipoCrud == "envios") {
        document.getElementById("cuerpo-tablas").innerHTML = "";
        enviosRaw = elemento.classList.contains("activo") ? {"url": `http://127.0.0.1:8000/api/envio/?order=${tipoFiltro}`, "method": "GET", "timeout": 0} : {"url": `http://127.0.0.1:8000/api/envio/?order=-${tipoFiltro}`, "method": "GET", "timeout": 0}
        $.getJSON(enviosRaw).done(function (envios) {
            envios.forEach(envio => {
                document.getElementById("cuerpo-tablas").innerHTML += `<tr>
                    <th class="text-center" scope="row">${envio["id"]}</th>
                    <td>${envio["comprador"]["nombres"]} ${envio["comprador"]["apellidos"]}</td>
                    <td>${envio["vendedor"]["nombres"]} ${envio["vendedor"]["apellidos"]}</td>
                    <td>${envio["pedido"]}</td>
                    <td>${envio["estado"]["nombre"]}</td>
                    <td>${envio["fecha_emision"]}</td>
                    <td>${envio["fecha_actualizacion"]}</td>
                    <td>
                        <img class="imagen accion editar" src="{% static 'BuyBeeApp/assets/images/Admin/Editar.png' %}">
                        <img class="imagen accion eliminar" src="{% static 'BuyBeeApp/assets/images/Admin/Eliminar.png' %}">
                    </td>
                </tr>`
            });
        });
    } else if (tipoCrud == "productos") {
        document.getElementById("cuerpo-tablas").innerHTML = "";
        productosRaw = elemento.classList.contains("activo") ? {"url": `http://127.0.0.1:8000/api/producto/?order=${tipoFiltro}`, "method": "GET", "timeout": 0} : {"url": `http://127.0.0.1:8000/api/producto/?order=-${tipoFiltro}`, "method": "GET", "timeout": 0}
        $.getJSON(productosRaw).done(function (productos) {
            productos.forEach(producto => {
                document.getElementById("cuerpo-tablas").innerHTML += `<tr>
                    <th class="text-center" scope="row">${producto["id"]}</th>
                    <td>${producto["categoria"]["nombre"]}</td>
                    <td>${producto["nombre"]}</td>
                    <td>${producto["descripcion"]}</td>
                    <td>${producto["precio"]}</td>
                    <td>${producto["stock"]}</td>
                    <td>${producto["vendedor"]["nombres"]} ${producto["vendedor"]["apellidos"]}</td>
                    <td>${producto["fecha_publicacion"]}</td>
                    <td>${producto["vistas"]}</td>
                    <td>${producto["compras"]}</td>
                    <td>
                        <img class="imagen accion editar" src="{% static 'BuyBeeApp/assets/images/Admin/Editar.png' %}">
                        <img class="imagen accion eliminar" src="{% static 'BuyBeeApp/assets/images/Admin/Eliminar.png' %}">
                    </td>
                </tr>`
            });
        });
    }
}
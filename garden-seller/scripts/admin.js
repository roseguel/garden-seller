const exData = new Map([
    ['usuarios', ['Moonie;moonie@gmail.com', 'Wacoldo;wacoldo@live.cl', 'Euclides;euclides@microsoft.com']],
    ['envios', ['10;Puente Alto, Santiago', '20;Los Copihues, Talcahuano', '30;Centinela 1, Talcahuano']],
    ['pedidos', ['10;Enviado', '20;En Recorrido', '30;Confirmando']]
]);

const fields = new Map([
    ['usuarios', 'Usuario Correo'], 
    ['envios', 'ID Destino'], 
    ['pedidos', 'ID Estado']
]);

function changeCrudMode(option) {
    let old = document.getElementsByClassName("active")[0].id;
    document.getElementById(old).classList.remove("active");
    document.getElementById(option.id).classList.add("active");
    // Ahora cambio los fields
    document.getElementById("field1").innerHTML = fields.get(option.id).split(' ')[0];
    document.getElementById("field2").innerHTML = fields.get(option.id).split(' ')[1];
    loadExampleData(option.id)
}

function loadExampleData(option) {
    document.getElementById('tablaDisplay').innerHTML = '';
    for (let x in exData.get(option)) {
        let data1 = exData.get(option)[x].split(";")[0];
        let data2 = exData.get(option)[x].split(";")[1];
        document.getElementById('tablaDisplay').innerHTML += `
        <tr id="crudItem${x}">
            <td class="crudItem${x}-d1">${data1}</td>
            <td class="crudItem${x}-d2">${data2}</td>
            <td>
                <img onclick="editItem(event)" class="crudEditarItem" id="${x}" src="assets/images/Editar.png">
                <img onclick="removeItem(event)" class="crudEliminarItem" id="${x}" src="assets/images/EliminarItem.png">
            </td>
        </tr>`;
    }
}

function removeItem(e) {
    document.getElementById("tablaDisplay").removeChild(document.getElementById(`crudItem` + e.target.id));
}

function editItem(e) {
    // Crud Mode
    crudMode = document.getElementsByClassName("active")[0].id;
    let edit;
    switch (crudMode) {
        case "usuarios":
            edit = prompt("Ingrese el nuevo nombre de Usuario:");
            if (edit != null || edit != "") {
                document.getElementsByClassName(`crudItem${e.target.id}-d1`)[0].innerText = edit;
            }
            break;
        case "envios":
            edit = prompt("Ingrese el nuevo Destino:");
            if (edit != null || edit != "") {
                document.getElementsByClassName(`crudItem${e.target.id}-d2`)[0].innerText = edit;
            }
            break;
        case "pedidos":
            edit = prompt("Ingrese el nuevo estado del Pedido:");
            if (edit != null || edit != "") {
                document.getElementsByClassName(`crudItem${e.target.id}-d2`)[0].innerText = edit;
            }
            break;
        default:
            alert("¡Input inválido!");
    }
}
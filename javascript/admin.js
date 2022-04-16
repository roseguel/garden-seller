function changeCrudMode(option) {
    const fields = new Map([['usuarios', 'Usuario Correo'], ['envios', 'ID Destino'], ['pedidos', 'ID Estado']]);
    let old = document.getElementsByClassName("active")[0].id;
    document.getElementById(old).classList.remove("active");
    document.getElementById(option.id).classList.add("active");
    // Ahora cambio los fields
    document.getElementById("field1").innerHTML = fields.get(option.id).split(' ')[0];
    document.getElementById("field2").innerHTML = fields.get(option.id).split(' ')[1];
    loadExampleData(option.id)
}

function loadExampleData(option) {
    const exData = new Map([
        ['usuarios', ['Moonie;moonie@gmail.com', 'Wacoldo;wacoldo@live.cl', 'Euclides;euclides@microsoft.com']],
        ['envios', ['10;Puente Alto, Santiago', '20;Los Copihues, Talcahuano', '30;Centinela 1, Talcahuano']],
        ['pedidos', ['10;Enviado', '20;En Recorrido', '30;Confirmando']]
    ]);
    document.getElementById('tablaDisplay').innerHTML = '';
    for (let x in exData.get(option)) {
        let data1 = exData.get(option)[x].split(";")[0];
        let data2 = exData.get(option)[x].split(";")[1];
        document.getElementById('tablaDisplay').innerHTML += `
        <tr>
            <td>${data1}</td>
            <td>${data2}</td>
            <td>
                <a href="#" role="button" class="btn btn-warning btn-md">
                    <i class="fa-solid fa-gear text-light"></i>
                </a>
                <a href="#" role="button" class="btn btn-danger btn-md">
                    <i class="fa-solid fa-trash-can text-light"></i>
                </a>
            </td>
        </tr>`;
    }
}
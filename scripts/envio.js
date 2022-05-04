function cargarCiudades() {
    document.getElementById("region").innerHTML = ``;
    var regiones = {
        "url": "https://countriesnow.space/api/v0.1/countries/states",
        "method": "GET",
        "timeout": 0,
    };

    $.getJSON(regiones).done(function (response) {
        pais = document.getElementById("pais").value;
        paisCode = 0;
        for (let x = 0; x < response.data.length; x++) {
            if (response.data[x].name == pais) {
                paisCode = x;
                break;
            }
        }
        for (let x = 0; x < response.data[paisCode].states.length; x++) {
            let htmlxd = `<option value="${response.data[paisCode].states[x].name}">${response.data[paisCode].states[x].name}</option>`
            document.getElementById("region").innerHTML += htmlxd;
        }
    });
}

function cargarComunas() {
    document.getElementById("comuna").innerHTML = ``;
    var comunas = {
        "url": "https://countriesnow.space/api/v0.1/countries",
        "method": "GET",
        "timeout": 0,
    };

    $.getJSON(comunas).done(function (response) {
        pais = document.getElementById("pais").value;
        paisCode = 0;
        for (let x = 0; x < response.data.length; x++) {
            if (response.data[x].country == pais) {
                paisCode = x;
                break;
            }
        }
        for (let x = 0; x < response.data[paisCode].cities.length; x++) {
            let htmlxd = `<option value="${response.data[paisCode].cities[x]}">${response.data[paisCode].cities[x]}</option>`
            document.getElementById("comuna").innerHTML += htmlxd;
        }
    });
}
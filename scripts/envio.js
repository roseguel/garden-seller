function cargarCiudades() {
    document.getElementById("ciudad").innerHTML = ``;
    var ciudades = {
        "url": "https://countriesnow.space/api/v0.1/countries/states",
        "method": "GET",
        "timeout": 0,
    };

    $.getJSON(ciudades).done(function (response) {
        paisCode = 0;
        for (let x = 0; x < response.data.length; x++) {
            if (response.data[x].name.toLowerCase() == "chile") {
                paisCode = x;
                break;
            }
        }
        for (let x = 0; x < response.data[paisCode].states.length; x++) {
            let htmlxd = `<option value="${response.data[paisCode].states[x].name}">${response.data[paisCode].states[x].name}</option>`
            document.getElementById("ciudad").innerHTML += htmlxd;
        }
        document.getElementById("ciudad").innerHTML += `<option selected>Region</option>`;
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
        paisCode = 0;
        for (let x = 0; x < response.data.length; x++) {
            if (response.data[x].country.toLowerCase() == "chile") {
                paisCode = x;
                break;
            }
        }
        for (let x = 0; x < response.data[paisCode].cities.length; x++) {
            let htmlxd = `<option value="${response.data[paisCode].cities[x]}">${response.data[paisCode].cities[x]}</option>`
            document.getElementById("comuna").innerHTML += htmlxd;
        }
        document.getElementById("comuna").innerHTML += `<option selected>Comuna</option>`;
    });
}
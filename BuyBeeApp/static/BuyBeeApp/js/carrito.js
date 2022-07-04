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
        document.getElementById("ciudad").innerHTML += `<option selected value="default">Region</option>`;
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
        document.getElementById("comuna").innerHTML += `<option selected value="default">Comuna</option>`;
    });
}

function validarForm(e) {
    if (document.getElementById("ciudad").value == 'default') {
        e.preventDefault();
        document.getElementById("error-envio").style.display = "flex";
        document.getElementById("error-envio-msg").innerText = "Por favor selecciona una ciudad válida para el Envio";
        return false;
    }
    if (document.getElementById("comuna").value == 'default') {
        e.preventDefault();
        document.getElementById("error-envio").style.display = "flex";
        document.getElementById("error-envio-msg").innerText = "Por favor selecciona una comuna válida para el Envio";
        return false;
    }
    if (document.getElementById("metodo_pago").value == 'default') {
        e.preventDefault();
        document.getElementById("error-envio").style.display = "flex";
        document.getElementById("error-envio-msg").innerText = "Por favor selecciona un método de Pago Válido";
        return false;
    }
}
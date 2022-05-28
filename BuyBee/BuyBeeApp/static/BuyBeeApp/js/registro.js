function chequearContraseña(e) {
    if (document.getElementById("contra").value != document.getElementById("contra2").value) {
        document.getElementById("labelSubmitRegistrar").style.display = "flex"
        return false;
    }
}

function formatearRut(blur) {
    if (blur) {
        rut = document.getElementById("inputRut").value
        /* Valido via RegEx si el rut cumple con el formato indicado. */
        formateado = rut.search("(.|..)\....\....-[0-9(k)]");
        if (formateado < 0) {
            rut = rut.includes(".") || rut.includes("-") ? rut.replace(".", "").replace("-", "") : rut;
            if (rut.length == 8 || rut.length == 9) {
                /* Añado de forma rápida los guiones y puntos al Rut. */
                rut = rut.length == 8 ? rut.slice(0, 1) + "." + rut.slice(1, 4) + "." + rut.slice(4, 7) + "-" + rut.slice(7) : rut.slice(0, 2) + "." + rut.slice(2, 5) + "." + rut.slice(5, 8) + "-" + rut.slice(8);
                document.getElementById("inputRut").value = rut;
            } else {
                document.getElementById("labelSubmitConfirmarRegistro").append("El rut debe tener 9 a 10 digitos")
                document.getElementById("labelSubmitConfirmarRegistro").style.display = "flex";
            }
        }
    } else {
        document.getElementById("labelSubmitConfirmarRegistro").removeChild(document.getElementById("labelSubmitConfirmarRegistro").lastChild)
        document.getElementById("labelSubmitConfirmarRegistro").style.display = "none";
    }
}

function validarRegistroPersonal() {
    /* Valido via RegEx si el rut cumple con el formato indicado. */
    rut = document.getElementById("inputRut").value
    if (rut.search("(.|..)\....\....-[0-9(k)]") < 0) {
        return false;
    }
}
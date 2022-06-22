# Preguntenle al Ariel antes de editar las funciones por favor.

def formatNumberToPrice(numeroRaw):
    numero = ""
    for x in range(len(str(numeroRaw))):
        numero += (str(numeroRaw)[::-1])[x]
        if (x + 1) % 3 == 0:
            numero += "."
    numero = numero[0:-1] if numero.endswith(".") else numero
    return numero[::-1]

def shrinkProdName(nombreRaw, limite):
    return nombreRaw[:limite] + "..." if len(nombreRaw) > limite else nombreRaw
    #if len(nombreRaw) > 10:
    #    nombre = nombreRaw[:10]
    #    nombre += "..."
    #else:
    #    nombre = nombreRaw
    #return nombre

def normalizeName(nombreRaw, apellidoRaw):
    nombre = nombreRaw.split()[0] if " " in nombreRaw else nombreRaw
    apellido = apellidoRaw.split()[0] if " " in apellidoRaw else apellidoRaw
    return f"{nombre} {apellido}"
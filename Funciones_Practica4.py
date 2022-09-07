

# Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
# - Agregar pasajeros a la lista de pasajeros
# - Agregar ciudades a la lista de ciudades
# - Dada la CLAVE de un pasajero, ver a que ciudad viaja
# -  Dada la CIUDAD, mostrar la cantidad de pasajeros que viajan a esa ciudad
# - Dada la CLAVE de un pasajero, ver a que ESTADO viaja
# -  Dado un Estado, mostrar cuantos pasajeros viajan a ese Estado
# - Salir del programa
def agregar_pasajeros(pasajeros,ciudades):
    nombre = input("Dame el nombre del pasajero ")
    clave = int(input("Clave del pasajero "))
    print("Lista de ciudades ,\n",ciudades)
    ciudad =(input("Escoge sobre las distintas ciudades "))
    pasajero = (nombre, clave, ciudad)
    pasajeros.append(pasajero)
    print("Pasajeros: ", pasajeros)



def agregarCiudad(ciudades):
    nom_ciudad = input("Nombre de la ciudad")
    nom_estado = input("Nombre del estado")
    ciudad = (nom_ciudad, nom_estado)
    ciudades.append(ciudad)
    print("Ciudades ",ciudades)



def buscarPasajero(pasajeros):
    clave_buscar = int(input("Dame la clave del pasajero a buscar "))
    ban = False


    for x in pasajeros:
        nombre,clave,estado = x
        if (clave == clave_buscar):
            print("Pasajero encontrado:\n", x)
            ban = True
    if not ban:
        print("Pasajero no encontrado")


def pasajeros_Ciudad(ciudades,pasajeros):
    ciudad_buscar = input("Dame la ciudad ")
    ban = False
    for x in ciudades:
        ciudad,estado = x
        if ciudad == ciudad_buscar:
           for y in pasajeros:
               nombre,clave,destino = y
               if destino == ciudad_buscar:
                   print(y,"\t")
                   ban = True
    if not ban:
        print("No se encontraron pasajeros")
def estado_clave(pasajeros):
    clave_buscar = int(input("Clave del pasajero a buscar "))
    bandera = False
    for x in pasajeros:
        nombre,clave,destino =  x
        if clave == clave_buscar:
            print("Pasajero encontrado\n", x)
            print("Destino: ",destino)
            bandera = True
    if not bandera:
        print("No se encontro el pasajero")
def pasajeros_Estado(pasajeros,ciudades):
    estado_buscar = input("Dame el Estado ")
    ban = False
    contador = 0
    for x in ciudades:
        ciudad,estado = x
        if estado == estado_buscar:
            print("Encontro el estado")
            for y in pasajeros:
                nombre,clave,destino = y
                if destino == ciudad:
                    print(y)
                    contador+=1
    print("Total de pasajeros: ", contador)

    # for x in ciudades:
    #     if x == estado:
    #        for y in pasajeros:
    #            if y == estado:
    #                print(y,"\t")
    #                ban = True
    # if not ban:
    #     print("No se encontraron pasajeros")



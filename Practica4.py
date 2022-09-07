#
# tupla1=tuple()
# tupla2=()
# tupla3=(2,"pepe",True,89)
#
# print(tupla3)
#
# for e in tupla3:
#     print(e)
# grupo_a=("Luis","Carmen","Pepe")
# grupo_b=("Jose","Hector","Brian")
# grupo_c=(grupo_a,grupo_b)
# print(grupo_c)
#
# lista = ['A','B', 'C']
# tupla_letras = tuple(lista)
# print(tupla_letras)
#
# alumno = (184204, "Pepe")
# control,nombre = alumno
# print("Control: ", control, " Nombre: ", nombre)
#
# print(grupo_a.count("Carmen"))
from Funciones_Practica4 import *

pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]
# Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
# - Agregar pasajeros a la lista de pasajeros
# - Agregar ciudades a la lista de ciudades
# - Dada la CLAVE de un pasajero, ver a que ciudad viaja
# - AQUI Dada la CIUDAD, mostrar la cantidad de pasajeros que viajan a esa ciudad
# - Dada la CLAVE de un pasajero, ver a que ESTADO viaja
# - Dado un Estado, mostrar cuantos pasajeros viajan a ese Estado
# - Salir del programa



salir = False
while salir==False:
    opcion = int(input("Seleccione una opcion \n1.Agregar pasajero\t2.Agregar Ciudades\t3.Busqueda por clave\t4.Cantidad de pasajeros\t5.Buscar por clave el destino \t6.Pasajeros por Estado\t 7.Salir\n"))
    match opcion:
        case 1:
            agregar_pasajeros(pasajeros,ciudades)
        case 2:
            agregarCiudad(ciudades)
        case 3:
            buscarPasajero(pasajeros)
        case 4:
            pasajeros_Ciudad(ciudades, pasajeros)
        case 5:
            estado_clave(pasajeros)
        case 6:
            pasajeros_Estado(pasajeros,ciudades)
        case 7:
            salir = True
        case default:
            print("Dato invalido")


alumnos =[[18420451,"Jose",80],[18420452,"Hector",89],[18420493,"Aylin",99],[18420453,"Brian",70] ]
# print(alumnos)
# print(alumnos[1])
# promedios = []
# for alum in alumnos:
#     promedios.append(alum[-1])
# print(promedios)
# promedios2=[alum[-1] for alum in alumnos]
# print(promedios2)
# 1.Menu principal que tenga insertar eliminar actualizar, imprimir y salir y opcion no valida
lista = []
def buscar(nom):
    for x in lista:
        if(nom == x):
            return True
        return False
def imprimir():
    print(lista)


def insertar():
    nombre = input("Nombre del Alumno: ")
    lista.append(nombre)

def actualizar(nom):
    for x in lista:
        if (nom == x):
            nombre = input("Dame el nuevo nombre ")
            lista.insert(lista.index(nom), nombre)
            lista.remove(nom)

def eliminar(nom):
    lista.remove(nom)







salir = False

while salir==False:
    opcion = int(input("Seleccione una opcion \n1.Insertar\t2.Eliminar\t3.Actualizar\t4.Imprimir\t5.Salir\n"))
    match opcion:
        case 1:
            insertar()
        case 2:
            nombr = input("Nombre de la persona a eliminar ")
            eliminar(nombr)
        case 3:
            nombr = input("Nombre de la persona a actualizar ")
            actualizar(nombr)
        case 4:
            imprimir()
        case 5:
            salir = True
        case default:
            print("Opcion no valida")


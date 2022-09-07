'''
Tema: conjuntos
Fecha: 05 de septiembre del 2022
Autor: Leonardo Martínez González
'''
import json
# 1. Definición. en Python es utilizado para trabajar con conjuntos de elementos.
#    La principal característica de este tipo de datos es que es una colección cuyos elementos
#    no guardan ningún orden y que además son únicos.
#    los principales usos de esta clase se usan para conocer si un elemento pertenece o no
#    a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).



# 2. Creación. Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {},
#    o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable
#    (como una lista, una tupla, una cadena …).

# conjunto = {1,2,3,4,5}
# print(conjunto)
# conjunto_2= set([i for i in range(0,11,2)])
# print(conjunto_2)
#
# #    Usando la función forezenset. es inmutable y su contenido no puede ser modificado
# #    una vez que ha sido inicializado
# c4 = frozenset(chr(i) for i in range(65,90) )
# print(c4)
# #    Los elementos repetidos se eliminan
#
#
# # 3. Para acceder a los elementos de un conjunto. Dado que los conjuntos son colecciones
# #    desordenadas, en ellos no se guarda la posición en la que son insertados los elementos
# #    como ocurre en los tipos list o tuple. Es por ello que no se puede acceder a los elementos
# #    a través de un índice.
#
#
#
# # 4. Añadir elementos: con el método add() ó con el método update()
# #    Agregar el numero 8 al conjunto c
# conjunto_2.add('Amonos')
# print(conjunto_2)
#
# #    Agregar varios elementos al conjunto
# conjunto_2.update([20,30,40])
# conjunto_2.update(conjunto)
# print(conjunto_2)
#
# # 5. Eliminar elementos del conjunto: discard(elemento), remove(elemento), pop() y clear()
# #    discard(elemento) y remove(elemento) son muy parecidos, solo que remove lanza una excepcion KeyError
# #    en caso de no existir el elemento
# conjunto_2.discard('Amonos')
# conjunto_2.discard(100)
# # conjunto_2.remove(100)
# print(conjunto_2)
#
#
#
# #     pop() devuelve un elemento aleatorio y lo elimina, si el conjunto esta vacio lanza una
# #     excepcion KeyError.
# # conjunto.pop()
# # conjunto.pop()
# # print(conjunto)
#
#
# #    El método clear() elimina todos los elementos del conjunto
# conjunto.clear()
# print(conjunto)
#
# #    Número de elementos en un conlunto con la función len()
# print(len(conjunto_2))
#
#
# #    Verificar si un elemento esta dentro de un conjunto
#
# print(10 in conjunto_2)
# print(50 in conjunto_2)
#

# ************************ Operaciones con conjuntos
# cp = {i for i in range(0,21,2)}
# ci = {i for i in range(1,21,2)}
#
# print("Pares: ",cp)
# print("Impares: ",ci)
# # 1. Union  ( | )
# union = cp | ci
# print("Union: ",union)
#
# # 2. Intersección ( & )
# inter = cp & ci
# print("Interseccion: ",inter)
#
# # 3. Diferencia ( - )
# difer = cp - ci
# print("Diferencia: ",difer)
#
#
# # 4. Diferencia simétrica ( ^ ). es el conjunto que contiene los elementos de A y B
# #    que no son comunes.
# difers = cp ^ ci
# print("Diferencia Simetrica: ",difers)
#
#
# # 5. Inclusión de conjuntos.  Se utiliza el operador <= para comprobar si un conjunto A
# #    es subconjunto de B y el operador >= para comprobar si un conjunto A es superconjunto de B.
# print(cp<=ci)
#
# # 5. Conjuntos disjuntos. Dos conjuntos A y B son disjuntos si no tienen elementos en común,
# #    es decir, la intersección de A y B es el conjunto vacío.
# print(cp.isdisjoint(ci))
#
# # 6. Igualdad de conjuntos. En Python dos conjuntos son iguales si y solo si todos los elementos
# #    de un conjunto están contenidos en el otro. Esto quiere decir que cada uno es un subconjunto
# #    del otro.
# print(cp == ci)

'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"",
                "Promedio":
            },
            {
                "Nombre":"",
                "Promedio":
            },
            . . . 
        ],
        "Promedio general": 
   }


'''
estudiantes = open("Estudiantes.prn","r")
conjunto_estudiantes= set()
lista_estudiantes = estudiantes.readlines()
for x in lista_estudiantes[0:]:
    estudiante = x.split("\n")
    no_control = estudiante[0][0:8]
    nombre = estudiante[0][8:]
    tupla = (no_control, nombre)
    conjunto_estudiantes.add(tupla)
print(conjunto_estudiantes)

materias = open("Kardex.txt","r")
conjunto_materias= set()
lista_materias = materias.readlines()
for x in lista_materias[0:]:
    materia = x.split("\n")
    datos = materia[0].split('|')
    no_control2 = datos[0]
    nombre_materia = datos[1]
    calificacion = int(datos[2])
    conjunto_materias.add((no_control2,nombre_materia,calificacion))
print(conjunto_materias)

materias=[]
num_control_b = input("Dame el numero de control a buscar ")
prom = 0
contador = 0
bandera = False
for x in conjunto_estudiantes:
    if x[0] == num_control_b:
        alumno = {}
        print("Numero de control encontrado")
        alumno['Nombre'] = x[1]
        for y in conjunto_materias:
            if y[0]== x[0]:
                materia = {}
                materia["Nombre"] = y[1]
                materia["Promedio"] = y[2]
                materias.append(materia)
                prom += int(y[2])
        alumno['Promedio General'] = int(prom / len(materias))
        alumno['Materias'] = materias
        bandera = True
if not bandera:
    print("Alumno no encontrado")
else:
    print(alumno)
    with open('alumno.json', 'w') as file:
        json.dump(alumno, file, indent=4)















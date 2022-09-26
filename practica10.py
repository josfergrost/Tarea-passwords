'''
Tema: Funciones
Fecha: 22 de septiembre del 2022
Autor: Leonardo Martínez González
Link: https://www.youtube.com/watch?v=_nAuo8JsAcM  *args y **kwargs
Link: https://www.youtube.com/watch?v=8JpE9CwfOJc funciones lambda
'''

'''
Paso de Parámetros por valor o referencia 
'''
# lista=['Juan','Pedro','Jose','Brian']
# def imprimir_lista(x):
#     for nom in x:
#         print(nom)
# imprimir_lista(lista)
'''
Funciones con argumentos con valor por defecto
'''
# import mysql.connector
# productos = []
# def conectarmysql(host,user,pwd,bd):
#
#     try:
#         conexion = mysql.connector.connect(host=host,user=user,password=pwd,database=bd)
#     except Exception as error:
#         print("ERROR: ",error)
#     else:
#         return conexion
#     #     try:
#     #         ccursor.execute("SELECT id,nombre,precio from productos")
#     #     except mysql.connector.errors.ProgrammingError as err:
#     #         print("Error en la consulta: ",err)
#     #     else:
#     #         for reg in ccursor:
#     #             clave,nombre,precio = reg
#     #             producto = {}
#     #             producto['id'] = clave
#     #             producto['nombre']= nombre
#     #             producto['precio'] =str(precio)
#     #             productos.append(producto)
#     #
#     #
#     #
#     #     finally:
#     #         ccursor.close()
#     #         conexion.close
#
#     def consulta(conexion,cadena):
#         try:
#             cursor = conexion.cursor()
#             cursor.execute()
#         except mysql.connector.errors.ProgrammingError as err:
#             print("Error en la consulta: ",err)
#         else:
#             for reg in cursor:
#                 clave,nombre,precio = reg
#                 producto = {}
#                 producto['id'] = clave
#                 producto['nombre']= nombre
#                 producto['precio'] =str(precio)
#                 productos.append(producto)
#
#
#
#         finally:
#                      cursor.close()
#                      conexion.close
#
#     consulta(conectarmysql("localhost", "root", "", "opensource"),"SELECT id,nombre,precio from productos")
'''
Funciones que retornan varios valores
'''
def suma(a,b):
    return a+b,a,b
d,e,f = suma(10,2)
print(d)
print(e)
print(f)
print(suma(2,10))


'''
Funciones lambda o anónimas, son de una sola linea, solo las ocupamos una sola vez.
1. Definir una función lambda con un ejemplo
saludar = lambda nombre: return f"Hola {nombre}"
2. Llamada de otras funciones dentro de una función lambda
3. Ordenar una lista
3. Pasarlas como parámetros a filter y map. 
   filter filtra elementos, toma dos parámetros: (una_funcion, lista)
   map por cada elemento de la lista llama al elemento y regresa el elemento ya modificado
'''
# lista=[10,20,19,18,15,16,15,29]
# def cuadrado(num):
#     return num*num
# cuad = lambda x:cuadrado(x)
# for e in lista:
#     print(f"El cuadrado de {e} es: {cuad(e)} ")

# Si es menor de edad regresar  edad = a 18 de lo contrario regresar la edad

# Regresar los estudiantes aprobados, de lo contrario regresar un False
lista = [(700,'Jose',18,98.0),
         (300,'Juan',17,80.0),
         (200,'Pepe',15,60.0),
         (100,'Israel',20,70.0)]
print(lista)
lista.sort(key=lambda t:t[3])
print(lista)


'''
Argumentos arbitrarios. Se utiliza cuando no sabemos la cantidad de argumentos
que vamos a recibir
'''


'''
 y keyword arguments **kwargs
'''
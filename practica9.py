'''
Tema: Gestión de excepciones
Fecha: 19 de septiembre del 2022
Autor: Leonardo Martínez González
'''
from logging import exception
import mysql.connector
#    En algunas ocasiones nuestros programas pueden fallar ocasionando su detención.
#    Ya sea por errores de sintaxis o de lógica, tenemos que que ser capaces de detectar esos
#    momentos y tratarlos debidamente para prevenirlos.

#    Los errores detienen la ejecución del programa y tienen varias causas. Para poder estudiarlos
#    vamos a provocar algunos intencionadamente.
#    Tipos: Errores de sintaxis, de nombre y semánticos.

# 1. Excepciones: Las excepciones son bloques de código que nos permiten continuar
#    con la ejecución de un programa pese a que ocurra un error.

#    Se trata de una forma de controlar el comportamiento de un programa
#    cuando se produce un error.

# 2. Sintaxis:
'''
try:
        # Intenta ejecutar la instrucion(es)
    except:
        # Si ocurre un error aqui se trata
    else:
        # Si entra al bloque try se ejecuta este bloque de código
    finally: 
        # Siempre se ejecutara este código
'''

# Los ejemplos más comunes que podemos nombrar de excepciones:
#
# 1. Tratar de convertir a entero un string que no contiene valores numéricos. (ValueError)
# 2. Tratar de dividir por cero.
# 3. Abrir un archivo de texto inexistente o que se encuentra bloqueado por otra aplicación.
# 4. Conectar con un servidor de bases de datos que no se encuentra activo.
# 5. Acceder a subíndices de listas o tuplas inexistentes.

'''
# Ejemplo 1: Calcular si un  numero es PAR o IMPAR, introducir el dato desde teclado
'''
# while True:
#     try:
#         numero = int(input("Dame el numero"))
#
#         if numero % 2 ==0:
#            print("Numero PAR:",numero)
#         else:
#             print("Numero IMPAR:", numero)
#     except ValueError:
#         print("Error en el valor, debe ser un numero")
#     else:
#         print(f"El numero es: {numero}")
#         break





'''
# 2. Tratar de dividir por cero. (ZeroDivisionError)
'''
#
# while True:
#     try:
#         a = int(input("Dame un valor"))
#         b = int(input("Cambia el valor del denominador"))
#         c = a / b
#     except ZeroDivisionError:
#         print("Error en el valor, division entre cero")
#     except ValueError:
#         print("Error en el valor")
#     else:
#         print(f"El resultado de la division es: {c}")
#         break
#


'''
# 3. Abrir un archivo de texto inexistente.
#    (FileNotFoundError)
'''

# try:
#     PATH="C:/Users/josfe/PycharmProjects/Unidad2/"
#     ARCHIVO = "alumnos.json"
#     archivo = open(PATH+ARCHIVO, "r")
# except FileNotFoundError:
#     print(f"No existe el archivo buscado {ARCHIVO}")
#
# else:
#     print(ARCHIVO,f"Tiene {len(archivo.readlines())}")
# # finally:
#     # if not archivo.closed:
#     #     archivo.close()
#



'''
# 4. Conectar con un servidor de bases de datos de MySQL que no se encuentra activo.
#      Importar mysql-connector
#      pip install mysql-connector
'''
# try:
#     conexion = mysql.connector.connect(host="localhost",user="root",passwd="", database ="topicos")
# except mysql.connector.errors.InterfaceError:
#     print("No me puedo conectar martha")
# else:
#     cursor1 = conexion.cursor()
#     try:
#         cursor1.execute("Select producto for productos where id = 2")
#     except mysql.connector.errors.ProgrammingError:
#         print("Nimodillo, nomas no lo encuentro Martha")
#     else:
#         print("No existe el campo o nombre de tabla")



'''
# 5. Acceder a subíndices de listas o tuplas inexistentes.
#    Utilizar el mismo ejemplo anterior
'''
# tuplilla = [10, 20, 30, 40, 50]
# while True:
#     try:
#         len = int(input("Dame el rango "))
#         num = tuplilla[len]
#     except IndexError:
#         print("Estas fuera del rango mongolito")
#     else:
#         print(f"El numero es: {num}")
#         break

'''
# ========== Generación manual de excepciones con la declaración raise en Python ==========
Podemos usar la declaración raise dentro de una declaración if
para generar una excepción específica si ocurre una condición específica. 
'''

'''
#1. Generar una excepción ZeroDivisionError
'''
while True:
    try:
        a = int(input("Dame un valor"))
        b = int(input("Cambia el valor del denominador"))
        c = a / b
    except ZeroDivisionError:
        print("Error en el valor, division entre cero")
    except ValueError:
       print("Error en el valor")
    else:
       print(f"El resultado de la division es: {c}")
       break


'''
# 2. Generar una excepción TypeError si var no es una variable de tipo entero.
'''
try:
    c = int(input("Dame un numero"))
except TypeError:
    print(f"Esto no es un numero {c}")
else:
    print(f"El numero es: {c}")



'''
# 3. Generar una excepción ValueError si month es mayor que 12
'''
try:
    dia = input("Dia de nacimiento")
    mes = int(input("Dame el mes en valor numerico"))
    if mes > 12:

    year = int(input("Dame el año en valor numerico"))
except ValueError:
    print("El mes es mayor a 12")
'''
# ERRORES PERSONALIZADOS CON assert
'''


'''
# PROPAGACIÓN DEL ERROR con raise
'''

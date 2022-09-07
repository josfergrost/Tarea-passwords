'''
Tema: Aplicación de estructuras de Python: archivos, JSON, cifrado de contraseñas
Fecha: 06 de septiembre del 2022
Autor: Leonardo Martínez González
Continuación de la práctica 6
'''
import random
import bcrypt
'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes. (5) 10 min.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"Base de Datos",
                "Promedio":85
            },
            {
                "Nombre":"Inteligencia Artificial",
                "Promedio":100
            },
            . . . 
        ],
        "Promedio general": 98.4
   }
   

4. Regresar una lista de JSON con las materias de un estudiante, el formato es el siguiente:
[
    {"Nombre": "Contabilidad Financiera"},
    {"Nombre": "Dise\u00f1o UX y UI"}, 
    {"Nombre": "Base de datos distribuidas"}, 
    {"Nombre": "Finanzas internacionales IV"}, 
    {"Nombre": "Analisis y dise\u00f1o de sistemas de informacion"}, 
    {"Nombre": "Microservicios"},
    {"Nombre": "Algoritmos inteligentes"}
]


5. Generar un archivo de usuarios que contenga el numero de control, éste será el usuario
   y se generará una contraseña de tamaño 10 la cual debe tener:
   A. Al menos una letra mayúscula 
   B. Al menos una letra minúscula
   C. Numeros
   D. Al menos UN carácter especial, considere ( @, #, $,%,&,_,?,! )

   Considere:
    - Crear un método para generar cada caracter
    - El codigo ascii: https://elcodigoascii.com.ar/
    - Encriptar la contraseña con bcrypt, se utiliza con node.js, react, etc. Para ello:
        * Descargue la libreria bcrypt con el comando: "pip install bcrypt" desde la terminal o desde PyCharm
        * Página: https://pypi.org/project/bcrypt/
        * Video:Como Cifrar Contraseñas en Python     https://www.youtube.com/watch?v=9tEovDYSPK4

   El formato del archivo usuarios.txt será:
   control contrasena contraseña_cifrada

6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que 
   indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
   {
        "Bandera": True,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
   }

   ó

   {
        "Bandera": False,
        "Usuario": "",
        "Mensaje": "No existe el Usuario"
   }

   ó

    {
        "Bandera": False,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Contraseña incorrecta"
   }


'''
import json
def estudiantes():
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
    return conjunto_estudiantes

def materias():
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
    return  conjunto_materias
# print(conjunto_materias)
#
# materias=[]
# num_control_b = input("Dame el numero de control a buscar ")
# prom = 0
# contador = 0
# bandera = False
# for x in conjunto_estudiantes:
#     if x[0] == num_control_b:
#         alumno = {}
#         print("Numero de control encontrado")
#         alumno['Nombre'] = x[1]
#         for y in conjunto_materias:
#             if y[0]== x[0]:
#                 materia = {}
#                 materia["Nombre"] = y[1]
#                 materia["Promedio"] = y[2]
#                 materias.append(materia)
#                 prom += int(y[2])
#         alumno['Promedio General'] = int(prom / len(materias))
#         alumno['Materias'] = materias
#         bandera = True
# if not bandera:
#     print("Alumno no encontrado")
# else:
#     print(alumno)
#     with open('alumno.json', 'w') as file:
#         json.dump(alumno, file, indent=4)

#4
def regresa_materias_control(control):
    listaMaterias = []
    for mat in materias():
        numcontrol,nom_mat,promedio = mat
        if control == numcontrol:
            listaMaterias.append({"Nombre":nom_mat})
    return listaMaterias
# num_control = input("Numero de control a buscar ")
# print(regresa_materias_control(num_control))

def generar_letra_mayuscula(): # regresa mayuscula una de la A a la Z
    return chr(random.randint(65, 90))
def generar_letra_minuscula():
    return chr(random.randint(97,122))
def generar_numeros():
    return chr(random.randint(48,57))
def generar_caracter_especial():
    lista_caracteres = ['@', '#', '$', '%', '&', '*', '!', '?', '_']
    caracter = lista_caracteres[random.randint(0,8)]
    return caracter
def generar_contra():
    clave = ""
    for i in range(0,10):
        numero = random.randint(1,5)
        if numero == 1:
            clave+=generar_letra_mayuscula()
        elif numero == 2:
            clave += generar_letra_minuscula()
        elif numero == 3:
            clave += generar_caracter_especial()
        elif numero == 4 or numero == 5:
            clave += generar_numeros()
    return clave
def cifrar_contra(passw):
    password = passw.encode('utf-8')
    # Hash the ecoded password and generate a salt:
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashedPassword

#generar el archivo de usuarios
def generar_archivo_usuarios():
    usuarios = open("Usuarios.txt", "w")
    tot_estudiantes = estudiantes()
    contador = 0
    for est in tot_estudiantes:
        control,nombre = est
        clave = generar_contra()
        clave_c = cifrar_contra(clave)
        registro = control + "|" + clave + "|" + str(clave_c,'utf-8') + "\n"
        usuarios.write(registro)
        contador += 1
        print(contador)
    print("Archivo generado")


#generar_archivo_usuarios()

# 6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que
#    indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
#    {
#         "Bandera": True,
#         "Usuario": "Leonardo Martínez González",
#         "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
#    }
#
#    ó
#
#    {
#         "Bandera": False,
#         "Usuario": "",
#         "Mensaje": "No existe el Usuario"
#    }
#
#    ó
#
#     {
#         "Bandera": False,
#         "Usuario": "Leonardo Martínez González",
#         "Mensaje": "Contraseña incorrecta"
#    }

def autenticar_usuario(usuario,password):
    bandera = False
    ban_usuario = False
    mensaje =""
    usuarios = open("Usuarios.txt", "r")
    conjunto_usuarios = []
    contador = 0
    users = usuarios.readlines()
    for us in users [0:]:
        linea = us.split("\n")
        separa = linea[0].split('|')
        user = separa[0]
        clave = separa[1]
        clave_c = separa[2]
        if usuario == user:
            ban_usuario = True
            break
    if ban_usuario :
        print("Se encontro el usuario.")
        if bcrypt.checkpw(password.encode('utf-8'),clave_c.encode('utf-8')):
            bandera = True
            usuario = user
            mensaje = "Bienvenido al sistema de verificacion de usuarios"

        else:
            bandera = False
            usuario = user
            mensaje = "Contraseña incorrecta"

    else:
        rev_usuario = {}
        bandera = False
        usuario = ""
        mensaje = "No se encontro el usuario"
    rev_usuario = {}
    rev_usuario['Bandera'] = bandera
    rev_usuario['Usuario'] = usuario
    rev_usuario['Mensaje'] = mensaje
    return json.dumps(rev_usuario, indent=4)


print(autenticar_usuario("18422451","It387F_$?F"))







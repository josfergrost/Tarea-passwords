lista = ["Juan", "Pedro", "Jose", "Hector", "Lucia"]
# print(lista[1])
for x in range(5):
    print(lista[x])

print(lista)

print("La longitud de la lista es "+str(len(lista)))
print(lista[-5])
print(lista[-5:-2])
lista.insert(1, 'Pepe')
print(lista)
lista.remove('Pedro')
print(lista)
print(lista[lista.index('Pepe')])
import random
rango=int(input("Numero de aleatorios para el arreglo "))
listilla = [random.randint(1, 100) for i in range(rango)]
print(listilla)
alumnos =[[18420451,"Jose",8.89],[18420452,"Hector",8.90],[18420493,"Aylin",9.90],[18420453,"Brian",7.0] ]
print(alumnos)
print(alumnos[1])
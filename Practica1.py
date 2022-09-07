#Listas
#26/Ago/22
# pendejos_lista=[]
# pendejos2=list()
# numeros=[3,4,5,6,7,10]
#  for i in numeros:
#      print(i)
#  nombres=["Pepe","Brian","Hector"]
#  for i in nombres:
#      print(i)
#
# print(numeros[6:0:-1])
lista = list()
x=0
while x<10:
    numero = int(input("Dame un numero "))
    lista.append(numero)
    x+=1
lista.sort()
print(lista)

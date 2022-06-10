import numpy as np
from numpy import random


arreglo1 = np.arange(10) 
cantidad = 0
total = 0

for n in range(10):
    num = random.randint(0,1001)
    arreglo1[n] = num

#Mostrar el arreglo
print(arreglo1)


#contar elementos pares
for i in range(10):
    if (arreglo1[i] % 2 == 0):
        cantidad = cantidad + 1

print(f"Cantidad de elementos pares: {cantidad}")


#suma de elementos impares
for x in range (10):
    if arreglo1[x]%2 != 0:
        total = total + arreglo1[x]

print(f"La suma de los impares es {total}")

#mostrar numeros primos
for i in range(10):
    contador = 0
    for n in range(1, arreglo1[i]+1):
        if arreglo1[i]%n == 0:
            contador = contador + 1

    if contador == 2:
        print(f"El numero {arreglo1[i]} es primo")            






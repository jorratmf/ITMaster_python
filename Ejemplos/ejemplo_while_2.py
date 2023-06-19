import random

#antes (para todos)
sumador = 0
contador = 0
numero = random.randint(0, 1000)
while numero != 0:

#durante (para cada dato)
    sumador += numero
    contador += 1
    numero = random.randint(0, 1000)
    
#despues (totales)
print(f"La cantidad de numeros es: {contador}\nLa suma es: {sumador}")
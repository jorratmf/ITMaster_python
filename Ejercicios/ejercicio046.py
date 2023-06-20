## Ejercicio 046

### Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.

cant = int(input("Ingrese la cantidad de números enteros: "))
numeros = []
for i in range(cant):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

maximo = max(numeros)
posicion = numeros.index(maximo)

print("El mayor número es", maximo, "y aparece en la posición", posicion)
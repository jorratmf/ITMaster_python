## Ejercicio 043
### Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100, y muestre la cantidad de números ingresados.

suma = 0
cantidad = 0

while suma <= 100:
    num = int(input("Ingrese un número entero: "))
    suma += num
    cantidad += 1

print("La cantidad de números ingresados es:", cantidad)
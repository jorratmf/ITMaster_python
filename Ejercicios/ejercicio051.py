## Ejercicio 051
### Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.
### La computadora debe mostrar el número máximo y el número mínimo.

numeros = []
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    numeros.append(num)

if len(numeros) > 0:
    print("El número máximo es:", max(numeros))
    print("El número mínimo es:", min(numeros))
else:
    print("No se ingresaron números.")
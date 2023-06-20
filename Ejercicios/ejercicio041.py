## Ejercicio 041
### Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el máximo.

max_int = 0

while True:
    num = int(input("Introduzca un número entero (0 para detener la entrada): "))
    if num == 0:
        break
    if num > max_int:
        max_int = num

print("El número máximo ingresado es:", max_int)
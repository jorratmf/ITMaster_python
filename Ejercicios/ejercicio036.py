## Ejercicio 036
### Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operacion a realizar (+, -, *, /): ")

if operacion == '+':
    print(num1 + num2)
elif operacion == '-':
    print(num1 - num2)
elif operacion == '*':
    print(num1 * num2)
elif operacion == '/':
    if num2 == 0:
        print("ERROR")
    else:
        print(num1 / num2)
else:
    print("Operacion invalida")
## Ejercicio 048
### Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. La computadora debe mostrar el resultado para la operación ingresada. Considerar que no se puede dividir por cero. Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.

operacion = None
while operacion != 'F':
    operacion = input("Ingrese la operación a realizar ('+', '-', '*', '/', 'F'): ")
    if operacion == '+':
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        print(f'{n1} + {n2} = {n1 + n2}')
    elif operacion == '-':
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        print(f'{n1} - {n2} = {n1 - n2}')
    elif operacion == '*':
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        print(f'{n1} * {n2} = {n1 * n2}')
    elif operacion == '/':
        n1 = int(input("Ingrese el primer número: "))
        n2 = int(input("Ingrese el segundo número: "))
        print(f'{n1} / {n2} = {n1 / n2}')
        if n2 == 0:
            print("No se puede dividir por cero")   
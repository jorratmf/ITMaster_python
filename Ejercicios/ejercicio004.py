# Ejercicio 004

## Escribir un programa que solicite al usuario ingresar tres numeros enteros.El programa debe mostrar por pantalla el resultado de sumar los tres numeros de la siguiente manera: "[numero1] + [numero2] + [numero3] = [suma]".

### Ejemplo: Si el usuario ingresa 1, 2 y 3, el programa debe mostrar por pantalla: "1 + 2 + 3 = 6".

print("Ingrese tres numeros enteros: ")
n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese un numero: "))
n3=int(input("Ingrese un numero: "))
suma=n1+n2+n3

print(f'{n1} + {n2} + {n3} = {suma}')
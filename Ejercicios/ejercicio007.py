## Ejercicio 007

### Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:
### a. Multiplicado por 10. (utilizar el operador *)
### b. Dividido por 10. (utilizar el operador /)
### c. Elevado al cuadrado. (utilizar el operador **)
### Cada resultado debe mostrarse en una línea distinta.
'''
Ejemplo de ejecución:

    Ingrese un número entero: 5
    5 * 10 = 50
    5 / 10 = 0.5
    5 ** 2 = 25
'''

print("Ingrese un numero entero: ")
n=int(input())
producto=n*10
division=n/10
potencia=n**2

print(f'Producto de {n}*10 = {producto}')
print(f'División de {n}/10 = {division}')
print(f'Potencia de {n}^2 = {potencia}')
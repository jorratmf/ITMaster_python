## Ejercicio 020

### Escribir un programa que permita ingresar dos cadenas de caracteres e indicar si son iguales o distintas.

n1 = int(input('Numero 1:'))
n2 = int(input('Numero 2:'))

if n1 > n2:
    print('Mayor:',n1)
else:
    if n1 < n2:
        print('Mayor:',n2)
    else:
        print('Son iguales')
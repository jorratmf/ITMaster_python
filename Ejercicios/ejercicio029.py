"""
Ejercicio 029
Escribir un programa que permita Ingresar las notas de los dos parciales de 
un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la 
nota no esta entre 0 y 10, debe informar un error.
Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""

import random

# nota1= int(input("Nota 1: "))
# nota2 = int(input("Nota 1: "))


nota1 = random.randint(0,10)
nota2 = random.randint(0,10)
# if nota1 >= 0 and nota2 >= 0 and nota1 <= 10 and nota2 <= 10:
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    if nota1 >= 7 and nota2 >= 7:
        print(f"Notas: [{nota1},{nota2}] ==> Promociona")
    elif nota1 >= 4 and nota2 >= 4:
        print(f"Notas: [{nota1},{nota2}] ==> Aprueba")
    else:
        print(f"Notas: [{nota1},{nota2}] ==> Recupera")
else:
    print(f"Notas: [{nota1},{nota2}] ==> Error en las notas")




## Ejercicio 047
### Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.  
### La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.

nota = -1
while nota < 0 or nota > 10:
    nota = float(input("Ingrese la nota del examen: "))
    if nota < 0 or nota > 10:
        print("La nota ingresada debe estar entre 0 y 10.")
print("La nota ingresada es:", nota)
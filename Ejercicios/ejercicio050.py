## Ejercicio 050

### Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.  
### La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
'''
- Las notas 1 y 3 no usan nunca.  
- La nota 0 se reserva para los ausentes.  
'''
### Las notas válidas pueden ser un 2 o un valor entre 4 y 10.

nota = -1
while (nota < 0) or (nota == 1) or (nota == 3) or (nota > 10):
    nota = float(input("Ingrese la nota del examen del 0 al 10 (0 para los ausentes, no usar 1 ni 3): "))
    if (nota < 0) or (nota == 1) or (nota == 3) or (nota > 10):
        print(f"Nota inválida {nota}. Vuelva a intentarlo.")
    elif (nota == 0):
        print("El alumno estuvo ausente.")
    elif (nota == 2) or (nota >= 4 and nota <= 10):
        print(f"La nota {nota} ingresada es válida.")
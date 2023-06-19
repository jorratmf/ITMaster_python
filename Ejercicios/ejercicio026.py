## Ejercicio 026

### Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.

invitados = int(input("Ingrese la cantidad de invitados: "))
asientos = int(input("Ingrese la cantidad de asientos disponibles: "))

if invitados <= asientos:
    print("Alcanzan los asientos")
else:
    faltantes = invitados - asientos
    print("No alcanzan los asientos para todos los invitados. Faltan", faltantes, "asientos para que todos puedan sentarse.")

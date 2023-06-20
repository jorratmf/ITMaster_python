## Ejercicio 049
### Escribir un programa que permita validar una opción ingresada. Se le preguntará al usuario si desea continuar con alguna operación de la forma "¿Deseás continuar? [S/N]". Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). La opción debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas

continuar = True

while continuar:
    opcion = input("¿Deseás continuar? [S/N]: ").lower()

    while opcion not in ['s', 'n']:
        opcion = input("Opción inválida. Por favor ingrese S o N: ").lower()

    if opcion == 'n':
        continuar = False
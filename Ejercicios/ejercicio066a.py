'''
## Ejercicio 066a

### La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus 5 estantes. Para cada uno de los 5 estantes, se deben ingresar los libros, y para cada libro, se debe ingresar su nombre (usando 'FIN' si no hay más libros para ese estante), género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género y el promedio de libros por estante.
'''

genero_infantil = 0
genero_novela = 0
genero_historia = 0
total_libros = 0

for estante in range(5):
    max_paginas = -1
    nombre_max_paginas = ""
    print("Estante", estante + 1, ":")
    while True:
        nombre = input("Ingrese el nombre del libro o FIN si no hay más libros: ")
        if nombre == "FIN":
            break
        while True:
            genero = input("Ingrese el género (I, N, H): ").upper()
            if genero in {"I", "N", "H"}:
                break
            print("Género incorrecto. Inténtalo de nuevo.")
        while True:
            paginas = int(input("Ingrese la cantidad de páginas (mayor a 0): "))
            if paginas > 0:
                break
            print("Cantidad de páginas incorrecta. Inténtalo de nuevo.")
        if paginas > max_paginas:
            max_paginas = paginas
            nombre_max_paginas = nombre
        total_libros += 1
        if genero == "I":
            genero_infantil += 1
        elif genero == "N":
            genero_novela += 1
        else:
            genero_historia += 1
    print("El libro con más páginas es", nombre_max_paginas, "con", max_paginas, "páginas.")
    print()

promedio_libros = total_libros / 5
print("Cantidad de libros por género:")
print("Infantil:", genero_infantil)
print("Novela:", genero_novela)
print("Historia:", genero_historia)

print("Promedio de libros por estante:", promedio_libros)
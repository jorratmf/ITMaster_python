## Ejercicio 066d

### La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los 5 estantes, se le pide al usuario que ingrese la cantidad de libros que tendrá ese estante. Para cada libro, se debe ingresar su nombre, género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género.

# Definir diccionarios de géneros y cantidad de libros por género
generos = {'I': 'Infantil', 'N': 'Novela', 'H': 'Historia'}
libros_por_genero = {'Infantil': 0, 'Novela': 0, 'Historia': 0}

# Definir variables para libro con mayor cantidad de páginas
libro_mayor_paginas = ""
mayor_cantidad_paginas = 0

# Pedir al usuario la cantidad de libros por cada estante
for i in range(1, 6):
    cantidad_libros = int(input("Ingrese la cantidad de libros en el estante {}: ".format(i)))
    
    # Pedir al usuario información de cada libro
    for j in range(1, cantidad_libros+1):
        nombre_libro = input("Ingrese el nombre del libro {}: ".format(j))
        genero_libro = input("Ingrese el género del libro (I para Infantil, N para Novela, H para Historia): ")
        cantidad_paginas = int(input("Ingrese la cantidad de páginas del libro: "))
        
        # Actualizar cantidad de libros por género
        libros_por_genero[generos[genero_libro]] += 1
        
        # Verificar si este libro tiene más páginas que el actual libro con mayor cantidad de páginas
        if cantidad_paginas > mayor_cantidad_paginas:
            libro_mayor_paginas = nombre_libro
            mayor_cantidad_paginas = cantidad_paginas
    
    # Mostrar el libro con mayor cantidad de páginas para ese estante
    print("El libro con mayor cantidad de páginas en el estante {} es {} con {} páginas".format(i, libro_mayor_paginas, mayor_cantidad_paginas))
    
# Mostrar la cantidad de libros por género
print("Cantidad de libros por género:")
for genero in libros_por_genero:
    print("{}: {}".format(genero, libros_por_genero[genero]))

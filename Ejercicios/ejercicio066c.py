## Ejercicio 066c

### La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar el fin del estante), se deben ingresar los libros, y para cada libro, se debe ingresar su nombre (usando 'FIN' si no hay más libros para ese estante), género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género y el promedio de libros por estante.


#Inicializar variables
cantidad_infantil = 0
cantidad_historia = 0
cantidad_novela = 0
total_libros = 0
total_estantes = 0
mayor_libro = ("", 0)

#Iterar sobre los estantes
while True:
    #Pedir nombre del estante
    estante = input("Ingrese el nombre del estante (F para finalizar): ")
    #Detener si es F
    if estante == "F":
        break
    #Sumar al total de estantes
    total_estantes += 1
    #Inicializar variables para este estante
    cantidad_estante = 0
    cantidad_estante_infantil = 0
    cantidad_estante_historia = 0
    cantidad_estante_novela = 0
    #Iterar sobre los libros del estante
    while True:
        #Pedir nombre del libro
        libro = input("Ingrese el nombre del libro (FIN si no hay más libros): ")
        #Detener si es FIN
        if libro == "FIN":
            break
        #Pedir género del libro
        genero = input("Ingrese el género del libro (I para Infantil, N para Novela, H para Historia): ")
        #Pedir cantidad de páginas del libro
        paginas = int(input("Ingrese la cantidad de páginas del libro (mayor a 0): "))
        #Verificar que la cantidad de páginas sea mayor a 0
        while paginas <= 0:
            paginas = int(input("Ingrese una cantidad de páginas válida (mayor a 0): "))
        #Sumar al total de libros
        total_libros += 1
        #Actualizar conteos por género y cantidad en este estante
        if genero == "I":
            cantidad_estante_infantil += 1
            cantidad_infantil += 1
        elif genero == "N":
            cantidad_estante_novela += 1
            cantidad_novela += 1
        elif genero == "H":
            cantidad_estante_historia += 1
            cantidad_historia += 1
        cantidad_estante += 1
        #Actualizar libro con mayor cantidad de páginas
        if paginas > mayor_libro[1]:
            mayor_libro = (libro, paginas)
    #Mostrar nombre del libro con mayor cantidad de páginas y su cantidad correspondiente
    print(f"El libro con mayor cantidad de páginas en este estante es {mayor_libro[0]} con {mayor_libro[1]} páginas.")
    #Actualizar variables de conteo totales
    cantidad_total_estante = cantidad_estante_infantil + cantidad_estante_historia + cantidad_estante_novela
    promedio_porestante = cantidad_total_estante / 3
#Mostrar resultados finales
print(f"Cantidad de libros de género infantil: {cantidad_infantil}")
print(f"Cantidad de libros de género novela: {cantidad_novela}")
print(f"Cantidad de libros de género historia: {cantidad_historia}")
print(f"Promedio de libros por estante: {total_libros / total_estantes}")
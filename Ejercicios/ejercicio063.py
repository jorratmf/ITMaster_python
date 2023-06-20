'''
## Ejercicio 063

### Escribir un programa para registrar y obtener información sobre los viajes diarios de un conductor de Uber.
### Cada vez que comienza un viaje se debe ingresar la distancia recorrida, indicando si el viaje fue corto (‘C’), mediano (‘M’), largo (‘L’) o si es el fin de los datos (‘Z’).  
### El día finaliza cuando se llega a los 30 viajes o cuando se ingresa distancia ‘Z’ (fin de los datos).

### Por cada viaje se debe ingresar la siguiente información:

- ### Cantidad de pasajeros (mayor a 0 y menor a 4).
- ### Importe a cobrar, incluyendo la el costo básico ($180).  
- ### Por cada pasajero de ese viaje se debe ingresar:  
- ### Nombre.
- ### Edad (mayor a 18 y menor a 120 años).  

### Se desea saber, para cada viaje, cuál es la persona más grande y su nombre.

### Al finalizar el día de trabajo, el programa debe informar:

- ### Cantidad de viajes por cada categoría (‘C’, ‘M’, ‘L’).
- ### Recaudación total.
- ### Valor promedio del viaje.
- ### Porcentaje de viajes cortos.

### Todos los datos ingresados deben ser validados.
'''

# Función para validar la cantidad de pasajeros (mayor a 0 y menor a 4)


def validar_cantidad_pasajeros(cantidad):
    return cantidad > 0 and cantidad < 4

# Función para validar la edad de un pasajero (mayor a 18 y menor a 120 años)


def validar_edad(edad):
    return edad > 18 and edad < 120

# Función para obtener el nombre de la persona más grande en un viaje


def obtener_persona_mas_grande(pasajeros):
    mayor_edad = 0
    nombre_mayor = ""
    for pasajero in pasajeros:
        if pasajero[1] > mayor_edad:
            mayor_edad = pasajero[1]
            nombre_mayor = pasajero[0]
    return nombre_mayor


# Variables para almacenar los datos
viajes_cortos = 0
viajes_medianos = 0
viajes_largos = 0
recaudacion_total = 0
contador_viajes = 0

# Bucle para ingresar información sobre los viajes
while contador_viajes < 30:
    distancia = input(
        "Ingrese la distancia recorrida (C: corto, M: mediano, L: largo, Z: fin de los datos): ")
    if distancia == 'Z':
        break

    if distancia == 'C':
        viajes_cortos += 1
    elif distancia == 'M':
        viajes_medianos += 1
    elif distancia == 'L':
        viajes_largos += 1

    # Validar y obtener información de cada pasajero
    pasajeros = []
    cantidad_pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
    if not validar_cantidad_pasajeros(cantidad_pasajeros):
        print("Error: Cantidad de pasajeros inválida.")
        continue

    importe_total = 180  # Costo básico de $180
    for _ in range(cantidad_pasajeros):
        nombre = input("Ingrese el nombre del pasajero: ")
        edad = int(input("Ingrese la edad del pasajero: "))
        if not validar_edad(edad):
            print("Error: Edad inválida.")
            continue
        pasajeros.append((nombre, edad))
        importe_total += 180  # Incrementar el importe por cada pasajero

    recaudacion_total += importe_total

    # Obtener la persona más grande en el viaje actual
    persona_mas_grande = obtener_persona_mas_grande(pasajeros)

    # Imprimir información del viaje actual
    print("Información del viaje:")
    print("Distancia:", distancia)
    print("Cantidad de pasajeros:", cantidad_pasajeros)
    print("Importe a cobrar:", importe_total)
    print("Persona más grande:", persona_mas_grande)

    contador_viajes += 1

# Calcular valores finales y mostrar resultados
valor_promedio = recaudacion_total / contador_viajes
porcentaje_cortos = (viajes_cortos / contador_viajes) * 100

print("\nResumen del día de trabajo:")
print("Cantidad de viajes cortos:", viajes_cortos)
print("Cantidad de viajes medianos:", viajes_medianos)
print("Cantidad de viajes largos:", viajes_largos)
print("Recaudación total:", recaudacion_total)
print("Valor promedio del viaje:", valor_promedio)
print("Porcentaje de viajes cortos:", porcentaje_cortos)
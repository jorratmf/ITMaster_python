## Ejercicio 052
### Escribir un programa que permita un programa que permita ingresar la estatura (en metros con decimales) de cada jugador de un equipo de baloncesto. La carga finalizará al ingresar cero. Calcular y mostrar la estatura promedio del equipo.

estaturas = []
while True:
    estatura = float(input("Ingrese la estatura del jugador en metros (0 para terminar): "))
    if estatura == 0:
        break
    estaturas.append(estatura)
    
if len(estaturas) > 0:
    promedio = sum(estaturas) / len(estaturas)
    print("La estatura promedio del equipo es:", round(promedio, 2), "m")
else:
    print("No se ingresaron estaturas.")
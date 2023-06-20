## Ejercicio 064

### Un animal en rehabilitación después de una cirugía requiere ser alimentado y monitoreado en un zoológico. Se alimenta al animal 3 veces al día y se le da de comer hasta que ya no tenga ganas de comer.
### Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (número entero) que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N').
### Se desea conocer:
'''
- ### Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento y cuánto fue esa cantidad.
- ### El total en kg de alimento recibido.
- ### Promedio de alimento por tanda.
'''

comidas = [[], [], []]
for i in range(3):
    while True:
        cantidad = int(input(f"Ingrese la cantidad de alimento en kg para la comida {i+1}: "))
        comidas[i].append(cantidad)
        seguir_comiendo = input("¿Quiere seguir comiendo? (S/N): ")
        while seguir_comiendo.upper() not in ["S", "N"]:
            seguir_comiendo = input("Opción inválida. ¿Quiere seguir comiendo? (S/N): ")
        if seguir_comiendo.upper() == "N":
            break

total_alimento = int(sum([sum(comida) for comida in comidas]))
promedio_alimento = int(total_alimento / len(comidas))

print(f"El total en kg de alimento recibido es: {total_alimento}")
print(f"El promedio de alimento por comida es: {promedio_alimento}")

max_comida = max(comidas, key=sum)
print(f"La comida en la que se dio más alimento fue la número {comidas.index(max_comida)+1} con {sum(max_comida)} kg.")
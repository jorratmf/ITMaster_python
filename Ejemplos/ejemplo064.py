'''
Ejercicio 064
Un animal en rehabilitación después de una cirugía requiere ser alimentado y monitoreado en un zoológico.
Se alimenta al animal 3 veces al día y se le da de comer hasta que ya no tenga ganas de comer.
Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (número entero) que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N') Se desea conocer:
-Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento y cuánto fue esa cantidad.
-El total en kg de alimento recibido.
-Promedio de alimento por tanda.
'''

TANDAS = 3
kg = 0
total = 0
mas_kg = -float('inf')
comida_mayor = 0

for comida in range(TANDAS):
    print(f'Comida {comida + 1} de {TANDAS}')
    terminar = False
    while not terminar:
        kg = int(input('Ingrese la cantidad de alimento en kg: '))

        if kg > mas_kg:
            mas_kg = kg
            comida_mayor = comida + 1

        total += kg

        terminar = input('¿Quiere seguir comiendo? (S/N): ').upper() == 'N'


print(f'El total de alimento recibido es {total} kg.')
print(f'El promedio de alimento por tanda es {total / TANDAS} kg.')
print(f'La cantidad de alimento recibido en la tanda que más comió fue la #{comida_mayor}, con {mas_kg} kg.')
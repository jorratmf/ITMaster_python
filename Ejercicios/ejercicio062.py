## Ejercicio 062

### Un entrenador le ha propuesto a un atleta recorrer una ruta de cinco kilómetros durante 10 días para determinar si es apto para la prueba de 5 kilómetros que se desarrollará en el Parque. No se sabe si está apto y para eso nos piden que hagamos el siguiente programa.
### Nos ingresan por cada día de entrenamiento tiempo de la prueba en minutos (entero mayor que 0 y menor a 100)
### Para considerarlo apto debe cumplir las siguientes condiciones:
'''
- Que en ninguna de las pruebas haga un tiempo mayor a 20 minutos. 
- Que al menos en una de las pruebas realice un tiempo menor de 15 minutos.
- Que su promedio sea menor o igual a 18 minutos.
### Se pide:
- Diseñar un algoritmo para registrar los datos y decidir si es apto para la competencia.
- Sólo en caso de estar apto, informar el promedio y el número de día en el que realizó el
menor tiempo.
'''

total_time = 0
lowest_time = 100
day_lowest_time = 0
is_apt = True

for day in range(1, 11):
    time = int(input(f"Ingrese el tiempo de la prueba en minutos para el día {day}: "))
    
    if time > 20:
        is_apt = False
    
    if time < lowest_time:
        lowest_time = time
        day_lowest_time = day
    
    total_time += time

if lowest_time > 15:
    is_apt = False
    
average_time = total_time / 10

if is_apt:
    print(f"El atleta es apto para la competencia con un promedio de {average_time:.2f} minutos y el menor tiempo de {lowest_time} minutos fue realizado en el día {day_lowest_time}")
else:
    print("El atleta no es apto para la competencia.") 
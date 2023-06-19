'''
## Ejercicio 010

### Escribir un programa para resolver el siguiente problema:
### Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales).

### Calcular qué porcentaje invirtió cada una.

### Como pensarlo:

- 1 Solicitar al usuario que ingrese las cantidades invertidas por cada persona en tres variables numéricas. 

   inversion_persona1 = float(input("Ingrese la cantidad invertida por la persona 1: "))
   
   inversion_persona2 = float(input("Ingrese la cantidad invertida por la persona 2: "))
   
   inversion_persona3 = float(input("Ingrese la cantidad invertida por la persona 3: "))

- 2 Calcular el total de la inversión sumando las cantidades de las tres personas.  

    total = inversion_persona1 + inversion_persona2 + inversion_persona3

- 3 Calcular el porcentaje que representa la inversión de cada persona en relación al total de la inversión.

    - 3 - 1 Dividir la cantidad invertida por cada persona entre el total de la inversión y multiplicar por 100 para obtener el porcentaje.
    Almacenar el resultado en una variable correspondiente a cada persona.
    Opcionalmente, se puede redondear el resultado a un número determinado de decimales utilizando la función round().

    Ejemplo: 

        porcentaje_inversion_persona1 = round((inversion_persona1 / total) * 100, 2)  
        porcentaje_inversion_persona2 = round((inversion_persona2 / total) * 100, 2)  
        porcentaje_inversion_persona3 = round((inversion_persona3 / total) * 100, 2)    


- 4 Mostrar por pantalla el porcentaje de inversión de cada persona.
'''

i1=float(input("Ingrese la cantidad invertida por la persona 1: "))
i2=float(input("Ingrese la cantidad invertida por la persona 2: "))
i3=float(input("Ingrese la cantidad invertida por la persona 3: "))

total=i1+i2+i3

porcentaje1=round((i1/total)*100,2)
porcentaje2=round((i2/total)*100,2)
porcentaje3=round((i3/total)*100,2)

print(f'Porcentaje de inversion de la persona 1: {porcentaje1}%\nPorcentaje de inversion de la persona 2: {porcentaje2}%\nPorcentaje de inversion de la persona 3: {porcentaje3}%')
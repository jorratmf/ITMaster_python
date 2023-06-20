'''
## Ejercicio 060

### Escribir un programa para calcular el sueldo final a pagar a cada empleado de una empresa. De cada uno se tiene, sueldo básico, antigüedad, cantidad de hijos y estudios superiores (‘S’ o ‘N’). Además, se conocen los porcentajes de aumento del sueldo que dependen de los siguientes factores:

- Si el empleado tiene más de 10 años de antigüedad: aumento del 10%  
- Si el empleado tiene más de 2 hijos: aumento del 10%, si solo tiene uno 5%  
- Si el empleado posee estudios superiores: aumento del 5%  

### Luego de ingresar los datos de un empleado se debe preguntar si se desea ingresar otro empleado o no. Se termina la carga cuando no se deseen ingresar más empleados.
- Determinar:  
    - a. Por cada empleado: número de empleado, el sueldo básico y el nuevo sueldo.  
    - b. Sueldo nuevo promedio de la empresa.  
'''

cantidad_empleados = 0
sueldo_empresa = 0

while True:
    cantidad_empleados += 1
    numero_empleado = cantidad_empleados
    sueldo_basico = float(input(f"Ingrese el sueldo básico del empleado {numero_empleado}: "))
    antiguedad = int(input(f"Ingrese la antigüedad en años del empleado {numero_empleado}: "))
    cantidad_hijos = int(input(f"Ingrese la cantidad de hijos del empleado {numero_empleado}: "))
    estudios_superiores = input(f"¿El empleado {numero_empleado} posee estudios superiores? (S/N): ").upper()

    aumento_antiguedad = 0
    aumento_hijos = 0
    aumento_estudios = 0

    if antiguedad > 10:
        aumento_antiguedad = 0.1

    if cantidad_hijos > 2:
        aumento_hijos = 0.1
    elif cantidad_hijos == 1:
        aumento_hijos = 0.05

    if estudios_superiores == "S":
        aumento_estudios = 0.05

    aumento_total = aumento_antiguedad + aumento_hijos + aumento_estudios
    nuevo_sueldo = round(sueldo_basico * (1 + aumento_total), 2)

    print(f"Empleado {numero_empleado}:")
    print(f"Sueldo básico: {sueldo_basico}")
    print(f"Nuevo sueldo: {nuevo_sueldo}\n")

    sueldo_empresa += nuevo_sueldo

    opcion = input("¿Desea ingresar otro empleado? (S/N): ").upper()
    if opcion == "N":
        break

promedio_sueldo = sueldo_empresa / cantidad_empleados

print(f"Sueldo nuevo promedio de la empresa: {promedio_sueldo}")
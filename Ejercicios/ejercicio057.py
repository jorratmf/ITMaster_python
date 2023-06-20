'''
Ejercicio 057

Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo. 

Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
- Cantidad de alumnos que aprobaron (nota >= 4).
- Cantidad de alumnos que desaprobaron el examen (nota < 4).
- Porcentaje de alumnos que están aplazados (nota == 1).
'''

legajo = int(input("Ingrese el número de legajo del alumno (o -1 para salir): "))
aprobados = 0
desaprobados = 0
aplazados = 0
total_alumnos = 0

while legajo != -1:
    nota = int(input("Ingrese la nota del alumno (entre 1 y 10): "))
    while nota < 1 or nota > 10:
        nota = int(input("Nota inválida. Ingrese la nota del alumno (entre 1 y 10): "))
    
    total_alumnos += 1
    
    if nota >= 4:
        aprobados += 1
        print("El alumno con legajo", legajo, "ha aprobado el examen.")
    else:
        desaprobados += 1
        print("El alumno con legajo", legajo, "ha desaprobado el examen.")
        if nota == 1:
            aplazados += 1
    
    legajo = int(input("Ingrese el número de legajo del alumno (o -1 para salir): "))

porcentaje_aplazados = (aplazados / total_alumnos) * 100

print("Cantidad de alumnos que aprobaron: ", aprobados)
print("Cantidad de alumnos que desaprobaron el examen: ", desaprobados)
print("Porcentaje de alumnos que están aplazados: ", porcentaje_aplazados, "%")
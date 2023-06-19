'''
Ejercicio 057
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo. 
Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
- Cantidad de alumnos que aprobaron (nota >= 4).
- Cantidad de alumnos que desaprobaron el examen (nota < 4).
- Porcentaje de alumnos que están aplazados (nota == 1).
'''

def ingresar_legajo():
    legajo = int(input("Ingrese el número de legajo del alumno (-1 para terminar): "))
    return legajo

def ingresar_nota():
    nota = float(input("Ingrese la nota del examen final (entre 1 y 10): "))
    while nota < 1 or nota > 10:
        print("Nota inválida. Intente de nuevo.")
        nota = float(input("Ingrese la nota del examen final (entre 1 y 10): "))
    return nota

def ingresar_notas():
    legajos = []
    notas = []
    legajo = ingresar_legajo()
    while legajo != -1:
        nota = ingresar_nota()
        legajos.append(legajo)
        notas.append(nota)
        legajo = ingresar_legajo()
    return legajos, notas

def informar_resultado_individual(legajo, nota):
    if nota >= 4:
        print(f"El alumno con legajo {legajo} aprobó el examen.")
    else:
        print(f"El alumno con legajo {legajo} desaprobó el examen.")

def calcular_estadisticas(legajos, notas):
    aprobados = 0
    desaprobados = 0
    aplazados = 0
    for i in range(len(legajos)):
        if notas[i] >= 4:
            aprobados += 1
        else:
            desaprobados += 1
            if notas[i] == 1:
                aplazados += 1
    return aprobados, desaprobados, aplazados

def informar_estadisticas(aprobados, desaprobados, aplazados, total_alumnos):
    print(f"Cantidad de alumnos que aprobaron: {aprobados}")
    print(f"Cantidad de alumnos que desaprobaron: {desaprobados}")
    if total_alumnos > 0:
        porcentaje_aplazados = aplazados / total_alumnos * 100
        print(f"Porcentaje de alumnos que están aplazados: {porcentaje_aplazados:.2f}%")

def informar_resultados(legajos, notas):
    for i in range(len(legajos)):
        informar_resultado_individual(legajos[i], notas[i])
    aprobados, desaprobados, aplazados = calcular_estadisticas(legajos, notas)
    informar_estadisticas(aprobados, desaprobados, aplazados, len(legajos))

def main():
    legajos, notas = ingresar_notas()
    informar_resultados(legajos, notas)

if __name__ == "__main__":
    main()
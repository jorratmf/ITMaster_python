## Ejercicio 053

### Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.


personas = []

while True:
    nombre = input("Ingrese el nombre de la persona o '*' para salir: ")
    if nombre == '*':
        break
    edad = int(input("Ingrese la edad de la persona: "))
    personas.append({'nombre': nombre, 'edad': edad})

persona_mas_joven = min(personas, key=lambda p: p['edad'])
print('La persona más joven se llama', persona_mas_joven['nombre'])

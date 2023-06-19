'''
Ejercicio 003

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
cantidad_anios = int(input("Ingresa la cantidad de años que deseas incrementar a tu edad: "))

edad_futura = edad + cantidad_anios
mensaje = f"Hola, {nombre}. Dentro de {cantidad_anios} años tendrás {edad_futura} años."

print(mensaje)
.

Ejemplo: Si el usuario ingresa "Juan" y "20" y luego ingresa "5", el programa debe mostrar por pantalla "Hola, Juan. Dentro de 5 años tendrás 25 años".
'''
nombre=str(input("Ingrese su nombre: "))
edad=int(input("Ingrese su edad: "))
edad_futura=int(input("Ingrese una cantidad de años: "))

print(f'Hola {nombre}. Dentro de {edad_futura} año/s tendrás {edad+edad_futura} años.')
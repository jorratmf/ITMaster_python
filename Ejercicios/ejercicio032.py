## Ejercicio 032

### Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.
### Tiene la siguiente tarifa: 
'''
- Viaje mínimo $50  

- Si recorre entre 0 y 10km: $20/km  

- Si recorre 10km o más: $15/km  
'''
### Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.

kilometers = float(input("Ingrese la cantidad de kilómetros a recorrer: ")) #Pedir al usuario que ingrese la cantidad de kilómetros a recorrer
if kilometers < 0: # Si la cantidad de kilómetros es negativa, mostrar un mensaje de error
    print("Error: la cantidad de kilómetros ingresada es inválida.")
elif kilometers <= 10: # Si la cantidad de kilómetros es menor o igual a 10, aplicar tarifa de 20 por km
    cost = max(50, kilometers*20) # Aplicar tarifa mínima de 50
    print(f"El costo del viaje es de ${cost}")
else: # Si la cantidad de kilómetros es mayor que 10, aplicar tarifa de 15 por km
    cost = max(50, kilometers*15) # Aplicar tarifa mínima de 50
    print(f"El costo del viaje es de ${cost}")
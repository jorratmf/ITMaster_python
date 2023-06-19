# Ejercicio 011

### Escribir un programa que permita resolver el siguiente problema: 
### Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje). 
### Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente.

socios = []
total = 0

# pedir información de cada socio
for i in range(3):
    nombre = input(f"Ingrese el nombre del socio {i+1}: ")
    capital = float(input(f"Ingrese el capital aportado por el socio {i+1}: "))
    socios.append((nombre, capital))
    total += capital

# calcular porcentajes y mostrar resultados
porcentajes = [round((c/total)*100,2) for _, c in socios]
for i, (nombre, _) in enumerate(socios):
    print(f"Porcentaje de inversión de {nombre}: {porcentajes[i]}%")
## Ejercicio 045

### Escribir un programa que permita leer dos números naturales A y B. Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.  

### Ejemplo:  
'''
- 4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).  
- 3^4 = 3 * 3 * 3 * 3 (3 multiplicado 4 veces).
'''

def potencia_por_productos(A, B):
    sucesion = []
    resultado = 1
    for _ in range(B):
        sucesion.append(str(A))
        resultado *= A
    sucesion = ' * '.join(sucesion)
    return sucesion, resultado

# Solicitar los números al usuario
A = int(input("Ingrese el primer número (A): "))
B = int(input("Ingrese el segundo número (B): "))

# Calcular la potencia por productos sucesivos
resultado, potencia = potencia_por_productos(A, B)

# Imprimir el resultado
print("El resultado de", A, "elevado a la", B, "es igual a", resultado, "=", potencia)
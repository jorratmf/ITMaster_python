## Ejercicio 044

### Escribir un programa que permita leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado. 

### Ejemplo:
'''
- 4*3 = 4 + 4 + 4 (4 sumado 3 veces).  
- 3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).
'''

def producto_por_sumas(A, B):
    sucesion = []
    producto = 0
    for _ in range(B):
        sucesion.append(str(A))
        producto += A
    sucesion = ' + '.join(sucesion)
    return sucesion, producto

# Solicitar los números al usuario
A = int(input("Ingrese el primer número (A): "))
B = int(input("Ingrese el segundo número (B): "))

# Calcular el producto por sumas sucesivas
resultado, producto = producto_por_sumas(A, B)

# Imprimir el resultado
print("El producto de", A, "*", B, "es igual a", resultado, "=", producto)
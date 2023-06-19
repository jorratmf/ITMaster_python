## Ejercicio 015

### Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes. 
### Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

### ¿Sobran datos? ¿Qué datos sobran?

# Definición de variables y lectura por teclado de los datos necesarios
nombre_vendedor = input("Ingrese el nombre del vendedor: ")
sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
valor_ventas = float(input("Ingrese el valor total de las ventas: "))

COMISION = valor_ventas * 0.05

sueldo_total = sueldo_base + COMISION

print(f"El vendedor {nombre_vendedor} cobrará un total de ${sueldo_total:.2f} pesos.")
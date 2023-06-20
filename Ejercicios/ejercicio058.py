'''
## Ejercicio 058
### Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
- ### Aplica el precio base a la primera docena de unidades.  
- ### Aplica un 10% de descuento a todas las unidades entre 13 y 100.  
- ### Aplica un 25% de descuento a todas las unidades por encima de las 100.
### Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería:  
100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04  
### Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. El fin de carga se determina ingresando -1 como cantidad solicitada.
### Al finalizar informar:  
- a) Cantidad de ventas realizadas total.
- b) Cantidad de ventas que se aplicaron un 10% de descuento.
- c) Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos
'''

cantidad = int(input("Ingrese cantidad: "))
precio_base = float(input("Ingrese el precio base: "))
ventas_total = 0
ventas_10_desc = 0
ventas_precio_base = 0

while cantidad != -1:
    if cantidad <= 12:
        precio_venta = cantidad * precio_base
        ventas_precio_base += 1
    elif cantidad <= 100:
        precio_venta = 12 * precio_base + (cantidad - 12) * precio_base * 0.9
        ventas_10_desc += 1
    else:
        precio_venta = 12 * precio_base + 88 * precio_base * 0.9 + (cantidad - 100) * precio_base * 0.75
        ventas_10_desc += 1
    
    ventas_total += 1
    print("Precio venta: ", precio_venta)
    cantidad = int(input("Ingrese cantidad: "))
    
precio_promedio = ventas_total / precio_venta
print("Valor total de la venta: ", ventas_total * precio_venta)
print("Precio promedio por unidad: ", precio_promedio)
print("Cantidad de ventas realizadas total: ", ventas_total)
print("Cantidad de ventas que se aplicaron un 10% de descuento: ", ventas_10_desc)
print("Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos: ", ventas_precio_base)

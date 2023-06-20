'''
## Ejercicio 065

### Una cadena de comida rápida solicita el desarrollo de una aplicación para sus terminales de autoservicio que permita a los clientes armar su propio menú. Los clientes pueden elegir entre diferentes opciones de combos o pedir por separado la comida, bebida y postre.

### Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:

- #### 1) Combo 1: Hamburguesa, papas fritas y gaseosa - 1550
- #### 2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650
- #### 3) Hamburguesa sola - 1300
- #### 4) Hamburguesa con queso - 1400
- #### 5) Gaseosa - 700
- #### 6) Postre - 600
- #### 7) Agregar aderezo - 100
- #### 8) Terminar

### Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente pueda decidir si desea agregar más productos a su pedido antes de terminar.  
### El valor mínimo del pedido debe ser de $1550. Si el cliente elige un combo, se debe sumar el importe total al subtotal. Si el cliente selecciona opciones 3 a 7, se le debe preguntar la cantidad deseada y calcular el valor total antes de sumarlo al subtotal.
### Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más caro y, si no se han seleccionado productos, mostrar un mensaje que diga "Pedido cancelado".
'''

subtotal = 0
item_mas_caro = 0
pedido = []

print("Bienvenido a la cadena de comida rápida")
print("Menú:")
print("1) Combo 1: Hamburguesa, papas fritas y gaseosa - 1550")
print("2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650")
print("3) Hamburguesa sola - 1300")
print("4) Hamburguesa con queso - 1400")
print("5) Gaseosa - 700")
print("6) Postre - 600")
print("7) Agregar aderezo - 100")
print("8) Terminar")

productos_seleccionados = False

while True:
    opcion = input("Ingrese el número de la opción deseada o 8 para terminar: ")
    
    if not opcion:
        print("Debe ingresar una opción válida")
        continue
        
    opcion = int(opcion)
    
    if opcion == 8:
        if not productos_seleccionados:
            print("El pedido ha sido cancelado, no se seleccionaron productos")
            break
        elif subtotal < 1550:
            print("El valor mínimo del pedido es de $1550")
        else:
            for item in pedido:
                if item > item_mas_caro:
                    item_mas_caro = item
            print("El monto total a pagar es de ${}".format(subtotal))
            print("El ítem más caro es de ${}".format(item_mas_caro))
            break
    
    if opcion == 1:
        cantidad = input("Ingrese la cantidad deseada de combo 1: ")
        if not cantidad:
            print("Debe ingresar una cantidad válida")
            continue
        cantidad = int(cantidad)
        pedido.append(1550 * cantidad)
        subtotal += 1550 * cantidad
        productos_seleccionados = True
    elif opcion == 2:
        cantidad = input("Ingrese la cantidad deseada de combo 2: ")
        if not cantidad:
            print("Debe ingresar una cantidad válida")
            continue
        cantidad = int(cantidad)
        pedido.append(1650 * cantidad)
        subtotal += 1650 * cantidad
        productos_seleccionados = True
    elif opcion == 3:
        cantidad = input("Ingrese la cantidad deseada de la hamburguesa sola: ")
        if not cantidad:
            print("Debe ingresar una cantidad válida")
            continue
        cantidad = int(cantidad)
        total = cantidad * 1300
        pedido.append(total)
        subtotal += total
        productos_seleccionados = True
    elif opcion == 4:
        cantidad = input("Ingrese la cantidad deseada de la hamburguesa con queso: ")
        if not cantidad:
            print("Debe ingresar una cantidad válida")
            continue
        cantidad = int(cantidad)
        total = cantidad * 1400
        pedido.append(total)
        subtotal += total
        productos_seleccionados = True
    elif opcion == 5:
        cantidad = input("Ingrese la cantidad deseada de la gaseosa: ")
        if not cantidad:
            print("Debe ingresar una cantidad válida")
            continue
        cantidad = int(cantidad)
        total = cantidad * 700
        pedido.append(total)
        subtotal += total
        productos_seleccionados = True
    elif opcion == 6:
        cantidad = input("Ingrese la cantidad deseada del postre: ")
        if not cantidad:
            print("Debe ingresar una cantidad válida")
            continue
        cantidad = int(cantidad)
        total = cantidad * 600
        pedido.append(total)
        subtotal

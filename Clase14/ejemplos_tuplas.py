


renglon = ("Producto 1",3,100)

renglones = (renglon,renglon,renglon)

print(renglones)

total = 0
for renglon in renglones:
    importe = renglon[1]*renglon[2] # Cantidad * precio
    total += importe
    print(renglon,importe)
print("total: ",total)
## Ejercicio 017

cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))

billetes_mil = cantidad_total // 1000
resto = cantidad_total % 1000

billetes_doscientos = resto // 200
resto = resto % 200

billetes_cien = resto // 100
resto = resto % 100

billetes_cincuenta = resto // 50
resto = resto % 50

billetes_diez = resto // 10
resto = resto % 10

billetes_cinco = resto // 5
resto = resto % 5

billetes_uno = resto // 1


print("Para la cantidad de $", cantidad_total, " se necesitan:")
print(billetes_mil, "billetes de $1000")
print(billetes_doscientos, "billetes de $200")
print(billetes_cien, "billetes de $100")
print(billetes_cincuenta, "billetes de $50")
print(billetes_diez, "billetes de $10")
print(billetes_cinco, "billetes de $5")
print(billetes_uno, "billetes de $1")
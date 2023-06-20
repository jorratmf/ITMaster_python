## Ejercicio 055

### Escribir un programa que permita para cada cliente que va al banco "Express".
### Cada cliente indica su número de documento y aguarda a ser atendido, cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser atendidos. El banco desea saber quién fue el primer cliente atendido y quién fue el último.

first_client = None
last_client = None

while True:
    doc_number = int(input("Ingrese número de documento del cliente: "))
    if doc_number == -1:
        break
    if not first_client:
        first_client = doc_number
    last_client = doc_number
    
print(f"El primer cliente atendido fue {first_client} y el último cliente atendido fue {last_client}")
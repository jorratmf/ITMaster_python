## Ejercicio 054
### Escribir un programa que permita controlar con validación el ingreso a un sitio web. Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), el programa debe permitir al usuario ingresar sus credenciales. Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: "Acceso concedido" o "Se ha bloqueado la cuenta"

ADMIN = "admin"
CONTRASENIA = "123456"

for i in range(3):
    usuario = input("Ingrese su nombre de usuario: ")
    contrasenia = input("Ingrese su contraseña: ")
    if usuario == ADMIN and contrasenia == CONTRASENIA:
        print("Acceso concedido")
        break
    else:
        print("Usuario o contraseña incorrectos")
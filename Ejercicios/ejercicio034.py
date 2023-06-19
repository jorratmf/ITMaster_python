## Ejercicio 034
'''
### Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. También se le realizan los siguientes descuentos:

- Jubilación: 11%  

- Obra Social: 3%  

- Sindicato: 3%  

### Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)

Estado Civil: Soltero/Casado
Sueldo básico: $ 999.99
Antigüedad: 99 años

Descuentos:

- Jubilación - 999,99  

- Obra Social - 999,99  

- Sindicato - 999,99  

Sueldo Neto 999,99
'''

estado_civil = input("Estado Civil: ")
sueldo_basico = float(input("Sueldo básico: $ "))
antiguedad = int(input("Antigüedad: "))

incremento_anual = 0
if estado_civil.upper() == "S":
    incremento_anual = 0.05
elif estado_civil.upper() == "C":
    incremento_anual = 0.07

salario_bruto = sueldo_basico * (1 + incremento_anual * antiguedad)
jubilacion = salario_bruto * 0.11
obra_social = salario_bruto * 0.03
sindicato = salario_bruto * 0.03
salario_neto = salario_bruto - jubilacion - obra_social - sindicato

print("Descuentos:\n")
print("- Jubilación: $", format(jubilacion, ".2f"))
print("- Obra Social: $", format(obra_social, ".2f"))
print("- Sindicato: $", format(sindicato, ".2f"))
print("\nSalario Neto: $", format(salario_neto, ".2f"))
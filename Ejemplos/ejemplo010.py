'''
PROGRAMA PRINCIPAL
en el main se "dice" qué hace el programa
'''

import random
'''
20210000
    0700
+     25
--------
20210725
'''

def esfecha_valida(aaaammdd):
    pass

# Funciones
def es_bisiesto(a):
    es = a%4 == 0 and a%100 != 0 or a%400 == 0
    return es

def obtener_cantidad_dias_del_mes(m, anio):
    cantidad = 31
    if m in (4,6,9,11):
        cantidad = 30
    elif m == 2:
        if es_bisiesto(anio):
            cantidad = 29
        else:
            cantidad = 28
    return cantidad

def obtener_fecha_random(anio):
    m = random.randint(1, 12)
    cantidad_dias = obtener_cantidad_dias_del_mes(m, anio)
    d = random.randint(1, cantidad_dias)
    return (anio*10000) + (m*100) + d # AAAAMMDD

def el_anio(aaaammdd):
    '''
    Retorna el año de una fecha
    AAAA|==> MM <==|DD
    '''
    return aaaammdd // 10000 # AAAA <== |MMDD

def el_mes(aaaammdd):
    return (aaaammdd // 100) % 100 # AAAA| ==> MM <== |DD

def el_dia(aaaammdd):
    return aaaammdd % 100 # AAAAMMDD

def str_fecha(aaaammdd):
    d = el_dia(aaaammdd)
    m = el_mes(aaaammdd)
    a = el_anio(aaaammdd)

    return f'{d:02}/{m:02}/{a:04}' # f-string


# Programa principal
def main ():
    fecha = obtener_fecha_random(1)
    cadena = str_fecha(fecha)
    print(cadena)


main() # LLAMO A LA FUNCION PRINCIPAL
from importlib import import_module


def ej1():
    ANCHO = int(input("Ingrsar el ancho de la habitacion:\t"))
    LARGO = int(input("Ingrsar el largo de la habitacion:\t"))

    print("El area es de:\t" + str(ANCHO*LARGO) + "m")
def ej2():
    ANCHO = float(input("Ingrsar el ancho del campo:\t"))
    LARGO = float(input("Ingrsar el largo del campo:\t"))

    print("El area es de:\t%.2f"  %((ANCHO/100) *(LARGO/100))+ "Hectareas")
def ej3():
    cantidad_de_botellas_mayor_a_un_litro = float(input("Cantidad de botellas:\t"))
    cantidad_de_botellas_menor_a_un_litro = float(input("Cantidad de botellas:\t"))

    
    precio_menor_1l = 1.75
    precio_mayor_1l = 2.25
    

    print("Tu saldo es de:\t%.2f"  %((cantidad_de_botellas_mayor_a_un_litro*precio_mayor_1l) + (cantidad_de_botellas_menor_a_un_litro*precio_menor_1l) ))
def ej4():
    propina = 0.15
    inpuestos_por_plato = 150
    comensales = float(input("Cantidad de clmensales:"))
    precio_final = float(input("Valor de la comida:"))

    print("Precio total:\t%.2f"  %((comensales*inpuestos_por_plato) + (precio_final)/propina))
def ej5():
    porcentaje_de_intereses = 1.09
    valance_de_mi_cuenta = float(input("Ingresa el monto a depositar:\t"))
    ganacia_primer_año = (valance_de_mi_cuenta*porcentaje_de_intereses)
    
    print ("Esta es la ganancia del primer año:\t%.2f" % ganacia_primer_año )

    ganacia_segundo_año = (ganacia_primer_año*porcentaje_de_intereses)

    print ("Esta es la ganancia del segundo año:\t%.2f" % ganacia_segundo_año)

    ganacia_tercer_año = (ganacia_segundo_año*porcentaje_de_intereses)

    print ("Esta es la ganancia del tercer año:\t%.2f" % ganacia_tercer_año)
def ej6():
    import math
    pi=math.pi

    radio = float(input("Ingresar el valor del radio del cilindro:\t"))
    
    print ("Este es el area del circulo:\t%.2f" % (pi*radio)**2)

    radio_esfera = float(input("Ingresar el valor del radio de la esfera:\t"))

    print ("Este es el area de la esfera:\t%.2f" % (4*pi*radio_esfera)**2)
def ej7():
    dias = int(input("Ingresar cantidad de dias:\t"))
    horas = int(input("Ingresar cantidad de horas:\t"))
    minutos = int(input("Ingresar cantidad de minutos:\t"))

    segundos_de_dias = (dias*86400)
    segundos_de_horas = (horas*3600)
    minutos_de_segundos = (minutos*60)

    print ("Segundos totales:\t" + str(segundos_de_dias + segundos_de_horas + minutos_de_segundos))
def ej8():
    segundos = float(input("ingrsar los segundos totales:\t"))

    dias = round(segundos/86400)
    horas = round(segundos/3600)
    minutos = round(segundos/60)

    print ("D: " ,dias)
    print ("HH: " ,horas)
    print ("MM: " ,minutos)
    print ("SS: " ,segundos)
def ej9():
    celsius = float(input("Ingresar cuantos grados hacen hoy: "))

    fahrenheit = ((celsius*1.8)+32)
    kelvin = (celsius+273.15)
    print("fahrenheit: ", fahrenheit)
    print("kelvin: ", kelvin)
def ej10():
    n1 = float(input("Ingrse su primer numero: "))
    n2 = float(input("Ingrse su segundo numero: "))
    n3 = float(input("Ingrse su tercer numero: "))

    masgrande = max(n1,n2,n3)
    maschico = min(n1,n2,n3)
    print("Este es el numero mas grande: " , masgrande)
    print("Este es el numero intermedio: ", (masgrande-maschico))
    print("Este es el numero mas chico: ", maschico)


ej10()

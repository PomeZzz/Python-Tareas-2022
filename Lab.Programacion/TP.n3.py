from asyncio.windows_events import NULL
from cgi import print_arguments
from math import comb
from operator import index
from re import T
from traceback import print_tb
from xml.sax.handler import EntityResolver


def ej1():
    numero = int(input("Ingresar un numero: "))

    if numero % 2 == 0:
        print("Tu numero es par")
    else:
        print("Tu numero es impar")
def ej2():
    letra = input("Ingrsar una letra: ")

    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("Tu letra es una vocal")
    else:
        print("Tu letra es consonante")
def ej3():
    lados = int(input("Ingresar la cantidad de lados de la figura: "))
    if lados == 4:
        print("Es un cuadrado")
    elif lados == 3:
        print("Es un triangulo")
    elif lados == 5:
        print("Es un pentagono")
    elif lados == 6:
        print("Es un Hexagono")
    elif lados == 7:
        print("Es un Heptagono")
    elif lados == 8:
        print("Es un octogono")
    elif lados == 9:
        print("Es un enagono")
    elif lados == 10:
        print("Es un decagono")
    elif lados > 10:
        print("ERROR -> cantidad de lados superiro a la soportada")
    elif lados < 3:
        print("ERROR -> cantidad de lados menor a la soportada")
def ej4():
    mes = input("Ingrese un mes del año: ")
    

    if mes == "enero" or mes =="marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre":
        print("El mes que elegiste tiene 30 dias")
    elif mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre":
        print("El mes que elegiste tiene 31 dias")
    elif mes == "febrero":
        print("El mes que elegiste tiene 28 dias")
def ej5():
    billete = int(input("Ingrese el monto del billete: "))

    if billete == 10:
        print("El que aparece en el billete de 10$ es el General Manuel Belgrano")
    elif billete == 20:
        print("El que aparece en el billete de 20$ es Juan Manuel de Rosas, pero en la nueva ilustracion aparece un Guanaco")
    elif billete == 50:
        print("El que aparece en el billete de 50$ es Domingo Faustino Sarmiento")
    elif billete == 100:
        print("La que aparece en el billete de 100$ es Maria Eva Duarte de Peron")
    elif billete == 200:
        print("El que aparece en el billete de 200$ es Jose de Miguel de Guemes y Juan Azurduy")
    elif billete == 1000:
        print("El que aparece en el billete de 1000$ es Jose de San Martin")
    elif billete != 10 or billete != 20 or billete != 50 or billete != 100 or billete != 200 or billete != 500 or billete != 1000:
        print("ERROR no corresponde a ningun billete")
def ej6():
    dia = input("Ingresa un mes")

    if dia == "marzo" or dia == "abirl" or dia == "mayo" or dia == "junio":
        print("Estas en otoño!!!!")
    elif dia == "diciembre" or dia == "enero" or dia == "febrero" or dia == "marzo":
        print("Estas en Verani!!!!")
    elif dia == "junio" or dia == "julio" or dia == "agosto" or dia == "septiembre":
        print("Estas en invierno!!!!")
    elif dia == "septiembre" or dia == "octubre" or dia == "noviembre" or dia == "dicembre":
        print("Estas en Primavera!!!!")
def ej7():
    mes = int(input("Ingrese un mes: "))
    dia = int(input("Ingrese un dia: "))
    signo = ""
    
    if mes == 1:
        if dia <= 20:
            signo = "Capricornio"
        else:
            signo = "Acuario"
    elif mes == 2:
        if dia <= 18:
            signo = "Acuario"
        else:
            signo = "Piscis"
    elif mes == 3:
        if dia <= 20:
            signo = "Piscis"
        else:
            signo = "Aries"
    elif mes == 4:
        if dia <= 20:
            signo = "Aries"
        else:
            signo = "Tauro"
    elif mes == 5:
        if dia <= 21:
            signo = "Tauro"
        else:
            signo = "Géminis"
    elif mes == 6:
        if dia <= 21:
            signo = "Géminis"
        else:
            signo = "Cáncer"
    elif mes == 7:
        if dia <= 22:
            signo = "Cáncer"
        else:
            signo = "Leo"
    elif mes == 8:
        if dia <= 23:
            signo = "Leo"
        else:
            signo = "Virgo"
    elif mes == 9:
        if dia <= 23:
            signo = "Virgo"
        else:
            signo = "Libra"
    elif mes == 10:
        if dia <= 23:
            signo = "Libra"
        else:
            signo = "Escorpio"
    elif mes == 11:
        if dia <= 22:
            signo = "Escorpio"
        else:
            signo = "Sagitario"
    elif mes == 12:
        if dia <= 21:
            signo = "Sagitario"
        else:
            signo = "Capricornio"
    print(signo)
def ej8():
    año = int(input("Ingrese un año: "))
    bisiesto = ""
    
    
    if año%400 == 0:
        bisiesto = True
    elif año%100 == 0:
        bisiesto = False
    elif año%4 == 0:
        bisiesto = True
    else:
        bisiesto = False


    if bisiesto:
        print(año, " este año es biciesto.")
    else:
        print(año," este año no es biciesto")
def ej9():
    
    minutos_en_llamada = int(input("Minutos de llamada: "))
    mensajes_enviados = int(input("Mensajes enviados: "))
    
    
    MINUTOS_DE_LLAMADA = 50
    MENSAJES_ENVIADOS = 50
    LLAMADAS_ADICIONALES = 3.50
    MENSAJES_ADICIONALES = 2.25

    extra_llamadas = ((minutos_en_llamada)-50)*LLAMADAS_ADICIONALES
    extra_mensajes = ((mensajes_enviados)-50)*MENSAJES_ADICIONALES

    if minutos_en_llamada > MINUTOS_DE_LLAMADA:
        print("Este es el monto a pagar", extra_llamadas, "$")
    elif minutos_en_llamada <= MINUTOS_DE_LLAMADA:
        print("El monto a pagar es de 450$")

    if mensajes_enviados > MENSAJES_ENVIADOS:
        print("El monto a pagr es de: ", extra_mensajes, "$")
    elif mensajes_enviados <= MENSAJES_ENVIADOS:
        print("El monto a pagar es de: 450$")
def ej10():
    combinacion = input("Ingrese una letra y un numero: ")
    fila = int(combinacion[1])

    if (combinacion[0] == "a" or combinacion[0] == "c" or combinacion[0] == "e" or combinacion[0] == "g") and fila % 2 == 1:
        print("Es una casilla negra")
    elif(combinacion[0] == "b" or combinacion[0] == "d" or combinacion[0] == "f" or combinacion[0] == "h") and fila % 2 == 0:
        print("Es una casilla negra")
    else:
        print("Es una casilla blanca")
ej10()
from email.headerregistry import MessageIDHeader
from xml.etree.ElementTree import tostring


def ej1():
    numero = int(input("Ingrese un numero: "))
    cant = 0
    total = 0
    while numero != 0:
        cant = cant + 1
        total = (total + numero)
        numero = int(input("Ingrese un numero: "))
    
    promedio = (total)/cant
    print(promedio)
def ej2():

    CELCIUS = 0
    CANT = 0
    KELVIN = 273

    while CANT < 11:
        CANT = CANT + 1
        print("Celcius", CELCIUS, "Kelvin", KELVIN)
        CELCIUS = CELCIUS + 10
        KELVIN = KELVIN + 10
def ej3():
    PRECIO1 = 140
    PRECIO2 = 180
    PRECIO3 = 230
    total = 0
    EDAD1 = 2
    EDAD2 = 12
    EDAD3 = 65

    edad = input("Ingrese la edad de la persona: ")
    while edad != "":
        edad = int(edad)

        if edad >= EDAD1:
            total = total + PRECIO1
        elif edad >= EDAD2:
            total = total + PRECIO2
        elif edad <= EDAD3:
            total = total + PRECIO3
        
        edad = input("Ingrese la edad de la persona: ")
        


    
    print(total)    
def ej5():
    numero = int(input("Ingrese el numero a multiplicar: "))
    
    
    for x in range(1,11):
        
        pitagoras = numero * x
        print(numero, "x" ,x, "=" ,pitagoras)
def ej6():
    binario = int(input("numero en binario: "))

    decimal = 0
    i = 0
    while (binario>0):
        digito  = binario%10
        binario = int(binario//10)
        decimal = decimal+digito*(2**i)
        i = i+1

    print("en decimal: ",decimal)
def ej7():
    decimal = int(input("Ingresa un número decimal: "))
    if decimal <= 0:
        return "0"

    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario

    print(binario)
def ej4():
    igual = 0
    messi = 0

    texto = input("Ingresa tu palabra: ")

    for x in reversed(range(0, len(texto))):
        if texto[x].lower() == texto[messi].lower():
            igual += 1
            messi += 1

    if len(texto) == igual:
        print("Es capicua")
    else:
        print("No es capicua")

ej4()
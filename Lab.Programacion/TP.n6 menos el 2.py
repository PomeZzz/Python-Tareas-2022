from random import sample
from random import randrange
def ej1():
    lista = []
    numeros = int(input("Ingrese un Numero: "))
    while numeros != 0:
        lista.append(numeros)
        numeros = int(input("Ingrese un Numero: "))

    lista.sort()
    print(lista)
def ej3():
    lista = []
    palabras = input("Ingrsar una Palabra: ")
    while palabras != "":
        lista.append(palabras)
        palabras = input("Ingrsar una Palabra: ")

    for x in lista:
        print(x)
def ej4():
    lista = sample(range(1,46), 6)
    lista.sort()
    print(lista)


def esta_ordenada(listas):
    listas.append(0)
    for x in range(0, len(listas)):
        pos = x + 1
        if listas[x] == 0:
            return True
        elif listas[x] > listas[pos] != 0:
            return False

def ej5():
    lista = []
    numeros = int(input("Ingresar un Numero: "))
    while numeros != 0:
        lista.append(numeros)
        numeros = int(input("Ingresar un Numero: "))

    if esta_ordenada(lista):
        print("Esta ordenada")
    else:
        print("No esta ordenada")

def crear_mazo():
    maso = []

    for palo in ["d","c","p","t"]:
        for palosNumeros in ["2","3","4","5","6","7","8","9","D","J","Q","K","A"]:
            maso.append(palo + palosNumeros)
    
    return maso

def mesclar(maso):
    for x in range(0, len(maso)):
        ubicacion = randrange(0, len(maso))

        owo = maso[1]
        maso[1] = maso[ubicacion]
        maso[ubicacion] = owo

def ej6():
    maso = crear_mazo()
    print(maso)
    mesclar(maso)

ej6()



def pitagoras(l1, l2):
    from math import sqrt
    hipotenusa = sqrt((l2**2) + (l1**2))
    return (hipotenusa)

def ej1():
    lado1 = int(input("Ingrese un numero: "))
    lado2 = int(input("Ingrese otro numero: "))
    print(pitagoras(lado1, lado2))
TAXI = 13.75
TARIFA_BASE = 120

def distancia(km):
    costo = TARIFA_BASE + (km/100)*TAXI
    return(costo)

def ej2():
    kilometros = int(input("Ingrese la distancia en kilometros: "))
    print(distancia(kilometros))

def bienEscrito(texto):
    L = texto[0]

def ej2():
    texto = input("Ingrese su texto")
    print(bienEscrito(texto))

def primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True
def ej4():
    numero = int(input("Ingrese un numero: "))
    print(primo(numero))


def ej5():
    numero = int(input("Ingrese un numero: "))
    while True:
        numero += 1
        if primo(numero):
            break
    
    print(numero)


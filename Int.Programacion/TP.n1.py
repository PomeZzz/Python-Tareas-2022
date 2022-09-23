from ast import If, Num
from decimal import InvalidOperation
from threading import BrokenBarrierError


def ej1():
    numero_Uno=12
    numero_Dos=23
 
    print("promedio:" + str(numero_Uno + numero_Dos/2))
def ej2():
    import random
    num=random.randint(1, 10)
 
    x =int(input("Escribi un numero:"))
    print(num)
    if(num > x):
        print("Mi numero es mayor que el tuyo")
    elif(num < x):
        print("Mi numero es menor que el tuyo")
    elif(num == x):
        print("Adivinaste!")
def ej3():
    import random
    random_numero= random.randint(1, 1000)
    print(random_numero)
    while(True):
        
        numero_usuario = int(input("Ingrse su numero: "))
        
        if(numero_usuario > random_numero):
            print("Mi numero es menor que el tuyo")
        elif(numero_usuario < random_numero):
            print("Mi numero es mayor que el tuyo")
        elif(numero_usuario == random_numero):
            print("Adivinaste!!!!!!")
            break
    


ej3()


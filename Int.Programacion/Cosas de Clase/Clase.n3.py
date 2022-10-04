from audioop import mul
from cmath import sqrt
from itertools import product
from tkinter import END

def ej1():

    lista = [1,-3,5,-4,7,-7,-56,9]

    x=0

    while x < len(lista):
        print(lista[x])
        x=x+1
def ej2():
    lista = [1,-3,5,-4,7,-7,-56,9]
    
    for ix in range (len(lista)):
        print(lista[ix])
def ej3():
    lista = [1,-3,5,-4,7,-7,-56,9]
    
    for elem in lista:
        print(elem)
def ej4():
    lista = [1,-3,5,-4,7,-7,-56,9]
    
    for elem in lista:
        if elem > 0:
            print(elem , end= " ")
def ej5():
    lista = [1,-3,5,-4,7,-7,-56,9]
    
    multiplicacion = 1
    for elem in lista:
        if elem > 0:
            multiplicacion = multiplicacion*elem
    print(multiplicacion)
def diccionarios():
    # Diccionarios
    diccionario = {"clave":"valor" , "otra cosa":3}

    for clave,valor in diccionario.items():
        print()
def tarea_de_clase():
    precios = {"remeras": 125, "pantalon": 50, "zapatillas": 120}

    pedido = ["zapatillas", "remeras", "zapatillas"]

    cantidades = [2,3,7]
    
    
    print(sum(precios[x] for x in pedido))
def clase():
    precios = {"remeras": 125, "pantalon": 50, "zapatillas": 120}

    pedido = ["zapatillas", "remeras", "zapatillas"]

    suma = 0
    
    cantidades = [2,3,7]
    
    
    for x in range(len(cantidades)):
        
        suma = suma + precios[pedido[x]]*cantidades[x]

    
    print(suma)
clase()
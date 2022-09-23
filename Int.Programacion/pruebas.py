lista = ["mesa", "perro", "ooooooooo", "fsknslknvnslkf"]

longitud = 0
palabra = None

for x in lista:
    if len(x) > longitud:
        longitud = len(x)
        palabra = x
    
print(palabra)




def cuenta_Vocales(vocales):
    palabra = "hola"
    vocales = 0

    for x in palabra:
        if x == "a":
            vocales += 1
        elif x == "e":
            vocales += 1
        elif x == "i":
            vocales += 1
        elif x == "o":
            vocales += 1
        elif x == "u":
            vocales += 1
    return(vocales)

def comparador():
    lista = ["hola", "mercurio", "mouse","supercalifragilisticoespidalidoso", "avion"]
    
    for x in lista:
        for xi in x:
            if x == "a":
                vocales += 1
            elif x == "e":
                vocales += 1
            elif x == "i":
                vocales += 1
            elif x == "o":
                vocales += 1
            elif x == "u":
                vocales += 1

    print()
     

def cuentaVocalesLista(lista:list):
    lista = ["hola", "merco", "mouse","messi", "avion"]
    
    
    
    
    mayorvocales = 0
    stringmax = 0

    for i in lista:
        vocales = 0
        for x in i:
            if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
                vocales += 1
        if vocales > mayorvocales:
            stringmax = i
            mayorvocales = vocales
    return(stringmax)

print(cuentaVocalesLista(lista))

def cuentaVocalesLista(lista:list):
    lista = []
    
    cosas = input("ingresar las cosas que quiers en la lista: ")
    while cosas != "":
        lista.append(cosas)
        cosas = input("ingresar las cosas que quiers en la lista: ")
    
    mayorvocales = 0
    stringmax = 0

    for i in lista:
        vocales = 0
        for x in i:
            if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
                vocales += 1
        if vocales > mayorvocales:
            stringmax = i
            mayorvocales = vocales
    return(stringmax)

print(cuentaVocalesLista(lista))

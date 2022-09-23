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
     









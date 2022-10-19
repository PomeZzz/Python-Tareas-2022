def Eliminar_Numeros(lista, eliminados):
    for x in range(eliminados):
        lista.pop()
        lista.pop(0)
    return lista
        



def Crear_Lista():
    lista = []
    eliminados = int(input("Ingresar la cantidad de numero a eliminar: "))
    numeros = int(input("Ingresar un Valor: "))
    while numeros != "":
        lista.append(numeros)
        numeros = input("Ingresar un Valor: ")
    

    print(Eliminar_Numeros(lista, eliminados))

Crear_Lista()


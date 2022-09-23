from operator import index


def ej1():
    lst = [1, 4 , "El Colado", 2, 7]
    print(lst)
    ubicacion = lst.index("El Colado")
    del lst[ubicacion]

    lst.append("El Colado")
    print(lst)
def ej2():
    import random
    num = [random.randint(0,10) for x in range(0,100)]
    for elem in num:
        if elem >= 7:
            print(elem , end= " ")
def ej3():
    import random
    num = [23,54,56,87,98,76,54,34,32,34,63,756,242,112,12,21,9,5,53,87,98,90,87,554,76]
    
    maschico = min(num)
    ubicacion = num.index(min(num))

    print(maschico,ubicacion)

ej3()
    

from random import sample
from secrets import choice
def generar_mazo(n):
    mazo = sample(range(1,40), n)
    return mazo


def elegir_carta_de_mazo(mazo):
    cartas = choice(mazo)
    return(cartas)

def repartir_mano(mazo, n):
    cartas = []
    for x in range(n):
        c = elegir_carta_de_mazo(mazo)
        cartas.append(c)
    return(cartas)

def le_gana(carta1, carta2):    
    if carta1 > carta2:
        return True
    else:
        return False

def pruebas():    
    puntaje_primer_jugador = 0    
    puntaje_segundo_jugador = 0
    m = generar_mazo(20)

    print(m)

    l1 = repartir_mano(m,3)
    l2 = repartir_mano(m,3)
    print(l1,l2)
    k = le_gana(l1[0],l2[0])
    # usar un whilde hasta que la lista sea distinta de cero para hacer la comparacion de las cosas, por que la lista son tres cartas compara las primeras de cada lista y luego saca el primer valos, entonces el segundo vuelve a ser el primero




    print(k)


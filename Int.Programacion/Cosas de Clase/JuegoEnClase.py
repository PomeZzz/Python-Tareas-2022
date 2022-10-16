import random
cartas = [1,2,3,4,5,6,7,10,11,12]
palos = ("espada","basto","oro","copa")
def numero_de_carta_al_azar():
    numero = random.choice(cartas)
    palo = random.choice(palos)
    return(numero,palo)
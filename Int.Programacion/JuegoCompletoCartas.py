import CodigoCartas

m = CodigoCartas.generar_mazo(20)

l1 = CodigoCartas.repartir_mano(m,3)
l2 = CodigoCartas.repartir_mano(m,3)


puntaje_primer_jugador = 0    
puntaje_segundo_jugador = 0

while len(l1) != 0:
    
    if CodigoCartas.le_gana(l1[0],l2[0]):
        puntaje_primer_jugador += 1
    elif CodigoCartas.le_gana(l2[0],l1[0]):
        puntaje_segundo_jugador += 1
    l1.pop(0)
    l2.pop(0)

if puntaje_primer_jugador > puntaje_segundo_jugador:
    print("El Jugador 1 Gana con una puntuacion de: ",puntaje_primer_jugador)
else:
    print("El Jugador 2 Gana con una puntuacion de: ",puntaje_segundo_jugador)

print("Resultados:","\n payer 1:", puntaje_primer_jugador,"\nplayer 2:", puntaje_segundo_jugador)

#goed
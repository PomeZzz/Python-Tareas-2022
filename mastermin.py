import random

continuar = 1 
while continuar == 1:
    print("--- Bienvenido a MasterMind ---\n")
    print("Elija la dificultad en la que quiera jugar. 1=Facilito - 2=Complicadito - 3=TryHard\n")
    dificultad = int(input("Escriba el numero correspondiente del nivel a jugar: "))
    
    if dificultad == 1:
        cant_digitos = 3
    elif dificultad == 2:
        cant_digitos = 4
    elif dificultad == 3:
        cant_digitos = 6
    
    digitos = ["0","1","2","3","4","5","6","7","8","9"]
    codigo = ""
    # Esto esta para que no se repitan los numeros
    for i in range(cant_digitos):
        elegido = random.choice(digitos)
        while elegido in codigo:
            elegido = random.choice(digitos)
        codigo += elegido

    print("El codigo que tenes que adivinar tiene ", cant_digitos, "digitos\n")
    codigo_user = input("Que codigo estas pensando rey??: ")
    
    intentos = 1
    
    while codigo_user != codigo:
        intentos = intentos + 1
        aciertos = 0
        parecidos = 0
        for i in range(cant_digitos):
            if codigo_user[i] == codigo[i]:
                aciertos += 1
            elif codigo_user[i] in codigo:
                parecidos += 1
        print("El codigo que elegiste ", codigo_user, "tiene ", aciertos, "aciertos y ", parecidos, "parecido. Dedicate a otra cosa que esto no se te da bien >:/\n")
        codigo_user = input("Pone otro codigo: ")
    
    print("AGANASTE AMIGO POSTA SOS MUY BUENO TE FELICITO :DDD APARTE LO HICISTE EN ", intentos, "INTENTOS, no cualquiera te lo hace asi de rapidito.")
    continuar = input("Queres volver a jugar? si su respuesta es un si escriba el numero <1>, de lo contrario un <0> ")

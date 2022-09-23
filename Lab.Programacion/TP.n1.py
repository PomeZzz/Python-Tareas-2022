def ej1():
    Numero_Uno = int(input("Escribi Tu primer Numero:\n"))
    Numero_Unox10 = Numero_Uno*10 + Numero_Uno
    Numero_Unox100 = Numero_Uno*100 + Numero_Uno*10 + Numero_Uno
    print("Resultado de La suma es:\t" + str(Numero_Uno + (Numero_Unox10) + (Numero_Unox100)))
def ej2():
    print("Estrellita¿Donde Estas?\n\tMe pregunto quién serás\n\t\tEn el cielo o en el mar\nUn diamante de verdad")   
def ej3():
    ValorDeLaInversion = int(input("Ingresar el valor a invertir:\n"))
    AñosDeInversion = int(input("Ingrsar la cantidad de años que quieras dejar tu inversion:\n"))
    InteresesAnuales = int(input("Ingresar la tasa de intereses:\n"))
    Ganancia = (((AñosDeInversion*12)*100)%ValorDeLaInversion)


    print("Este es el capital obtenido en la inversion:\n" + str(Ganancia))
def ej4():
    z =input("Escriba su Nombre:\n")
    x =input("Escriba su apellido:\n")


    print("Tu nombre y apellido son:\n" + x + " " + z) 
def ej5():
    UsoDeSplit = "Esto. Es. Una. Prueba. Del .Funcionamiento. De. Split"

    NombreDeLaLista = UsoDeSplit.split(".")

    print(NombreDeLaLista[2])
def ej6():
    from ssl import PEM_cert_to_DER_cert


    PayasosVendidos = int(input("Ingresar la cantidad de Payasos vendidos:\n"))
    MuñecasVendidas = int(input("Ingrsar la cantidad de Muñecas vendidas:\n"))

    PesoDeLosPayasos = PayasosVendidos*112
    PesoDeLasMuñecas = MuñecasVendidas*75


    print("Este es el peso del paquete de Payasos:\n" + str(PesoDeLosPayasos) + "g")
    print("Este es el peso del paquete de las Muñecas:\n" + str(PesoDeLasMuñecas) + "g")
ej6()
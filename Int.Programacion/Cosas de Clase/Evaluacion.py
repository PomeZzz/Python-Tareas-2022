from operator import index
from pdb import Restart
from warnings import resetwarnings
cajas = [2,3,5,1,2,3]
cant = 5
resta = 3
def imprimir(cajas):
    ubicacion = 0
    for x in cajas:
        print(ubicacion, "Tiene", x)
        ubicacion += 1
#Modifique mi idea inicial que era utilizar un index, gracias a un foro, me base en una isea crada
def encontrar(cajas, cant):
    valor1 = 0
    valor2 = 0
    for x in cajas:
        valor1 = x
        if valor1 > cant:
            i = valor2
        valor2 += 1
    return i 

def acomodar(cajas):
    cartas = encontrar(cajas,resta)
    numero = (cajas[cartas])
    for x in range(cajas)
    # Mi idea principal era recorrer la lista una vez y verificar cada valor que este adyacente hasta tres numero a la derecha del asigando y sumarle los 3 numero que le saque al asignado

    

# Las operaciones parciales son aquellas que tienen precondiciones es decir que cuentan con condiciones para su correcto funcionamiento, de lo contrario se la concidera operacion total
# Si en este trabajo hay operaciones parciales ya que sin su parametro no funcionan, claro que hay casos que no funcionan por ejemplo si yo le asigno un valor != int por ejemplo una letra este no funcionara ya que esta hecho para valores numericos
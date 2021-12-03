"""
Reglas:
Tenemos n piedras y hay dosjugadores los cuales deberán intentar quitar todas las piedras para poder ganar.
Movimientos:
-quitar tres piedraa
-quitar dos piedras
-quitar cinco piedras
Siempre empezará el jugador uno.
  
"""
import random
piedras = random.randint(1,9)
print(piedras)
print ("Empieza jugando el jugardo 1")
def repartir(piedras):
    if piedras >= 5:
        jugador = 5
    elif piedras < 5 or piedras >= 3:
        jugador = 3
    elif piedras == 2: 
        jugador = 2
    else:
        jugador = 0
    return jugador

print("Piedras del jugador 1:")
jugador1 = repartir(piedras)
print("Piedras del jugador 2")


while piedras >=5:
    print("Jugador 1 coge 5 piedras")
    piedras_totales = piedras - 5
    print(piedras_totales)
    if piedras_totales == 5:
        print("Jugador 2 gana")
    elif piedras_totales == 3:
        print("Jugador 2 coge 3 piedras")
        piedras_totales = piedras_totales - 3
        print(piedras_totales)
        print("Jugador 2 gana")
    elif piedras_totales == 2:
        print("Jugador 2 coge 2 piedras")
        piedras_totales = piedras_totales - 2
        print(piedras_totales)
        print("Jugador 2 gana")
    else:
        print("Jugador 1 gana")
    
    break

while piedras < 5:
    if piedras == 4 or 3:
        print("Jugador 1 coge 3 piedras")
        piedras_totales = piedras - 3
        print (piedras_totales)
        print("Jugador 1 gana")
    elif piedras == 2:
        print("Jugador 1 coge 2 piedras")
        piedras_totales = piedras - 2
        print(piedras_totales)
        print("Jugador 1 gana")
    else: 
        print("Jugador 2 gana")
    break
        

        
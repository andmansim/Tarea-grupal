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
piedras = 1
print(piedras)
print ("Empieza jugando el jugardo 1")
def repartir(p):
    if p >= 5:
        jugador = 5
        
    elif p < 5 and p >= 3:
        jugador = 3
        
    elif p == 2: 
        jugador = 2
        
    else:
        jugador = p
    return jugador

while piedras > 0:
    print("Piedras del jugador 1:")
    jugador1 = repartir(piedras) 
    print(jugador1)
    piedras = piedras - jugador1
    if jugador1 < 2:
        print("Jugador 1 pierde")
        break
    elif piedras == 0:
        print("Jugador 2 pierde")
        break
    print("Piedras del jugador 2")
    jugador2 = repartir(piedras)
    piedras = piedras - jugador2
    print(jugador2)
    if jugador2 < 2:
        print("Jugador 2 pierde")
        break
    elif piedras == 0:
        print("Jugador 1 pierde")
        break

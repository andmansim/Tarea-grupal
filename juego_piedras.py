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
piedras = random.randint(1,8)
print(piedras)
print ("Empieza jugando el jugardo 1")

while piedras >=5:
    piedras_totales = piedras - 5
    if piedras_totales == 5:
        print("Jugador 1 gana")
    elif piedras_totales == 3 or 2:
        print("Jugador 2 gana")
    else:
        print("Jugador 1 gana")
    
    break

while piedras < 5:
    if piedras == 4 or 3:
        piedras_totales = piedras - 3
        print("Jugador 1 gana")
    elif piedras == 2:
        piedras_totales = piedras - 2
        print("Jugador 1 gana")
    else: 
        print("Jugador 2 gana")
    break
        

        
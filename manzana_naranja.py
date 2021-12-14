
# distancia casa: s y t
# manzano: a
#naranjo: b
import random
s = (7)
t = (11)
b = (15)
a = (5)
distancia_casa = [s,t]
distancia_arboles = [a,b]
manzanas_lista = []
naranjas_lista = []

def lanzamiento_manzana():
    j = random.randint(0,11)
    return j

def lanzamiento_naranja():
    h = random.randint(7,20)
    return h


posicion_manzana = lanzamiento_manzana()

posicion_naranja = lanzamiento_naranja()

print("Posición de una manzana:")
print(posicion_manzana)
print("Posición de una naranja:")
print(posicion_naranja)

def manzana ():
    if posicion_manzana < 5:
        distancia_manzana = a - posicion_manzana
    elif posicion_manzana > 5:
        distancia_manzana = posicion_manzana - a
    else:
        distancia_manzana = 0
    return distancia_manzana

def naranja ():
    if posicion_naranja < 15:
        distancia_naranja = b - posicion_naranja
    elif posicion_naranja > 15:
        distancia_naranja = posicion_naranja - b
    else:
        distancia_naranja = 0
    return distancia_naranja


#objetivo: print(numero de manzanas que caen dentro de la casa)
         # print(numero de naranjas que caen dentro de la casa)

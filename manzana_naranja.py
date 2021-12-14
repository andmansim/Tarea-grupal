
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

def lanzamiento_manzana():
    j = random.randint(0,11)
    return j

def lanzamiento_naranja():
    h = random.randint(7,20)
    return h


distancia_manzana = lanzamiento_manzana()

distancia_naranja = lanzamiento_naranja()

print("Distancia de una manzana:")
print(distancia_manzana)
print("Distancia de una naranja:")
print(distancia_naranja)

#objetivo: print(numero de manzanas que caen dentro de la casa)
         # print(numero de naranjas que caen dentro de la casa)

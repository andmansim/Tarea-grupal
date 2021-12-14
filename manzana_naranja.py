
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




def manzana (posicion_manzana):
    if posicion_manzana != 5:
        distancia_manzana = posicion_manzana - a
    else:
        distancia_manzana = 0
    return distancia_manzana

def naranja (posicion_naranja):
    if posicion_naranja != 15:
        distancia_naranja = posicion_naranja - b
    else:
        distancia_naranja = 0
    return distancia_naranja

contador = 10
while contador != 0:
    posicion_m = lanzamiento_manzana()
    print("Posición de las manzanas")
    print(posicion_m)
    posicion_n = lanzamiento_naranja()
    print("Posición de las naranjas")
    print(posicion_n)
    
    m = manzana(posicion_m)
    manzanas_lista.append(m)
    print("Lista de las manzanas")
    print(manzanas_lista)
    n = naranja(posicion_n)
    naranjas_lista.append(n)
    print("Lista de las manzanas")
    print(naranjas_lista)
    
    total_manzanas = 0
    if 7 < posicion_m < 11:
        total_manzanas = total_manzanas + 1
        print("Manzanas en la casa")
        print(total_manzanas)

    total_naranjas = 0
    if 7 < posicion_n < 11:
        total_naranjas = total_naranjas + 1  
        print("Manzanas en la casa")
        print(total_naranjas)
    
    contador = contador - 1

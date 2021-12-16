import random
from functools import reduce
import operator

laberinto = [
    ['I', 'X', 'X', 'B', 'X', 'X'],
    [' ', 'X', ' ', ' ', ' ', ' '],
    [' ', 'B', ' ', 'B', 'T2', ' '],
    [' ', ' ', ' ', 'X', ' ', ' '],
    [' ', ' ', ' ', 'X', ' ', ' '],
    ['T2', 'T1', ' ', 'T1', ' ','S']
    ]

#listas con las coordenadas correspondientes, necesarias para imprimir el laberinto
muro = ((0,1), (0,2), (0,4), (0,5), (1,1), (3,3), (4,3))
bomba = ((0,3),(2,1),(2,3))
teletransporte_1 = ((5,1), (5,3))
teletransporte_2 = ((5,0), (2,4)) 
inicio = ((0,0))
salida = ((5,5))

#listas vacias que se usan en distntas funciones
solucion = []
lab =[]

#listas de probabilidades necesarias para calcular la probabilidad en la funcion 'probabilidad'
prob_tres_cuartos = [(3, 1), (1, 4), (2, 4), (3, 4), (4, 4), (3, 2), (4, 2)]
prob_dos_tercios = [(1, 0), (2, 0), (1, 5), (2, 5), (5, 3)]
prob_uno = [(3, 0), (4, 0), (5, 0), (5, 1), (4, 1), (5, 4), (5, 2), (3, 5), (4, 5), (5, 5)]
prob_un_medio = [(0,0), (1, 2), (2, 2), (1, 3)]
prob_muerte = [(2, 1), (0, 3), (2, 3)]

#funcion que crea el laberinto
def creacionlab():
        fila = []
        for i in range(0,6): #line
                for j in range(0,6): #column             
                        if tuple([i,j]) in muro:
                                fila.append("X")
                        elif tuple([i,j]) in bomba:
                                fila.append("B")
                        elif tuple([i,j]) in teletransporte_1:
                                fila.append("T1")
                        elif tuple([i,j]) in teletransporte_2:
                                fila.append("T2")
                        elif tuple([i,j]) in inicio:
                                fila.append("I")
                        elif tuple([i,j]) in salida:
                                fila.append("S")
                        else:
                                fila.append(" ")
                lab.append (fila)
                fila = []



#funcion que calcula aleatoriamente el siguiente movimiento de la rana
def calcular_siguiente(posicion_actual): 
        coordenada = [] 
        x = posicion_actual[0] 
        y = posicion_actual[1]
        
        while coordenada == []:
            a = random.randint(1, 4)
            prob = Probabilidad(x, y)
            if a == 1:
                    if arriba(x, y) == True:
                            coordenada.append(x-1) 
                            coordenada.append(y) 
            elif a == 2:
                    if abajo(x, y) == True: 
                            coordenada.append(x+1) 
                            coordenada.append(y) 
            elif a == 3: 
                    if izquierda(x, y) == True: 
                            coordenada.append(x) 
                            coordenada.append(y-1) 
            elif a == 4:
                    if derecha(x, y) == True: 
                            coordenada.append(x) 
                            coordenada.append(y+1)
            if prob != 0:
                solucion.append(prob) 
                    
        return coordenada, prob

#las proximas 4 funciones indican si es posible o mover en la direccion que indican
def arriba(x, y): 
        if x > 0 and x < 5: 
                if laberinto[x-1][y] != "X": 
                        return True
        return False

def abajo(x, y): 
        if x >= 0 and x < 4: 
                if laberinto[x+1][y] != "X":
                        return True
        return False 

def derecha(x, y): 
        if y >= 0 and y < 4: 
                if laberinto[x][y+1] != "X":
                        return True
        return False 

def izquierda(x, y): 
        if y > 0 and y <= 5: 
                if laberinto[x][y-1] != "X":
                        return True
        return False

#funcion que calcula la probabilidad
def Probabilidad(x,y):
    if estaEnLista(x, y, prob_tres_cuartos) == True:
        prob = 3/4
    elif estaEnLista(x, y, prob_dos_tercios) == True:
        prob = 2/3 
    elif estaEnLista(x, y, prob_uno) == True:
        prob = 1
    elif estaEnLista(x, y, prob_un_medio) == True:
        prob = 1/2
    elif estaEnLista(x, y, prob_muerte) == True:
                prob = 0
                                                
    return prob

#funcion que indica si una pareja de numeros pertenece a una lista o no, necesaria para la funcion probabilidad
def estaEnLista(numA, numB, lista): 
        for x in range(len(lista)): 
                if lista[x][0] == numA and lista[x][1] == numB: 
                        return True 
        return False

#CODIGO PRINCIPAL
#creacionlab()
#for x in lab:
#    print(" ".join(x))
posicion_actual = [0,0]
x = posicion_actual[0]
y = posicion_actual[1]
prob = 10
while laberinto[x][y] != "S" and prob != 0: 
        posicion_siguiente, prob = calcular_siguiente(posicion_actual)
        print("posicion_siguiente " + str(posicion_siguiente))
        print("prob " + str(prob))
        posicion_actual[0] = posicion_siguiente[0] 
        posicion_actual[1] = posicion_siguiente[1] 
        x = posicion_actual[0] 
        y = posicion_actual[1]
        if estaEnLista(posicion_actual[x], posicion_actual[y], teletransporte_1) == True:
                if posicion_actual[0] == 5 and posicion_actual[1] == 1:
                        posicion_actual[0] = 5
                        posicion_actual[1] = 3
                if posicion_actual[0] == 5 and posicion_actual[1] == 3:
                        posicion_actual[0] = 5
                        posicion_actual[1] = 1

        elif estaEnLista(posicion_actual[x], posicion_actual[y], teletransporte_2) == True:
                if posicion_actual[0] == 5 and posicion_actual[1] == 0:
                        posicion_actual[0] = 2
                        posicion_actual[1] = 4
                if posicion_actual[0] == 2 and posicion_actual[1] == 4:
                        posicion_actual[0] = 5
                        posicion_actual[1] = 0
    

leche = reduce(operator.mul,solucion)
print (str(leche))


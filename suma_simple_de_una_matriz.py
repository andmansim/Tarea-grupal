#matriz = [["", " ", ""],
          #["", "", ""], 
          #["", "", ""]]

import random
   
matriz =[]

def creacionmatriz(n,m):
        fila = []
        for i in range(n,m): #linea
            for j in range(n,m): #columna
                
                a = random.randint(0,100)
                fila.append(a)
                
            matriz.append (fila)
            fila = []
           
creacionmatriz(0,3)
 
for x in matriz:
    print(" ".join(str(x)))

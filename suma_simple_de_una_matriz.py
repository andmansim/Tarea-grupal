import random
  
matriz =[]

def creacionmatriz(n,m):
        fila = []
        h = 0
        for i in range(n,m): #linea
            for j in range(n,m): #columna
                
                a = random.randint(0,100)
                fila.append(a)
                h = h + a 
            matriz.append (fila)
            fila = []
            
        return(h)
suma = creacionmatriz(0,3)  # Dimensiones de la matriz y donde nos añade el valor final

# Para unir las listas que forma a la principal

for x in matriz:
    print(" ".join(str(x)))

print(suma)


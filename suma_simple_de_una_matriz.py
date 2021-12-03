#matriz = [["", " ", ""],
          #["", "", ""], 
          #["", "", ""]]
matriz = []
posiciones = ((0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2))
def creacionmatriz():
    fila = []
    for i in range (0,2):
        for j in range (0,2):
            if tuple([i,j]) in posiciones:
                fila.append (" ")
        
        matriz.append (fila)
        matriz = []

creacionmatriz()

for x in matriz:
    print(",".join(x))
    



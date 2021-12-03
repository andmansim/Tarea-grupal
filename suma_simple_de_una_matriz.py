#matriz = [["", " ", ""],
          #["", "", ""], 
          #["", "", ""]]

posiciones = ((0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2))

matriz=[]
def creacionmatriz():
        fila=[]
        for i in range(0,3): #linea
                for j in range(0,3): #columna
                                      
                    if tuple([i,j]) in posiciones:
                        fila.append(" ")
                    else:
                        fila.append("a")
                matriz.append(fila)
                matriz=[]
creacionmatriz()
 
for x in matriz:
    print(",".join(x))
    



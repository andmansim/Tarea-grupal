#matriz = [["", " ", ""],
          #["", "", ""], 
          #["", "", ""]]

posiciones = ((0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2))
   
lab=[]
def mazecreation():
        maze = []
        for i in range(0,3): #line
                for j in range(0,3): #column
                                      
                        if tuple([i,j]) in posiciones:
                                maze.append("X")
                        else:
                                maze.append(" ")
                lab.append (maze)
                maze = []
mazecreation()
 
for x in lab:
    print(",".join(x))


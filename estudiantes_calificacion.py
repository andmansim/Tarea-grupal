import random

notas = []
mulriplos_5 = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

def calificaciones():
    
    calificacion = random.randint(0,100)
    notas.append(calificacion)
 
    
    
y = 0
while y < 5:

    d = calificaciones()
    y = y + 1
print("Notas iniciales")
print(notas)
notas.sort()
print(notas)
suspensos = []
for i in range (0,5):
    if notas[i] < 40:
        suspensos.append(notas[i])
    else:
        print("b")
print(suspensos)


import random

notas = []
mulriplos_5 = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

def calificaciones():
    
    calificacion = random.randint(0,100)
    notas.append(calificacion)
    
# Para conseguir un múltiplo de 5 mayor que la nota
def redondear(x, base):
    a = base * round(x/base)
    if a < x:
        a = a + 5
    return a


    
y = 0
while y < 5:

    d = calificaciones()
    y = y + 1
print("Notas iniciales")
print(notas)
notas.sort()
print(notas)
suspensos = []
aprobados = []

for i in range (0,5):
    if notas[i] < 40:
        suspensos.append(notas[i])
    else:
        aprobados.append(notas[i])
    
print(suspensos)
print(aprobados)

contador = 0
while contador != 6 or aprobados != []:
    print(redondear(aprobados[0],5))
    aprobados.pop(0)
    contador = contador + 1
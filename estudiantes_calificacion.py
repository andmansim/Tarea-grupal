import random
notas_totales = []
def calificaciones():
    notas = []
    calificacion = random.randint(0,100)
    notas.append(str(calificacion))
    notas_totales.append(notas)
    for x in notas_totales:
        print(",".join(x))
    return notas
print(calificaciones())



import random
claridadA = random.randint(0, 100)
originalidadA = random.randint(0, 100)
dificultadA = random.randint(0, 100)
claridadB = random.randint(0, 100)
originalidadB = random.randint(0, 100)
dificultadB = random.randint(0, 100)
a = [claridadA, originalidadA, dificultadA]
b = [claridadB, originalidadB, dificultadB]
Lucia = []
Carlos = []

#funcion para sumar las puntuaciones
def suma_puntuacion(lista):
    lista.append(1)


#codigo principal
if a[0] > b[0]:
    suma_puntuacion(Lucia)
    print(str(a[0]) + " es mayor que " + str(b[0]) + ", por lo que Lucia se lleva un punto.")
elif a[0] < b[0]:
    suma_puntuacion(Carlos)
    print(str(a[0]) + " es menor que " + str(b[0]) + ", por lo que Carlos se lleva un punto.")
if a[1] > b[1]:
    suma_puntuacion(Lucia)
    print(str(a[1]) + " es mayor que " + str(b[1]) + ", por lo que Lucia se lleva un punto.")
elif a[1] < b[1]:
    suma_puntuacion(Carlos)
    print(str(a[1]) + " es menor que " + str(b[1]) + ", por lo que Carlos se lleva un punto.")
if a[2] > b[2]:
    suma_puntuacion(Lucia)
    print(str(a[2]) + " es mayor que " + str(b[2]) + ", por lo que Lucia se lleva un punto.")
elif a[2] < b[2]:
    suma_puntuacion(Carlos)
    print(str(a[2]) + " es menor que " + str(b[2]) + ", por lo que Carlos se lleva un punto.")
else:
    Lucia.append(0)
    Carlos.append(0)
    print("Los valores son iguales, por lo que nadie se lleva puntos.")

puntuacion_total_Lucia = sum(Lucia)
puntuacion_total_Carlos = sum(Carlos)
print("La puntuacion total de lucia: " +str(puntuacion_total_Lucia))
print("La puntuacion total de carlos: " +str(puntuacion_total_Carlos))

puntuacion_final = [puntuacion_total_Lucia, puntuacion_total_Carlos]
print(puntuacion_final)


aprobados = [56, 67, 56]
print(aprobados)
def myround(x, base):
    a = base * round(x/base)
    if a < x:
        a = a + 5
    return a

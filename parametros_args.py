def calcular_perimetro (*args):
    perimetro = 0
    for lado in args:
        perimetro+=lado
    return perimetro

perimetro = calcular_perimetro (3,4)
print(perimetro)
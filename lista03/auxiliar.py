import math

def distanciaEuclidiana(xi, xj):
    soma = 0
    for i in range(len(xi)):
        soma += math.pow(xi[i] - xj[i], 2)
    return math.sqrt(soma).__round__(2)


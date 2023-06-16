import math
import statistics
import numpy as np


def distanciaEuclidiana(xi, xj):
    soma = 0
    for i in range(len(xi)):
        soma += math.pow(xi[i - 1] - xj[i - 1], 2)
    return math.sqrt(soma).__round__(2)

def distanciaMinkowski(xi, xj, p):
    soma = 0
    for i in range(len(xi)):
        soma += math.pow(abs(xi[i - 1] - xj[i - 1]), p)
    return math.pow(soma, (1/p))


'''
    xi, yi => treino
    xt, yt => teste
'''
def vizinhoMaisProximo(x_treino, y_treino, x_teste):
    dmin = 99999999999
    imin = 0
    classification = []
    for j in range(len(x_teste)):
        for i in range(len(x_treino)):
            #print("DISTANCIA: " + str(distanciaEuclidiana(x_treino[i], x_teste[j])))
            if distanciaEuclidiana(x_treino[i], x_teste[j]) < dmin:
                dmin = distanciaEuclidiana(x_treino[i], x_teste[j])
                imin = i
                #print("MATCH! " + str(y_treino[imin]) + "EM: " + str(imin))
        dmin = 99999999999 #Necessario para dar o reset a cara incremento do conjunto de teste, pra assim ser possivel
                            # adicionar
        classification.append(y_treino[imin])
    return classification


def vizinhoMaisProximoMinkowski(x_treino, y_treino, x_teste, p):
    dmin = 99999999999
    imin = 0
    classification = []
    for j in range(len(x_teste)):
        for i in range(len(x_treino)):
            if distanciaMinkowski(x_treino[i], x_teste[j], p) < dmin:
                dmin = distanciaMinkowski(x_treino[i], x_teste[j], p)
                imin = i
        dmin = 99999999999#Necessario para dar o reset a cara incremento do conjunto de teste, pra assim ser possivel
                            # adicionar
        classification.append(y_treino[imin])
    return classification
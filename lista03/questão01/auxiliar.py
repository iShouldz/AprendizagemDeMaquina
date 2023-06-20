import math
import statistics
import numpy as np
from scipy.spatial import distance


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
    classificationdata = []
    classData = []
    for j in range(len(x_teste)):
        classData.append(classificationdata)
        #print("\n")
        for i in range(len(x_treino)):
            #print("DISTANCIA: " + str(distanciaEuclidiana(x_treino[i], x_teste[j])))
            data = [distanciaEuclidiana(x_treino[i], x_teste[j]), y_treino[i]]
            classificationdata.append(data)
            if distanciaEuclidiana(x_treino[i], x_teste[j]) < dmin:
                dmin = distanciaEuclidiana(x_treino[i], x_teste[j])
                imin = i
                #print("MATCH! " + str(y_treino[imin]) + "EM: " + str(imin))
        dmin = 99999999999
        classificationdata = []
        classification.append(y_treino[imin])
    '''
    print(classificationdata)
    print(classData[0])
    print(classData[1])
    print(classData[2])'''
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
        dmin = 99999999999
        classification.append(y_treino[imin])
    return classification

def knn(x_treino, y_treino, x_teste, k, peso):
    if(k == 1):
        return vizinhoMaisProximo(x_treino, y_treino, x_teste)
    else:
        dmin = 99999999999
        imin = 0
        classification = []
        classificationdata = []
        classData = []
        for j in range(len(x_teste)):
            # classdata possui todas as distancias
            classData.append(classificationdata)
            for i in range(len(x_treino)):
                data = [distanciaEuclidiana(x_treino[i], x_teste[j]), y_treino[i]]
                classificationdata.append(data)
                if distanciaEuclidiana(x_treino[i], x_teste[j]) < dmin:
                    dmin = distanciaEuclidiana(x_treino[i], x_teste[j])
                    imin = i
            dmin = 99999999999
            classificationdata = []
            classification.append(y_treino[imin])
        knn = ordenarVetor(classData, k)
        """
        Se peso == false, sem peso; Se true, com peso
        """
        if not peso:
            return verificarPresenca(knn)
        else:
            return verificarPresencaPeso(knn)


def ordenarVetor(arrayDistancias, k):
    novoArray = []
    novoArray2 = []
    final = []
    menor = 9999999999
    for j in range(len(arrayDistancias)):
        novoArray2.append(novoArray)
        for i in range(len(arrayDistancias[0])):
            novoArray.append(arrayDistancias[j][i][0])
        novoArray = []
    for j in range(len(novoArray2)):
        novoArray2[j].sort()
    #print("Sem remoção: ", arrayDistancias)
    for p in range(len(arrayDistancias)):
        arrayDistancias[p].sort()
        del arrayDistancias[p][k:]
    #print("arraydistancia: ", arrayDistancias)
    return arrayDistancias

#Retorna a moda dos elementos
def verificarPresenca(arrayDistancias):
    vetor = []
    vetor2 = []
    vetorfinal = []
    for i in range(len(arrayDistancias)):
        vetor2.append(vetor)
        for j in range(len(arrayDistancias[0])):
           vetor.append(arrayDistancias[i][j][1])
        vetor = []

    #print(len(vetor2))
    #print("vetor final: ",vetor2)
    #len(vetor2) ==> o valor de k
    for l in range(len(vetor2)):
        moda = statistics.mode(vetor2[l])
        vetorfinal.append(moda)
    #print("vetor modal: ", vetorfinal)
    #Retorna a classificação de acordo com a moda
    return vetorfinal

def verificarPresencaPeso(arrayDistancias):
    vetor = []
    saida = []
    vetor2 = []
    resultado = []
    for i in range(len(arrayDistancias)):
        vetor2.append(vetor)
        for j in range(len(arrayDistancias[0])):
            if(arrayDistancias[i][j][0] == 0):
                vetor.append([arrayDistancias[i][j][0], arrayDistancias[i][j][1]])
            else:
                vetor.append([1/(arrayDistancias[i][j][0]), arrayDistancias[i][j][1]])
        vetor = []

    for i in range(len(vetor2)):
        for j, k in zip(range(0, len(arrayDistancias[i])), range(1, len(arrayDistancias[i]))):
            if arrayDistancias[i][j][1] == arrayDistancias[i][k][1]:
                saida.append([vetor2[i][k][0] + vetor2[i][j][0], arrayDistancias[i][j][1]])

    """
    depois de pegar a soma das saidas, remove o valor inicial que tem o valor soma primario, adiciona ao 
    fim do vetor resultante a soma, ordena pois assim vou ter a classe com maior peso e adiciono ao meu vetor
    de resultado o ultimo elemento que é a saida e retorno
    """
    for i in range(len(vetor2)):
        vetor2[i].remove(vetor2[i][0])
        vetor2[i].append(saida[i])
        vetor2[i].sort()
        resultado.append(vetor2[i][1][-1])
    return resultado





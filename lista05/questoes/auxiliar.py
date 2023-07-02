import math

from sklearn.datasets import load_wine, load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

x, y = load_iris(return_X_y=True)

def holdout100():
    holdout = []
    holdoutSemColuna = []
    for i in range(100):
        """100 holdout 50/50 base wine completa"""
        x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5, train_size=0.5)
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(verificarAcerto(resultado, y_teste))

        """100 holdout 50/50 base wine sem a última coluna"""
        x_treino2 = x_treino
        x_teste2 = x_teste
        x_treino2, x_teste2 = removerUltimaColuna(x_treino2, x_teste2)
        knn2 = KNeighborsClassifier(n_neighbors=1)
        knn2.fit(x_treino2, y_treino)
        resultado = knn2.predict(x_teste2)
        holdoutSemColuna.append(verificarAcerto(resultado, y_teste))

    return holdout, holdoutSemColuna

def verificarAcerto(arrayClassificadoByKNN, arrayClassificadoTeste):
    contador = 0
    for i in range(len(arrayClassificadoByKNN)):
        if arrayClassificadoByKNN[i] == arrayClassificadoTeste[i]:
            contador += 1
    return (contador / len(arrayClassificadoByKNN) * 100).__round__(2)

def removerUltimaColuna(x_treino, x_teste):
    novoXTreino = []
    novoXTeste = []
    for i in range(len(x_teste)):
        novoXTreino.append(np.delete(x_treino[i], [0]))
        novoXTeste.append(np.delete(x_teste[i], [0]))
    return novoXTreino, novoXTeste

def remover12Coluna(x_treino, x_teste):
    novoXTreino = []
    novoXTeste = []
    for i in range(len(x_teste)):
        novoXTreino.append(np.delete(x_treino[i], [0, 1]))
        novoXTeste.append(np.delete(x_teste[i], [0, 1]))
    return novoXTreino, novoXTeste

def diferencaTaxaDeAcerto(vetorA, vetorB):
    vetorDiferenca = []
    for i in range(len(vetorA)):
        resultado = vetorA[i] - vetorB[i]
        vetorDiferenca.append(resultado)
    return vetorDiferenca

def mediaamostra(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    return soma/len(vetor)

def calcular_desvio_padrao_amostral(dados):
    media = mediaamostra(dados)
    soma_diferencas_quadrado = sum((x - media) ** 2 for x in dados)
    variancia = soma_diferencas_quadrado / (len(dados) - 1)
    desvio_padrao = math.sqrt(variancia)
    return desvio_padrao

def desviopadraoamostral(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += math.pow(vetor[i] - mediaamostra(vetor), 2)
    return soma/len(vetor)

def intervaloDeConfianca(vetor):
    media = mediaamostra(vetor)
    desvio = calcular_desvio_padrao_amostral(vetor)
    ladoa = (media - 1.96 * desvio)
    ladob = (media + 1.96 * desvio)

    return "[" + str(ladoa) + "; " + str(ladob) + "]"


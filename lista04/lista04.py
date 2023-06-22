"""
Realize um Holdout com 1-NN (distância Euclidiana), utilizando 70% dos dados
para treinamento e o restante (30%) para teste na base de dados Wine archive.ics.uci.
edu/ml/datasets/Wine. Você precisa mostrar como calculou cada métrica, não pode utilizar
biblioteca que já calcula a métrica diretamente, mas pode utilizar biblioteca para o 1-NN e para
dividir os dados entre treino e teste.
"""

import lista04auxiliar
from sklearn.neighbors import KNeighborsClassifier
classes = [0, 1, 2]

holdoutXTreino, holdoutYTreino, holdoutXTeste, holdoutYTeste = lista04auxiliar.holdout()

resultado = KNeighborsClassifier(n_neighbors=1)
resultado.fit(holdoutXTreino, holdoutYTreino)
resultado.predict(holdoutXTeste)
print((resultado.score(holdoutXTeste, holdoutYTeste) * 100).__round__(2))

matriz = lista04auxiliar.matrizConfusao(holdoutYTeste, resultado.predict(holdoutXTeste))
acuracia = lista04auxiliar.taxaDeAcerto(matriz, holdoutXTeste)
recallbyclass = lista04auxiliar.recallByclass(matriz, 1)
precisaobyclass = lista04auxiliar.precisaByclass(matriz, 1)
medidaF = lista04auxiliar.medidaFbyClass(precisaobyclass, recallbyclass)

print("Matriz de confusão: ")
lista04auxiliar.exibirMatrizConfusao(holdoutYTeste, resultado.predict(holdoutXTeste), classes)
print("Recall por classe(classe 1): ", recallbyclass)
print("Taxa de acerto: ", acuracia)
print("Precisão por classe(classe 1): ", precisaobyclass)
print("Medida F por classe(classe 1): ", medidaF)

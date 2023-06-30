"""
Realize um Holdout com 1-NN (distância Euclidiana), utilizando 70% dos dados
para treinamento e o restante (30%) para teste na base de dados Wine archive.ics.uci.
edu/ml/datasets/Wine. Você precisa mostrar como calculou cada métrica, não pode utilizar
biblioteca que já calcula a métrica diretamente, mas pode utilizar biblioteca para o 1-NN e para
dividir os dados entre treino e teste.
"""

import lista04auxiliar
import sklearn.metrics as metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import multilabel_confusion_matrix

classes = [0, 1, 2]


# Exemplo de rótulos reais e previstos
y_true = [0, 1, 0, 1, 1, 2, 0, 2]
y_pred = [0, 1, 0, 1, 0, 2, 1, 2]



holdoutXTreino, holdoutYTreino, holdoutXTeste, holdoutYTeste = lista04auxiliar.holdout()

resultado = KNeighborsClassifier(n_neighbors=1)
resultado.fit(holdoutXTreino, holdoutYTreino)
resultado.predict(holdoutXTeste)

matriz = lista04auxiliar.matrizConfusao(holdoutYTeste, resultado.predict(holdoutXTeste))
acuracia = lista04auxiliar.taxaDeAcerto(matriz, holdoutXTeste)

recallbyclass0 = lista04auxiliar.recallByclass(matriz, 0)
recallbyclass1 = lista04auxiliar.recallByclass(matriz, 1)
recallbyclass2 = lista04auxiliar.recallByclass(matriz, 2)

precisaobyclass0 = lista04auxiliar.precisaByclass(matriz, 0)
precisaobyclass1 = lista04auxiliar.precisaByclass(matriz, 1)
precisaobyclass2 = lista04auxiliar.precisaByclass(matriz, 2)

medidaF0 = lista04auxiliar.medidaFbyClass(precisaobyclass0, recallbyclass0)
medidaF1 = lista04auxiliar.medidaFbyClass(precisaobyclass1, recallbyclass1)
medidaF2 = lista04auxiliar.medidaFbyClass(precisaobyclass2, recallbyclass2)

taxaFP0 = lista04auxiliar.taxaFP(matriz, 0)
taxaFP1 = lista04auxiliar.taxaFP(matriz, 1)
taxaFP2 = lista04auxiliar.taxaFP(matriz, 2)

print("Matriz de confusão: ")
lista04auxiliar.exibirMatrizConfusao(holdoutYTeste, resultado.predict(holdoutXTeste), classes)

"""Uso da biblioteca para comparação"""
recallReal = metrics.recall_score(holdoutYTeste, resultado.predict(holdoutXTeste), average=None)
print("RECALL biblioteca: ", recallReal)
print("==================================")
precisaoReal = metrics.precision_score(holdoutYTeste, resultado.predict(holdoutXTeste), average=None)
print("PRECISAO biblioteca: ", precisaoReal)
print("==================================")
medidaFReal = metrics.f1_score(holdoutYTeste, resultado.predict(holdoutXTeste), average=None)
print("MEDIDA F biblioteca: ", medidaFReal)
print("==================================")
cm = matriz
fpr_class_0 = cm[0][1] / (cm[0][1] + cm[0][0] + cm[0][2])
fpr_class_1 = cm[1][0] / (cm[1][0] + cm[1][1] + cm[1][2])
fpr_class_2 = cm[2][0] / (cm[2][0] + cm[2][1] + cm[2][2])
print("Taxa de Falsos Positivos - Classe 0:", fpr_class_0)
print("Taxa de Falsos Positivos - Classe 1:", fpr_class_1)
print("Taxa de Falsos Positivos - Classe 2:", fpr_class_2)

print("==================================")
print("Recall por classe(classe 0): ", recallbyclass0)
print("Recall por classe(classe 1): ", recallbyclass1)
print("Recall por classe(classe 2): ", recallbyclass2)
print("==================================")

print("Taxa de acerto do classificador: ", acuracia)
print("==================================")

print("Precisão por classe(classe 0): ", precisaobyclass0)
print("Precisão por classe(classe 1): ", precisaobyclass1)
print("Precisão por classe(classe 2): ", precisaobyclass2)
print("==================================")

print("Medida F por classe(classe 0): ", medidaF0)
print("Medida F por classe(classe 1): ", medidaF1)
print("Medida F por classe(classe 2): ", medidaF2)
print("==================================")

print("Taxa de FP por classe(classe 0): ", taxaFP0)
print("Taxa de FP por classe(classe 1): ", taxaFP1)
print("Taxa de FP por classe(classe 2): ", taxaFP2)
print("==================================")
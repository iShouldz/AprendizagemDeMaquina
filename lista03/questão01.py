'''Construa sua própria implementação do classicador pelo vizinho mais próximo
(1 − NN) utilizando distância euclidiana. Avalie este classicador utilizando metade dos exem-
plos de cada classe da base Iris (archive.ics.uci.edu/ml/datasets/iris) como conjunto de
teste e o restante como conjunto de treinamento. Atenção: construa também a implementação
da distância euclidiana.
'''

import numpy as np
import auxiliar
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
treino = open("treinoIris.txt", "r")
teste = open("testeIris.txt", "r")
x_treino = treino.readlines()
x_teste = teste.readlines()








x = [[5.1,3.5,1.4,0.2], [4.7,3.2,1.3,0.2], [5.8,2.7,3.9,1.2], [6.0,2.7,5.1,1.6], [6.3,2.9,5.6,1.8], [6.5,3.0,5.8,2.2]]
y = ["Iris-setosa", "Iris-setosa", "Iris-versicolor", "Iris-versicolor", "Iris-virginica", "Iris-virginica"]


print(auxiliar.vizinhoMaisProximo(x, y, [[5.4,3.0,4.5,1.5],[7.1,3.0,5.9,2.1],[4.9,3.0,1.4,0.2]]))

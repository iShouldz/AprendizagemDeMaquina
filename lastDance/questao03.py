import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.datasets import make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('spiral.csv')
X = data[['x', 'y']].values
y = data['class'].values

processar = StandardScaler()
X = processar.fit_transform(X)

"""Caso 1"""
arrayAcertos = []
for i in range(30):
    x_treino, x_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3)
    redeNeural = MLPClassifier(hidden_layer_sizes=(4), max_iter=500, learning_rate_init=0.3, activation='logistic')
    redeNeural.fit(x_treino, y_treino)
    arrayAcertos.append(redeNeural.score(x_teste, y_teste))

print(f'Media dos acertos caso 1: {sum(arrayAcertos) / len(arrayAcertos)}')

"""Caso 2"""
arrayAcertos = []
for i in range(30):
    x_treino, x_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3)
    redeNeural = MLPClassifier(hidden_layer_sizes=(4, 4), max_iter=500, learning_rate_init=0.3, activation='logistic')
    redeNeural.fit(x_treino, y_treino)
    arrayAcertos.append(redeNeural.score(x_teste, y_teste))

print(f'Media dos acertos caso 2: {sum(arrayAcertos) / len(arrayAcertos)}')

"""Caso 3"""
arrayAcertos = []
for i in range(30):
    x_treino, x_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3)
    redeNeural = MLPClassifier(hidden_layer_sizes=(4, 4, 4), max_iter=500, learning_rate_init=0.3, activation='logistic')
    redeNeural.fit(x_treino, y_treino)
    arrayAcertos.append(redeNeural.score(x_teste, y_teste))

print(f'Media dos acertos caso 3: {sum(arrayAcertos) / len(arrayAcertos)}')

"""Caso 4"""
arrayAcertos = []
for i in range(30):
    x_treino, x_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3)
    redeNeural = MLPClassifier(hidden_layer_sizes=(4, 4, 4), max_iter=1000, learning_rate_init=0.3, activation='logistic')
    redeNeural.fit(x_treino, y_treino)
    arrayAcertos.append(redeNeural.score(x_teste, y_teste))

print(f'Media dos acertos caso 4: {sum(arrayAcertos) / len(arrayAcertos)}')

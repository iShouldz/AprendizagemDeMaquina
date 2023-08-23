import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
X = data.iloc[:, 1:]
y = data.iloc[:, 0]

preProcessamento = StandardScaler()
X = preProcessamento.fit_transform(X)

x_treino, x_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.5, stratify=y)

redeNeural = MLPClassifier(hidden_layer_sizes=(16, 8, 3), max_iter=200)
redeNeural.fit(x_treino, y_treino)

acerto = redeNeural.score(x_teste, y_teste)
if acerto < 0.74:
    pass

repeticoes = RepeatedStratifiedKFold(n_splits=2, n_repeats=15)
arrayAcertos = []
for treino_index, teste_index in repeticoes.split(X, y):
    x_treino, x_teste = X[treino_index], X[teste_index]
    y_treino, y_teste = y[treino_index], y[teste_index]
    redeNeural = MLPClassifier(hidden_layer_sizes=(16, 8, 3), max_iter=200)
    redeNeural.fit(x_treino, y_treino)
    arrayAcertos.append(redeNeural.score(x_teste, y_teste))

print(f'Media: {sum(arrayAcertos) / len(arrayAcertos)} ; desvio padrão {np.std(arrayAcertos)}')


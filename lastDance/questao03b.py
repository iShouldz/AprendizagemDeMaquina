import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv('spiral.csv')
X = data[['x', 'y']].values
y = data['class'].values
processamento = StandardScaler()
X = processamento.fit_transform(X)

curvaErroTreino = []
curvaErroTeste = []

for i in range(30):
    x_treino, x_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3)
    redeNeural = MLPClassifier(hidden_layer_sizes=(4, 4, 4), max_iter=5000,
                               learning_rate_init=0.3, activation='logistic')

    erroDuranteTreino = []
    erroDuranteTeste = []
    for epoca in range(5000):
        redeNeural.partial_fit(x_treino, y_treino, classes=np.unique(y))
        """Verifica o erro a cada 100 epocas"""
        if epoca % 100 == 0:
            erroTreino = 1 - redeNeural.score(x_treino, y_treino)
            erroTeste = 1 - redeNeural.score(x_teste, y_teste)
            erroDuranteTreino.append(erroTreino)
            erroDuranteTeste.append(erroTeste)
    curvaErroTreino.append(erroDuranteTreino)
    curvaErroTeste.append(erroDuranteTeste)

mediaErroTreinoEpocas = np.mean(curvaErroTreino, axis=0)
mediaErroTesteEpocas = np.mean(curvaErroTeste, axis=0)

"""Gera imagem das curvas"""
plt.figure(figsize=(10, 6))
plt.plot(range(0, 5000, 100), mediaErroTreinoEpocas, label='Treinamento')
plt.plot(range(0, 5000, 100), mediaErroTesteEpocas, label='Teste')
plt.xlabel('Épocas')
plt.ylabel('Erro')
plt.title('Curvas de Erro => Comparativo treinamento vs Teste')
plt.legend()
plt.grid()
plt.show()

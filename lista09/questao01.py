import numpy as np
import pandas as pd
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from lista05.questoes.auxiliar import intervaloDeConfianca

dados = pd.read_csv("wdbc.data", header=None)

X = dados.iloc[:, 2:]
y = dados.iloc[:, 1].map({'M': 1, 'B': 0})

# Normalização dos dados, normaliza x
normalizador = StandardScaler()
X_normalizado = normalizador.fit_transform(X)

acertos = []
matriz = np.zeros((2, 2), dtype=int)
loo = LeaveOneOut()
leaveOneOutNormalizado = loo.split(X_normalizado)

for treino, teste in leaveOneOutNormalizado:
    X_treino, X_teste = X_normalizado[treino], X_normalizado[teste]
    y_treino, y_teste = y.iloc[treino], y.iloc[teste]

    knn = KNeighborsClassifier(n_neighbors=1, metric='euclidean')
    knn.fit(X_treino, y_treino)
    resultado = knn.predict(X_teste)
    resultadoAcerto = accuracy_score(y_teste, resultado)
    acertos.append(resultadoAcerto)


print("Acurácia Média:", np.mean(acertos))
print("Desvio Padrão:", np.std(acertos))
print("Intervalo de Confiança:", intervaloDeConfianca(acertos))

# KNN novamente para cross-validation bug da matriz individual
knn2 = KNeighborsClassifier(n_neighbors=1, metric='euclidean')

# Realizar cross-validation com Leave-One-Out
prever = cross_val_predict(knn2, X_normalizado, y, cv=loo)
matrizConfusao = confusion_matrix(y, prever)

print("\nMatriz de Confusão:")
print(matrizConfusao)

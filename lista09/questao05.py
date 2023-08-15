import numpy as np
import pandas as pd
from sklearn.model_selection import LeaveOneOut
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from lista05.questoes.auxiliar import intervaloDeConfianca

data = pd.read_csv("wdbc.data", header=None)

X = data.iloc[:, 2:].values
y = data.iloc[:, 1].values

def leave_one_out_evaluation(X, y):
    loo = LeaveOneOut()
    acertos = []
    resultados = []
    resultadosYTrue = []
    leaveOneOutNormalizado = loo.split(X)
    for treino, teste in leaveOneOutNormalizado:
        x_treino, x_teste = X[treino], X[teste]
        y_treino, y_teste = y[treino], y[teste]

        # Normalizar os dados
        scaler = StandardScaler()
        xTreinoNormalizado = scaler.fit_transform(x_treino)
        xTesteNormalizado = scaler.transform(x_teste)

        # classificador Naive Bayes com distribuição normal univariada
        knn = GaussianNB()
        knn.fit(xTreinoNormalizado, y_treino)

        # Fazer previsões
        resultado = knn.predict(xTesteNormalizado)

        acertos.append(accuracy_score(y_teste, resultado))
        resultados.append(resultado[0])
        resultadosYTrue.append(y_teste[0])

    return acertos, resultados, resultadosYTrue

#Aplica LOO
accuracies, all_predictions, all_true_labels = leave_one_out_evaluation(X, y)
matrizGlobal = confusion_matrix(all_true_labels, all_predictions)

# Calcular métricas de desempenho globais
mediaAcertos = np.mean(accuracies)
desvioPadrao = np.std(accuracies)

print("Média da acurácia:", mediaAcertos)
print("Desvio padrão da acurácia:", desvioPadrao)
print("Intervalo de confiança da acurácia:", intervaloDeConfianca(accuracies))
print("Matriz de Confusão Global:\n", matrizGlobal)

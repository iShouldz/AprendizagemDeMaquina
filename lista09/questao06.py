import numpy as np
import pandas as pd
from sklearn.model_selection import LeaveOneOut
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from lista05.questoes.auxiliar import intervaloDeConfianca

data = pd.read_csv("wdbc.data", header=None)

X = data.iloc[:, 2:].values
y = data.iloc[:, 1].values

def leave_one_out_evaluation(X, y):
    loo = LeaveOneOut()
    taxasAcerto = []
    resultados = []
    resultadoYTrue = []

    for treino, teste in loo.split(X):
        x_treino, x_teste = X[treino], X[teste]
        y_treino, y_teste = y[treino], y[teste]

        # Treinar o classificador Bayesiano
        classifier = GaussianNB()
        classifier.fit(x_treino, y_treino)

        resultado = classifier.predict(x_teste)

        taxasAcerto.append(accuracy_score(y_teste, resultado))
        resultados.append(resultado[0])
        resultadoYTrue.append(y_teste[0])

    return taxasAcerto, resultados, resultadoYTrue


accurtaxasAcertoacies, resultados, resultadoYTrue = leave_one_out_evaluation(X, y)

matriz = confusion_matrix(resultadoYTrue, resultados)
acertoMedio = np.mean(accurtaxasAcertoacies)
desvioPadrao = np.std(accurtaxasAcertoacies)

print("Média da acurácia:", acertoMedio)
print("Desvio padrão da acurácia:", desvioPadrao)
print("Intervalo de confiança da acurácia:", intervaloDeConfianca(accurtaxasAcertoacies))
print("Matriz de Confusão Global:\n", matriz)

import numpy as np
from sklearn.model_selection import LeaveOneOut
from lista05.questoes.auxiliar import intervaloDeConfianca
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from scipy import stats

dados = np.loadtxt('wdbc.data', delimiter=',', dtype='str')

X = dados[:, 2:32].astype(float)
y = dados[:, 1]
y = np.where(y == 'M', 0, 1)


valoresJanela = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
acuracias = []
matrizes_confusao = []

for janela in valoresJanela:
    loo = LeaveOneOut()
    resultadoPred = []
    resultadoTrue = []
    leaveOneOutNormalizado = loo.split(X)
    for treino, teste in leaveOneOutNormalizado:
        x_treino, x_teste = X[treino], X[teste]
        y_treino, y_teste = y[treino], y[teste]

        # Parzen gaugassiano
        discretizadoTreinoX = np.exp(-0.5 * ((x_treino - x_teste) / janela) ** 2)

        # Naive bayes gaugassiano
        clf = GaussianNB()
        clf.fit(discretizadoTreinoX, y_treino)

        resultado = clf.predict(x_teste)
        resultadoPred.append(resultado)
        resultadoTrue.append(y_teste)

        acuracia = accuracy_score(resultadoTrue, resultadoPred)
        acuracias.append(acuracia)

    acertoMedio = np.mean(acuracias)
    print(f"Acuracia para {janela}: {acertoMedio}")
    print(f"Desvio padrão: {np.std(acuracias)}")
    print(f"Intervalo de confiança da acurácia: {intervaloDeConfianca(acuracias)}\n")

    matriz = confusion_matrix(np.concatenate(resultadoTrue), np.concatenate(resultadoPred))
    print(f"Matriz de confusão: \n{matriz}")



"""
Objetivo:
    holdout 50/50 para a base wine
    1..15 KNN na base
    Realizar o intevalo de confiança
"""
import lista05.questoes.auxiliar as auxiliar05

from sklearn.datasets import load_wine, load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

x, y = load_iris(return_X_y=True)
def holdout(quantidade, k):
    holdout = []
    for i in range(quantidade):
        x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5, train_size=0.5)
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(auxiliar05.verificarAcerto(resultado, y_teste))
    intervalo = auxiliar05.intervaloDeConfianca(holdout)
    return intervalo

def holdoutSemPrimeiraColuna(quantidade, k):
    holdout = []
    for i in range(quantidade):
        x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5, train_size=0.5)
        x_treino, x_teste = auxiliar05.removerUltimaColuna(x_treino, x_teste)
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(auxiliar05.verificarAcerto(resultado, y_teste))
    intervalo = auxiliar05.intervaloDeConfianca(holdout)
    return intervalo

def holdout12PrimeiraColuna(quantidade, k):
    holdout = []
    for i in range(quantidade):
        x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5, train_size=0.5)
        x_treino, x_teste = auxiliar05.remover12Coluna(x_treino, x_teste)
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(auxiliar05.verificarAcerto(resultado, y_teste))
    intervalo = auxiliar05.intervaloDeConfianca(holdout)
    return intervalo

def holdoutSegundaTerceiraColuna(quantidade, k):
    holdout = []
    for i in range(quantidade):
        x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5, train_size=0.5)
        x_treino, x_teste = auxiliar05.removerSegundaTerceira(x_treino, x_teste)
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(auxiliar05.verificarAcerto(resultado, y_teste))
    intervalo = auxiliar05.intervaloDeConfianca(holdout)
    return intervalo

def holdoutPrimeiraTerceiraColuna(quantidade, k):
    holdout = []
    for i in range(quantidade):
        x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5, train_size=0.5)
        x_treino, x_teste = auxiliar05.removerPrimeiraETerceira(x_treino, x_teste)
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(auxiliar05.verificarAcerto(resultado, y_teste))
    intervalo = auxiliar05.intervaloDeConfianca(holdout)
    return intervalo

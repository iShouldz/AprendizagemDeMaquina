import qs1
import auxiliar_d
from lista05.questoes.auxiliar import verificarAcerto, intervaloDeConfianca
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier


def holdout100():
    rmseArray = []
    for i in range(100):
        """100 holdout 50/50 base students"""
        x_treino, x_teste, y_treino, y_teste = qs1.studentsTreinoTeste()
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        rmse = mean_squared_error(y_teste, resultado, squared=False)
        rmseArray.append(rmse)
    return rmseArray

print(f"Intervalo de confiança para RMSE 100 - Holdout 50/50\n{intervaloDeConfianca(holdout100())}")

def holdout100Numerico():
    rmseArray = []
    for i in range(100):
        """100 holdout 50/50 base students"""
        x_treino, x_teste, y_treino, y_teste = auxiliar_d.studentsTreinoTesteNumerico()
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        rmse = mean_squared_error(y_teste, resultado, squared=False)
        rmseArray.append(rmse)
    return rmseArray

print(f"Intervalo de confiança para RMSE 100, com base apenas numerica"
      f" - Holdout 50/50\n{intervaloDeConfianca(holdout100Numerico())}")

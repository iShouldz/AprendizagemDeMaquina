from lista05.questoes.auxiliar import intervaloDeConfianca
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from suporteqs3 import florestTreinoTeste, florestTreinoTesteSemTransformarBiblioteca
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
def holdout100():
    rmseArray = []
    for i in range(100):
        """100 holdout 50/50 base florest"""
        x_treino, x_teste, y_treino, y_teste = florestTreinoTeste()
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        rmse = mean_squared_error(y_teste, resultado, squared=False)
        rmseArray.append(rmse)
    return rmseArray

print(f"Intervalo de confiança para RMSE 100 com biblioteca- Holdout 50/50\n{intervaloDeConfianca(holdout100())}")

def holdout100_():
    rmseArray = []
    for i in range(100):

        """100 holdout 50/50 base florest"""
        x_treino, x_teste, y_treino, y_teste = florestTreinoTesteSemTransformarBiblioteca()
        knn = KNeighborsRegressor(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        #print(resultado)
        rmse = mean_squared_error(y_teste, resultado, squared=False)
        rmseArray.append(rmse)
    return rmseArray

print(f"Intervalo de confiança para RMSE 100 sem biblioteca- Holdout 50/50\n{intervaloDeConfianca(holdout100_())}")

import qs1
from lista05.questoes.auxiliar import verificarAcerto, intervaloDeConfianca
from sklearn.neighbors import KNeighborsClassifier

def holdout100():
    holdout = []
    for i in range(100):
        """100 holdout 50/50 base wine completa"""
        x_treino, x_teste, y_treino, y_teste = qs1.qs2Binario()
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(verificarAcerto(resultado, y_teste))
    return holdout

print(f"Intervalo de confiança para Q3 binario - Holdout 50/50\n{intervaloDeConfianca(holdout100())}")

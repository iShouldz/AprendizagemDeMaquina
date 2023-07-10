from questao06 import ordinalTreinoTeste
from qs6b import naoOrdinalTreinoTeste
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from lista05.questoes.auxiliar import verificarAcerto, intervaloDeConfianca


def holdout100():
    holdout = []
    holdoutSemColuna = []
    for i in range(100):
        """100 holdout 50/50 base car ordinal"""
        x_treino, x_teste, y_treino, y_teste = ordinalTreinoTeste()
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(verificarAcerto(resultado, y_teste))

        """100 holdout 50/50 base não ordinal"""
        x_treino, x_teste, y_treino, y_teste = naoOrdinalTreinoTeste()
        knn2 = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdoutSemColuna.append(verificarAcerto(resultado, y_teste))

    return holdout, holdoutSemColuna

ordinal, naoordinal = holdout100()
print(f"INTERVALO DE CONFIANÇA ORDINAL: {intervaloDeConfianca(ordinal)}")
print(f"INTERVALO DE CONFIANÇA NÃO-ORDINAL: {intervaloDeConfianca(naoordinal)}")

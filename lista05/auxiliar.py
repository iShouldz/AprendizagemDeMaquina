from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

x, y = load_wine(return_X_y=True)

def holdout100():
    holdout = []
    for i in range(100):
        x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5, train_size=0.5)
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(verificarAcerto(resultado, y_teste))
    return holdout


def verificarAcerto(arrayClassificadoByKNN, arrayClassificadoTeste):
    contador = 0
    for i in range(len(arrayClassificadoByKNN)):
        if arrayClassificadoByKNN[i] == arrayClassificadoTeste[i]:
            contador += 1
    return (contador / len(arrayClassificadoByKNN) * 100).__round__(2)

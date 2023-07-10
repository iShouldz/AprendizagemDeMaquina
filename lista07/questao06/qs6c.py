from questao06 import

def holdout100():
    holdout = []
    holdoutSemColuna = []
    for i in range(100):
        """100 holdout 50/50 base wine completa"""
        x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5, train_size=0.5)
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(verificarAcerto(resultado, y_teste))

        """100 holdout 50/50 base wine sem a última coluna"""
        x_treino2 = x_treino
        x_teste2 = x_teste
        x_treino2, x_teste2 = removerUltimaColuna(x_treino2, x_teste2)
        knn2 = KNeighborsClassifier(n_neighbors=1)
        knn2.fit(x_treino2, y_treino)
        resultado = knn2.predict(x_teste2)
        holdoutSemColuna.append(verificarAcerto(resultado, y_teste))

    return holdout, holdoutSemColuna
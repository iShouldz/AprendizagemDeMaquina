'''Construa sua própria implementação do classicador pelo vizinho mais próximo
(1 − NN) utilizando distância euclidiana. Avalie este classicador utilizando metade dos exem-
plos de cada classe da base Iris (archive.ics.uci.edu/ml/datasets/iris) como conjunto de
teste e o restante como conjunto de treinamento. Atenção: construa também a implementação
da distância euclidiana.
'''

import auxiliar, baseDeDados, teste

x_treino = baseDeDados.baseIris_Treinamento()
y_treino = baseDeDados.baseIris_Classificadores_Treinamento()
x_teste = baseDeDados.baseIris_Teste()
y_teste = baseDeDados.baseIris_Classificadores_Teste()

print("Taxa de acerto, para Minkowski p = 1")
resultado = auxiliar.vizinhoMaisProximoMinkowski(x_treino, y_treino, x_teste, 1)
print("Taxa de Acerto: " + str(baseDeDados.verificarAcerto(resultado, y_teste).__round__(2)) + "%")

print("Taxa de acerto, para Minkowski p = 2")
resultado = auxiliar.vizinhoMaisProximoMinkowski(x_treino, y_treino, x_teste, 2)
print("Taxa de Acerto: " + str(baseDeDados.verificarAcerto(resultado, y_teste).__round__(2)) + "%")

print("Taxa de acerto, para Minkowski p = 4")
resultado = auxiliar.vizinhoMaisProximoMinkowski(x_treino, y_treino, x_teste, 4)
print("Taxa de Acerto: " + str(baseDeDados.verificarAcerto(resultado, y_teste).__round__(2)) + "%")



'''
print("##########################################################")
print(x_treino)
print("==================")
print(y_treino)
print("==================")
print(x_teste)
print("==================")
print(y_teste)

print("==================")
print("==================")

print("Para distancia euclidiana em 1-NN da base iris:")
print("Taxa de Acerto: " + str(baseDeDados.verificarAcerto(resultado, y_teste).__round__(2)) + "%")
'''

x = [[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2], [5.8, 2.7, 3.9, 1.2],
     [6.0, 2.7, 5.1, 1.6], [6.3, 2.9, 5.6, 1.8], [6.5, 3.0, 5.8, 2.2]]
y = ["Iris-setosa", "Iris-setosa", "Iris-versicolor", "Iris-versicolor", "Iris-virginica", "Iris-virginica"]


print(auxiliar.vizinhoMaisProximo(x, y, [[5.4, 3.0, 4.5, 1.5], [7.1, 3.0, 5.9, 2.1], [4.9, 3.0, 1.4, 0.2]]))
print(baseDeDados.verificarAcerto(auxiliar.vizinhoMaisProximo(x, y,
                                                              [[5.4, 3.0, 4.5, 1.5], [7.1, 3.0, 5.9, 2.1],
                                                               [4.9, 3.0, 1.4, 0.2]]), ["Iris-versicolor",
                                                                                        "Iris-virginica",
                                                                                        "Iris-setosa"]))

#
print(auxiliar.knn(x, y, [[5.4, 3.0, 4.5, 1.5], [7.1, 3.0, 5.9, 2.1], [4.9, 3.0, 1.4, 0.2]], 4))
'''Construa sua própria implementação do classicador pelo vizinho mais próximo
(1 − NN) utilizando distância euclidiana. Avalie este classicador utilizando metade dos exem-
plos de cada classe da base Iris (archive.ics.uci.edu/ml/datasets/iris) como conjunto de
teste e o restante como conjunto de treinamento. Atenção: construa também a implementação
da distância euclidiana.
'''

import auxiliar, baseDeDados

x_treino = baseDeDados.baseIris_Treinamento().tolist()
y_treino = baseDeDados.baseIris_Classificadores_Treinamento().tolist()
x_teste = baseDeDados.baseIris_Teste().tolist()
y_teste = baseDeDados.baseIris_Classificadores_Teste().tolist()

print("Taxa de acerto, para Minkowski p = 1")
resultado = auxiliar.vizinhoMaisProximoMinkowski(x_treino, y_treino, x_teste, 1)
print("Taxa de Acerto: " + str(baseDeDados.verificarAcerto(resultado, y_teste).__round__(2)) + "%")

print("Taxa de acerto, para Minkowski p = 2")
resultado = auxiliar.vizinhoMaisProximoMinkowski(x_treino, y_treino, x_teste, 2)
print("Taxa de Acerto: " + str(baseDeDados.verificarAcerto(resultado, y_teste).__round__(2)) + "%")

print("Taxa de acerto, para Minkowski p = 4")
resultado = auxiliar.vizinhoMaisProximoMinkowski(x_treino, y_treino, x_teste, 4)
print("Taxa de Acerto: " + str(baseDeDados.verificarAcerto(resultado, y_teste).__round__(2)) + "%")


x = [[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2], [5.8, 2.7, 3.9, 1.2],
     [6.0, 2.7, 5.1, 1.6], [6.3, 2.9, 5.6, 1.8], [6.5, 3.0, 5.8, 2.2]]
y = ["Iris-setosa", "Iris-setosa", "Iris-versicolor",
     "Iris-versicolor", "Iris-virginica", "Iris-virginica"]
'''
print(auxiliar.knn(x, y, [[5.4, 3.0, 4.5, 1.5], [7.1, 3.0, 5.9, 2.1], [4.9, 3.0, 1.4, 0.2]], 2))
print(auxiliar.knn(x, y, [[5.4, 3.0, 4.5, 1.5], [7.1, 3.0, 5.9, 2.1], [4.9, 3.0, 1.4, 0.2]], 3))
print(auxiliar.knn(x, y, [[5.4, 3.0, 4.5, 1.5], [7.1, 3.0, 5.9, 2.1], [4.9, 3.0, 1.4, 0.2]], 4))
print(auxiliar.knn(x, y, [[5.4, 3.0, 4.5, 1.5], [7.1, 3.0, 5.9, 2.1], [4.9, 3.0, 1.4, 0.2]], 5))
'''



resultado = auxiliar.knn(x_treino, y_treino, x_teste, 7)
print("Taxa de acerto para 7-NN - SEM PESO: ", baseDeDados.verificarAcerto(resultado, y_teste))



'''
print("##########################################################")
print(x_treino)
print("==================")
print(y_treino)
print("==================")
print(x_teste)
print("==================")
print(y_teste)
print(auxiliar.knn(x_treino, y_treino, x_teste, 7))
print("==================")
print("==================")
print("Para distancia euclidiana em 1-NN da base iris:")
print("Taxa de Acerto: " + str(baseDeDados.verificarAcerto(resultado, y_teste).__round__(2)) + "%")


x = [[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2],[6.7,3.1,4.4,1.4],
     [5.8, 2.7, 3.9, 1.2],
     [6.0, 2.7, 5.1, 1.6], [6.3, 2.9, 5.6, 1.8], [6.5, 3.0, 5.8, 2.2]]
y = ["Iris-setosa", "Iris-setosa", "Iris-versicolor", "Iris-versicolor", "Iris-versicolor", "Iris-virginica",
     "Iris-virginica"]


print(auxiliar.vizinhoMaisProximo(x, y, [[5.4, 3.0, 4.5, 1.5], [7.1, 3.0, 5.9, 2.1], [4.9, 3.0, 1.4, 0.2]]))
print(baseDeDados.verificarAcerto(auxiliar.vizinhoMaisProximo(x, y,
                                                              [[5.4, 3.0, 4.5, 1.5], [7.1, 3.0, 5.9, 2.1],
                                                               [4.9, 3.0, 1.4, 0.2]]), ["Iris-versicolor",
                                                                                        "Iris-virginica",
                                                                                        "Iris-setosa"]))

x = [[14.23, 1.71, 2.43, 15.6, 127.0, 2.8, 3.06, 0.28, 2.29, 5.64, 1.04, 3.92, 1065.0],
     [12.08, 2.08, 1.7, 17.5, 97.0, 2.23, 2.17, 0.26, 1.4, 3.3, 1.27, 2.96, 710.0],
     [12.96, 3.45, 2.35, 18.5, 106.0, 1.39, 0.7, 0.4, 0.94, 5.28, 0.68, 1.75, 675.0]]
y = [1, 2, 3]

print(auxiliar.knn(x, y, [[12.72,1.81,2.2,18.8,86,2.2,2.53,.26,1.77,3.9,1.16,3.14,714]], 1))

x = [[5.1, 3.5, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2],[6.7,3.1,4.4,1.4],
     [5.8, 2.7, 3.9, 1.2],
     [6.0, 2.7, 5.1, 1.6], [6.3, 2.9, 5.6, 1.8], [6.5, 3.0, 5.8, 2.2]]
y = ["Iris-setosa", "Iris-setosa", "Iris-versicolor", "Iris-versicolor", "Iris-versicolor", "Iris-virginica",
     "Iris-virginica"]

print(auxiliar.knn(x, y, [[5.8,2.7,5.1,1.9], [4.7,3.2,1.6,0.2]], 2))

print("resultado")
resultado = auxiliar.knn(x_treino, y_treino, x_teste, 7)
print("resultado: ", resultado)
print("classificaçÃO")
print(y_teste)

print(baseDeDados.verificarAcerto(resultado, y_teste))

'''
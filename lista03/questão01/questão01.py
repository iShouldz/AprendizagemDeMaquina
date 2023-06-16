'''Construa sua própria implementação do classicador pelo vizinho mais próximo
(1 − NN) utilizando distância euclidiana. Avalie este classicador utilizando metade dos exem-
plos de cada classe da base Iris (archive.ics.uci.edu/ml/datasets/iris) como conjunto de
teste e o restante como conjunto de treinamento. Atenção: construa também a implementação
da distância euclidiana.
'''

import auxiliar, baseDeDados

x_treino = baseDeDados.baseIris_Treinamento()
y_treino = baseDeDados.baseIris_Classificadores_Treinamento()
x_teste = baseDeDados.baseIris_Teste()
y_teste = baseDeDados.baseIris_Classificadores_Teste()

resultado = auxiliar.vizinhoMaisProximo(x_treino, y_treino, x_teste)
'''print("##########################################################")
print(x_treino)
print("==================")
print(y_treino)
print("==================")
print(x_teste)
print("==================")
print(y_teste)

print("==================")
print("==================")
'''
print(resultado)
print(baseDeDados.verificarAcerto(resultado, y_teste))


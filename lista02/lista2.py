import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#Vetores auxiliares que contém cada classe
contador = 0
vetorSetosa = []
leitura = []
teste = []
vetorVersicolor = []
vetorVirginica = []

#Base de dados
iris = open("iris.txt", "r")

#Salvar os dados e remover a quebra de linha
arquivo = iris.read()
leitura = arquivo.split("\n")

#Separar a base em 3 arrays com suas classes, posteriormente, separar cada array em um sub-array => treinamento e testes
for x in leitura:
    teste = x.split(",")
    if teste[4] == "Iris-setosa":
        vetorSetosa.append(teste)
    elif teste[4] == "Iris-versicolor":
        vetorVersicolor.append(teste)
    elif teste[4] == "Iris-virginica":
        vetorVirginica.append(teste)

array = np.array(vetorSetosa)
matriz = np.split(array, 2)
array = np.array(vetorVersicolor)
matriz2 = np.split(array, 2)
array = np.array(vetorVirginica)
matriz3 = np.split(array, 2)

print(matriz)

#Separando conjunto de x_treino e x_teste de cada classe
arrayTreinamentoSetosa = matriz[0]
arrayTestesSetosa = matriz[1]
arrayTreinamentoVersicolor = matriz2[0]
arrayTestesVersicolor = matriz2[1]
arrayTreinamentoVirginica = matriz3[0]
arrayTestesVirginica = matriz3[1]
print(arrayTreinamentoSetosa)
#Concatenando os conjuntos de x_treino e x_teste
arrayTreinamento = np.concatenate((arrayTreinamentoSetosa, arrayTreinamentoVersicolor))
arrayTreinamento = np.concatenate((arrayTreinamento, arrayTreinamentoVirginica))
arrayTeste = np.concatenate((arrayTestesVirginica, arrayTestesSetosa))
arrayTeste = np.concatenate((arrayTeste, arrayTestesVersicolor))

#Convertendo os dados para float e obtendo o conjunto de classificadores para x_teste
copiaClasTeste = arrayTeste
arrayTeste = np.delete(arrayTeste, [4], 1)
arrayTeste = arrayTeste.astype('float64')
acertosClassificadores = np.delete(copiaClasTeste, [0, 1, 2, 3], 1)

#Convertendo os dados para float e obtendo o conjunto de classificadores para treinamento
copia = arrayTreinamento
classificadores = np.delete(copia, [0, 1, 2, 3], 1)
arrayTreinamento = np.delete(arrayTreinamento, [4], 1)
arrayTreinamento = arrayTreinamento.astype('float64')

#Realizando classificação para 1-NN
classificadores = classificadores.ravel()
neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(arrayTreinamento, classificadores)
resultado = neigh.predict(arrayTeste)


#Realizando verificação de acertos e em caso de erro, exibir o indice e a disparidade encontrada
for i in range(len(resultado)):
    if(acertosClassificadores[i] == resultado[i]):
        contador += 1
    else:
        print(acertosClassificadores[i])
        print("^ em: " + str(i))
        print(resultado[i])
        print("========================")
print(neigh.score(arrayTeste, acertosClassificadores))
print("Taxa de acerto: " + str(contador) + "/75, " + str((contador/75) * 100) + "%")
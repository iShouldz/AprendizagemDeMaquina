import numpy as np
from sklearn.datasets import load_wine, load_iris
from sklearn.model_selection import train_test_split


contador = 0
novoXTreino = []
novoXTeste = []
vetorSetosa = []
leitura = []
teste = []
vetorVersicolor = []
vetorVirginica = []
x, y = load_wine(return_X_y=True)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5)

#Base de dados
iris = open("iris.txt", "r")
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

#Separando conjunto de treino e teste de cada classe
arrayTreinamentoSetosa = matriz[0]
arrayTestesSetosa = matriz[1]
arrayTreinamentoVersicolor = matriz2[0]
arrayTestesVersicolor = matriz2[1]
arrayTreinamentoVirginica = matriz3[0]
arrayTestesVirginica = matriz3[1]
#Concatenando os conjuntos de treino e teste
arrayTreinamento = np.concatenate((arrayTreinamentoSetosa, arrayTreinamentoVersicolor))
arrayTreinamento = np.concatenate((arrayTreinamento, arrayTreinamentoVirginica))
arrayTeste = np.concatenate((arrayTestesVirginica, arrayTestesSetosa))
arrayTeste = np.concatenate((arrayTeste, arrayTestesVersicolor))

#Convertendo os dados para float e obtendo o conjunto de classificadores para teste
copiaClasTeste = arrayTeste
arrayTeste = np.delete(arrayTeste, [4], 1)
arrayTeste = arrayTeste.astype('float64')
acertosClassificadores = np.delete(copiaClasTeste, [0, 1, 2, 3], 1)

#Convertendo os dados para float e obtendo o conjunto de classificadores para treinamento
copia = arrayTreinamento
classificadores = np.delete(copia, [0, 1, 2, 3], 1)
arrayTreinamento = np.delete(arrayTreinamento, [4], 1)
arrayTreinamento = arrayTreinamento.astype('float64')


for i in range(len(x_teste)):
    novoXTreino.append(np.delete(x_treino[i], [12]))
    novoXTeste.append(np.delete(x_teste[i], [12]))

def removidoTreino():
    return novoXTreino

def removidoTeste():
    return novoXTeste

def baseIris_Treinamento(i):
    if i == 'i':
        return arrayTreinamento
    else:
        return x_treino

def baseIris_Classificadores_Treinamento(i):
    if i == 'i':
        return classificadores
    else:
        return y_treino

def baseIris_Teste(i):
    if i == 'i':
        return arrayTeste
    else:
        return x_teste

def baseIris_Classificadores_Teste(i):
    if i == 'i':
        return acertosClassificadores
    else:
        return y_teste

def verificarAcerto(arrayClassificadoByKNN, arrayClassificadoTeste):
    contador = 0
    for i in range(len(arrayClassificadoByKNN)):
        if arrayClassificadoByKNN[i] == arrayClassificadoTeste[i]:
            contador += 1
    return (contador / len(arrayClassificadoByKNN) * 100).__round__(2)

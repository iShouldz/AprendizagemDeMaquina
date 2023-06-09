import numpy as np
from sklearn.neighbors import KNeighborsClassifier

contador = contadorTamanho = 0
vetorES = []
vetorFR = []
vetorGE = []
vetorIT = []
vetorUK = []
vetorUS = []

linguas = open("accent-mfcc-data-1.csv", "r")
arquivo = linguas.read()
leitura = arquivo.split("\n")
#del leitura[0]

for x in leitura:
    arquivoSplit = x.split(",")
    arquivoSplit[0] = arquivoSplit[0].replace('"', '')
    if arquivoSplit[0] == "ES":
        vetorES.append(arquivoSplit)
    elif arquivoSplit[0] == "FR":
        vetorFR.append(arquivoSplit)
    elif arquivoSplit[0] == "GE":
        vetorGE.append(arquivoSplit)
    elif arquivoSplit[0] == "IT":
        vetorIT.append(arquivoSplit)
    elif arquivoSplit[0] == "UK":
        vetorUK.append(arquivoSplit)
    elif arquivoSplit[0] == "US":
        vetorUS.append(arquivoSplit)
    contadorTamanho += 1

array = np.array(vetorES)
matrizES = np.array_split(array, 2)
array = np.array(vetorFR)
matrizFR = np.array_split(array, 2)
array = np.array(vetorGE)
matrizGE = np.array_split(array, 2)
array = np.array(vetorIT)
matrizIT = np.array_split(array, 2)
array = np.array(vetorUK)
matrizUK = np.array_split(array, 2)
array = np.array(vetorUS)
matrizUS = np.array_split(array, 2)

#matrizX[0] => Treinamento;matriz[z] => Teste

arrayTreinamento = np.concatenate((matrizES[0], matrizFR[0]))
arrayTreinamento = np.concatenate((arrayTreinamento, matrizGE[0]))
arrayTreinamento = np.concatenate((arrayTreinamento, matrizIT[0]))
arrayTreinamento = np.concatenate((arrayTreinamento, matrizUK[0]))
arrayTreinamento = np.concatenate((arrayTreinamento, matrizUS[0]))
arrayTeste = np.concatenate((matrizES[1], matrizFR[1]))
arrayTeste = np.concatenate((arrayTeste, matrizGE[1]))
arrayTeste = np.concatenate((arrayTeste, matrizIT[1]))
arrayTeste = np.concatenate((arrayTeste, matrizUK[1]))
arrayTeste = np.concatenate((arrayTeste, matrizUS[1]))

#Conjunto de treino
copiaTreinamento = arrayTreinamento
classificadores = np.delete(copiaTreinamento, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1)
arrayTreinamento = np.delete(arrayTreinamento, [0], 1)
arrayTreinamento = arrayTreinamento.astype('float64')

#Conjunto de teste
copiaTeste = arrayTeste
acertoClassificadores = np.delete(copiaTeste, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1)
arrayTeste = np.delete(arrayTeste, [0], 1)
arrayTeste = arrayTeste.astype('float64')

classificadores = classificadores.ravel()
neigh = KNeighborsClassifier(n_neighbors=7, weights='distance', metric='euclidean')
neigh.fit(arrayTreinamento, classificadores)
resultado = neigh.predict(arrayTeste)
print(len(resultado))
print(len(acertoClassificadores))
print(len(arrayTreinamento))
print(len(arrayTeste))
print(len(classificadores))
print(neigh.score(arrayTeste, acertoClassificadores))
for i in range(len(resultado)):
    if(acertoClassificadores[i] == resultado[i]):
        contador += 1
    else:
        print(acertoClassificadores[i])
        print("^ em: " + str(i))
        print(resultado[i])
        print("========================")

print("Taxa de acerto: " + str(neigh.score(arrayTeste, acertoClassificadores) * 100) + "%")

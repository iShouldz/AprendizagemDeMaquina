import numpy as np
from sklearn.model_selection import train_test_split

baseSplitados = []

base = open('irisSaida.csv', 'r')
linhas = base.readlines()
del linhas[0]

for i in linhas:
    teste = i.split(',')
    baseSplitados.append(teste)

for i in range(len(baseSplitados)):
    del baseSplitados[i][0]

baseNp = np.array(baseSplitados)

def separarX(data):
    arrayX = []
    for i in range(len(data)):
        arrayX.append(np.delete(data[i], [4]))
    arrayXnp = np.array(arrayX)
    return arrayXnp

def separarY(data):
    arrayY = []
    for i in range(len(data)):
        arrayY.append(np.delete(data[i], [0, 1, 2, 3]))
    arrayYnp = np.array(arrayY)
    return arrayYnp

irisX = separarX(baseNp)
irisY = separarY(baseNp)
irisY = irisY.ravel()

def irisTreinoTeste():
    x_treino, x_teste, y_treino, y_teste = train_test_split(irisX, irisY, test_size=0.5)
    return x_treino, x_teste, y_treino, y_teste
print(baseSplitados)




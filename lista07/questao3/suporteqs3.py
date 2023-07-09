import math
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import preprocessing
from sklearn import utils

florestSplitados = []
florest = open("../forestfires.csv", "r")
linhasFlorest = florest.readlines()
copia_d = []

def imprimir():
    for i in florestSplitados:
        print(i)

#Splita pelo ; para poder ter colunas para tratar
for i in linhasFlorest:
    teste = i.split(",")
    florestSplitados.append(teste)

#imprimir()
del florestSplitados[0]
#Percorrer para realizar alteração
for i in range(len(florestSplitados)):
    #Remove o mes
    remover1 = florestSplitados[i][2]
    #Remove o dia
    remover2 = florestSplitados[i][3]
    if florestSplitados[i][2] == 'jan':
        #Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 1 / 12))
        #Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 1 / 12))
    elif florestSplitados[i][2] == 'feb':
        #Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 2 / 12))
        #Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 2 / 12))
    elif florestSplitados[i][2] == 'mar':
        # Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 3 / 12))
        # Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 3 / 12))
    elif florestSplitados[i][2] == 'apr':
        # Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 4 / 12))
        # Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 4 / 12))
    elif florestSplitados[i][2] == 'may':
        # Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 5 / 12))
        # Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 5 / 12))
    elif florestSplitados[i][2] == 'jun':
        # Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 6 / 12))
        # Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 6 / 12))
    elif florestSplitados[i][2] == 'jul':
        # Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 7 / 12))
        # Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 7 / 12))
    elif florestSplitados[i][2] == 'aug':
        # Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 8 / 12))
        # Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 8 / 12))
    elif florestSplitados[i][2] == 'sep':
        # Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 9 / 12))
        # Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 9 / 12))
    elif florestSplitados[i][2] == 'oct':
        # Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 10 / 12))
        # Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 10 / 12))
    elif florestSplitados[i][2] == 'nov':
        # Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 11 / 12))
        # Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 11 / 12))
    elif florestSplitados[i][2] == 'dec':
        # Mes seno
        florestSplitados[i].insert(2, math.sin(2 * math.pi * 12 / 12))
        # Mes cosseno
        florestSplitados[i].insert(3, math.cos(2 * math.pi * 12 / 12))
    florestSplitados[i].remove(remover1)

    #Replace no dia
    if remover2 == 'mon':
        #Mes seno
        florestSplitados[i].insert(4, math.sin(2 * math.pi * 1 / 7))
        #Mes cosseno
        florestSplitados[i].insert(5, math.cos(2 * math.pi * 1 / 7))
    elif remover2 == 'tue':
        #Mes seno
        florestSplitados[i].insert(4, math.sin(2 * math.pi * 2 / 7))
        #Mes cosseno
        florestSplitados[i].insert(5, math.cos(2 * math.pi * 2 / 7))
    elif remover2 == 'wed':
        # Mes seno
        florestSplitados[i].insert(4, math.sin(2 * math.pi * 3 / 7))
        # Mes cosseno
        florestSplitados[i].insert(5, math.cos(2 * math.pi * 3 / 7))
    elif remover2 == 'thu':
        # Mes seno
        florestSplitados[i].insert(4, math.sin(2 * math.pi * 4 / 7))
        # Mes cosseno
        florestSplitados[i].insert(5, math.cos(2 * math.pi * 4 / 7))
    elif remover2 == 'fri':
        # Mes seno
        florestSplitados[i].insert(4, math.sin(2 * math.pi * 5 / 7))
        # Mes cosseno
        florestSplitados[i].insert(5, math.cos(2 * math.pi * 5 / 7))
    elif remover2 == 'sat':
        # Mes seno
        florestSplitados[i].insert(4, math.sin(2 * math.pi * 6 / 7))
        # Mes cosseno
        florestSplitados[i].insert(5, math.cos(2 * math.pi * 6 / 7))
    elif remover2 == 'sun':
        # Mes seno
        florestSplitados[i].insert(4, math.sin(2 * math.pi * 7 / 7))
        # Mes cosseno
        florestSplitados[i].insert(5, math.cos(2 * math.pi * 7 / 7))
    florestSplitados[i].remove(remover2)
    florestSplitados[i][10] = float(florestSplitados[i][10])

#Convertendo strings para float
vetorNp = np.array(florestSplitados)
vetorrr = vetorNp.astype('float')

def separarX(data):
    studentsX = []
    for i in range(len(data)):
        studentsX.append(np.delete(data[i], [14]))
    return studentsX

def separarY(data):
    studentsY = []
    for i in range(len(data)):
        studentsY.append(np.delete(data[i], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    studentsY = np.array(studentsY)
    print(studentsY)
    #Calculando log para todo conjunto de Y
    for i in range(len(studentsY)):
        studentsY[i] = np.log(studentsY[i] + 1)
    print(studentsY)
    return studentsY

florestX = separarX(vetorrr)
florestY = separarY(vetorrr)
florestY = florestY.ravel()

def florestTreinoTeste():
    x_treino, x_teste, y_treino, y_teste = train_test_split(florestX, florestY, test_size=0.5)
    lab = preprocessing.LabelEncoder()
    y_teste_transformado = lab.fit_transform(y_teste)
    y_treino_transformado = lab.fit_transform(y_treino)
    return x_treino, x_teste, y_treino_transformado, y_teste_transformado

def florestTreinoTesteSemTransformarBiblioteca():
    x_treino, x_teste, y_treino, y_teste = train_test_split(florestX, florestY, test_size=0.5)
    return x_treino, x_teste, y_treino, y_teste

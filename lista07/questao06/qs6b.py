from sklearn.model_selection import train_test_split
import numpy as np

naoBinaria = []
carro = open("../car.data", "r")
linhaCarro = carro.readlines()

def imprimir(base):
    for i in base:
        print(i)

#Splita pelo ; para poder ter colunas para tratar
for i in linhaCarro:
    teste = i.split(",")
    naoBinaria.append(teste)

"""criando uma versão binaria da base de dados"""

for i in range(len(naoBinaria)):
    #print(f"Primeira linha: {naoBinaria[0]}")
    remover1 = naoBinaria[i][0]
    remover2 = naoBinaria[i][1]
    remover3 = naoBinaria[i][2]
    remover4 = naoBinaria[i][3]
    remover5 = naoBinaria[i][4]
    remover6 = naoBinaria[i][5]
    remover7 = naoBinaria[i][6]
    print(f"Não binaria i[{i}] {naoBinaria[i]}")
    if naoBinaria[i][0] == 'vhigh':
        naoBinaria[i].insert(0, 1)
    else:
        naoBinaria[i].insert(0, 0)

    if naoBinaria[i][1] == 'high':
        naoBinaria[i].insert(1, 1)
    else:
        naoBinaria[i].insert(1, 0)

    if naoBinaria[i][2] == 'med':
        naoBinaria[i].insert(2, 1)
    else:
        naoBinaria[i].insert(2, 0)

    if naoBinaria[i][3] == 'low':
        naoBinaria[i].insert(3, 1)
    else:
        naoBinaria[i].insert(3, 0)
    naoBinaria[i].remove(remover1)

    #Segundo
    if naoBinaria[i][4] == 'vhigh':
        naoBinaria[i].insert(4, 1)
    else:
        naoBinaria[i].insert(4, 0)

    if naoBinaria[i][5] == 'high':
        naoBinaria[i].insert(5, 1)
    else:
        naoBinaria[i].insert(5, 0)

    if naoBinaria[i][6] == 'med':
        naoBinaria[i].insert(6, 1)
    else:
        naoBinaria[i].insert(6, 0)

    if naoBinaria[i][7] == 'low':
        naoBinaria[i].insert(7, 1)
    else:
        naoBinaria[i].insert(7, 0)
    naoBinaria[i].remove(remover2)

    #Terceira
    if naoBinaria[i][8] == '2':
        naoBinaria[i].insert(8, 1)
    else:
        naoBinaria[i].insert(8, 0)

    if naoBinaria[i][9] == '3':
        naoBinaria[i].insert(9, 1)
    else:
        naoBinaria[i].insert(9, 0)

    if naoBinaria[i][10] == '4':
        naoBinaria[i].insert(10, 1)
    else:
        naoBinaria[i].insert(10, 0)

    if naoBinaria[i][11] == '5more':
        naoBinaria[i].insert(11, 1)
    else:
        naoBinaria[i].insert(11, 0)
    naoBinaria[i].remove(remover3)

    # Quarta
    if naoBinaria[i][12] == '2':
        naoBinaria[i].insert(12, 1)
    else:
        naoBinaria[i].insert(12, 0)

    if naoBinaria[i][13] == '4':
        naoBinaria[i].insert(13, 1)
    else:
        naoBinaria[i].insert(13, 0)

    if naoBinaria[i][14] == 'more':
        naoBinaria[i].insert(14, 1)
    else:
        naoBinaria[i].insert(14, 0)
    naoBinaria[i].remove(remover4)

    #Quinta
    print(f"Quinta: {naoBinaria[i][16]}")
    if naoBinaria[i][15] == 'small':
        naoBinaria[i].insert(15, 1)
    else:
        naoBinaria[i].insert(15, 0)

    if naoBinaria[i][16] == 'med':
        naoBinaria[i].insert(16, 1)
    else:
        naoBinaria[i].insert(16, 0)

    if naoBinaria[i][17] == 'big':
        naoBinaria[i].insert(17, 1)
    else:
        naoBinaria[i].insert(17, 0)
    naoBinaria[i].remove(remover5)

    #Sexta
    if naoBinaria[i][18] == 'low':
        naoBinaria[i].insert(18, 1)
    else:
        naoBinaria[i].insert(18, 0)

    if naoBinaria[i][19] == 'med':
        naoBinaria[i].insert(19, 1)
    else:
        naoBinaria[i].insert(19, 0)

    if naoBinaria[i][20] == 'high':
        naoBinaria[i].insert(20, 1)
    else:
        naoBinaria[i].insert(20, 0)
    naoBinaria[i].remove(remover6)

    #Class, deixando como categorico

    if naoBinaria[i][21] == 'unacc\n':
        naoBinaria[i][21] = 1
    elif naoBinaria[i][21] == 'acc\n':
        naoBinaria[i][21] = 2
    elif naoBinaria[i][21] == 'good\n':
        naoBinaria[i][21] = 3
    elif naoBinaria[i][21] == 'vgood\n':
        naoBinaria[i][21] = 4

    #print(naoBinaria[i])

imprimir(naoBinaria)
vetor = np.array(naoBinaria)

def separarX(data):
    studentsX = []
    for i in range(len(data)):
        studentsX.append(np.delete(data[i], [21]))
    return studentsX

def separarY(data):
    studentsY = []
    for i in range(len(data)):
        studentsY.append(np.delete(data[i], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                             17, 18, 19, 20]))
    studentsY = np.array(studentsY)
    return studentsY

florestX = separarX(vetor)
florestY = separarY(vetor)
florestY = florestY.ravel()

def naoOrdinalTreinoTeste():
    x_treino, x_teste, y_treino, y_teste = train_test_split(florestX, florestY, test_size=0.5)
    return x_treino, x_teste, y_treino, y_teste

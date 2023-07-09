import numpy as np
from sklearn.model_selection import train_test_split

studentsSplitados = []
students = open("../student-mat.csv", "r")
linhasEstudantes = students.readlines()

#Splita pelo ; para poder ter colunas para tratar
for i in linhasEstudantes:
    teste = i.split(";")
    studentsSplitados.append(teste)

#Remove o nome das colunas
del studentsSplitados[0]

#Remove os elementos que não são numericos
copia = []
vetorFinal = []
for i in range(len(studentsSplitados)):
    copia.append(np.delete(studentsSplitados[i], [0, 1, 3, 4, 5, 8, 9, 10, 11, 15, 16, 17, 18, 19, 20, 21, 22]))

#Converte de np para list para poder converter de string para int
for x in range(len(copia)):
    copia[x] = copia[x].tolist()
    vetorFinal.append(copia[x])

#Vetor final possui tudo convertido para int
for i in range(len(vetorFinal)):
    # Tratando a terceira coluna
    if vetorFinal[i][0] == '15':
        vetorFinal[i][0] = 15
    elif vetorFinal[i][0] == '16':
        vetorFinal[i][0] = 16
    elif vetorFinal[i][0] == '17':
        vetorFinal[i][0] = 17
    elif vetorFinal[i][0] == '18':
        vetorFinal[i][0] = 18
    elif vetorFinal[i][0] == '19':
        vetorFinal[i][0] = 19
    elif vetorFinal[i][0] == '20':
        vetorFinal[i][0] = 20
    elif vetorFinal[i][0] == '21':
        vetorFinal[i][0] = 21
    elif vetorFinal[i][0] == '22':
        vetorFinal[i][0] = 22

    #Tratando a setima coluna
    if vetorFinal[i][1] == '0':
        vetorFinal[i][1] = 0
    elif vetorFinal[i][1] == '1':
        vetorFinal[i][1] = 1
    elif vetorFinal[i][1] == '2':
        vetorFinal[i][1] = 2
    elif vetorFinal[i][1] == '3':
        vetorFinal[i][1] = 3
    elif vetorFinal[i][1] == '4':
        vetorFinal[i][1] = 4

    # Tratando a oitava coluna
    if vetorFinal[i][2] == '0':
        vetorFinal[i][2] = 0
    elif vetorFinal[i][2] == '1':
        vetorFinal[i][2] = 1
    elif vetorFinal[i][2] == '2':
        vetorFinal[i][2] = 2
    elif vetorFinal[i][2] == '3':
        vetorFinal[i][2] = 3
    elif vetorFinal[i][2] == '4':
        vetorFinal[i][2] = 4

    # Tratando a decima terceira coluna
    if vetorFinal[i][3] == '1':
        vetorFinal[i][3] = 1
    elif vetorFinal[i][3] == '2':
        vetorFinal[i][3] = 2
    elif vetorFinal[i][3] == '3':
        vetorFinal[i][3] = 3
    elif vetorFinal[i][3] == '4':
        vetorFinal[i][3] = 4

    # Tratando a decima quarta coluna
    if vetorFinal[i][4] == '1':
        vetorFinal[i][4] = 1
    elif vetorFinal[i][4] == '2':
        vetorFinal[i][4] = 2
    elif vetorFinal[i][4] == '3':
        vetorFinal[i][4] = 3
    elif vetorFinal[i][4] == '4':
        vetorFinal[i][4] = 4

    # Tratando a decima quinta coluna
    if vetorFinal[i][5] == '0':
        vetorFinal[i][5] = 0
    elif vetorFinal[i][5] == '1':
        vetorFinal[i][5] = 1
    elif vetorFinal[i][5] == '2':
        vetorFinal[i][5] = 2
    elif vetorFinal[i][5] == '3':
        vetorFinal[i][5] = 3
    elif vetorFinal[i][5] == '4':
        vetorFinal[i][5] = 4
    
 # Tratando a vigesima quarta coluna
    if vetorFinal[i][6] == '1':
        vetorFinal[i][6] = 1
    elif vetorFinal[i][6] == '2':
        vetorFinal[i][6] = 2
    elif vetorFinal[i][6] == '3':
        vetorFinal[i][6] = 3
    elif vetorFinal[i][6] == '4':
        vetorFinal[i][6] = 4
    elif vetorFinal[i][6] == '5':
        vetorFinal[i][6] = 5

    # Tratando a vigessima quinta coluna
    if vetorFinal[i][7] == '1':
        vetorFinal[i][7] = 1
    elif vetorFinal[i][7] == '2':
        vetorFinal[i][7] = 2
    elif vetorFinal[i][7] == '3':
        vetorFinal[i][7] = 3
    elif vetorFinal[i][7] == '4':
        vetorFinal[i][7] = 4
    elif vetorFinal[i][7] == '5':
        vetorFinal[i][7] = 5

    # Tratando a vigessima sexta coluna
    if vetorFinal[i][8] == '1':
        vetorFinal[i][8] = 1
    elif vetorFinal[i][8] == '2':
        vetorFinal[i][8] = 2
    elif vetorFinal[i][8] == '3':
        vetorFinal[i][8] = 3
    elif vetorFinal[i][8] == '4':
        vetorFinal[i][8] = 4
    elif vetorFinal[i][8] == '5':
        vetorFinal[i][8] = 5

    # Tratando a vigessima setima coluna
    if vetorFinal[i][9] == '1':
        vetorFinal[i][9] = 1
    elif vetorFinal[i][9] == '2':
        vetorFinal[i][9] = 2
    elif vetorFinal[i][9] == '3':
        vetorFinal[i][9] = 3
    elif vetorFinal[i][9] == '4':
        vetorFinal[i][9] = 4
    elif vetorFinal[i][9] == '5':
        vetorFinal[i][9] = 5

    # Tratando a vigessima oitava coluna
    if vetorFinal[i][10] == '1':
        vetorFinal[i][10] = 1
    elif vetorFinal[i][10] == '2':
        vetorFinal[i][10] = 2
    elif vetorFinal[i][10] == '3':
        vetorFinal[i][10] = 3
    elif vetorFinal[i][10] == '4':
        vetorFinal[i][10] = 4
    elif vetorFinal[i][10] == '5':
        vetorFinal[i][10] = 5

    # Tratando a vigessima nona coluna
    if vetorFinal[i][11] == '1':
        vetorFinal[i][11] = 1
    elif vetorFinal[i][11] == '2':
        vetorFinal[i][11] = 2
    elif vetorFinal[i][11] == '3':
        vetorFinal[i][11] = 3
    elif vetorFinal[i][11] == '4':
        vetorFinal[i][11] = 4
    elif vetorFinal[i][11] == '5':
        vetorFinal[i][11] = 5

   # Tratando a trigessima coluna
    for x in range(92):
        if vetorFinal[i][12] == str(x):
            vetorFinal[i][12] = x

   # Tratando a trigessima primeira coluna
    if vetorFinal[i][13] == '"0"':
        vetorFinal[i][13] = 0
    elif vetorFinal[i][13] == '"1"':
        vetorFinal[i][13] = 1
    elif vetorFinal[i][13] == '"2"':
        vetorFinal[i][13] = 2
    elif vetorFinal[i][13] == '"3"':
        vetorFinal[i][13] = 3
    elif vetorFinal[i][13] == '"4"':
        vetorFinal[i][13] = 4
    elif vetorFinal[i][13] == '"5"':
        vetorFinal[i][13] = 5
    elif vetorFinal[i][13] == '"6"':
        vetorFinal[i][13] = 6
    elif vetorFinal[i][13] == '"7"':
        vetorFinal[i][13] = 7
    elif vetorFinal[i][13] == '"8"':
        vetorFinal[i][13] = 8
    elif vetorFinal[i][13] == '"9"':
        vetorFinal[i][13] = 9
    elif vetorFinal[i][13] == '"10"':
        vetorFinal[i][13] = 10
    elif vetorFinal[i][13] == '"11"':
        vetorFinal[i][13] = 11
    elif vetorFinal[i][13] == '"12"':
        vetorFinal[i][13] = 12
    elif vetorFinal[i][13] == '"13"':
        vetorFinal[i][13] = 13
    elif vetorFinal[i][13] == '"14"':
        vetorFinal[i][13] = 14
    elif vetorFinal[i][13] == '"15"':
        vetorFinal[i][13] = 15
    elif vetorFinal[i][13] == '"16"':
        vetorFinal[i][13] = 16
    elif vetorFinal[i][13] == '"17"':
        vetorFinal[i][13] = 17
    elif vetorFinal[i][13] == '"18"':
        vetorFinal[i][13] = 18
    elif vetorFinal[i][13] == '"19"':
        vetorFinal[i][13] = 19
    elif vetorFinal[i][13] == '"20"':
        vetorFinal[i][13] = 20

# Tratando a trigessima segunda coluna
    if vetorFinal[i][14] == '"0"':
        vetorFinal[i][14] = 0
    elif vetorFinal[i][14] == '"1"':
        vetorFinal[i][14] = 1
    elif vetorFinal[i][14] == '"2"':
        vetorFinal[i][14] = 2
    elif vetorFinal[i][14] == '"3"':
        vetorFinal[i][14] = 3
    elif vetorFinal[i][14] == '"4"':
        vetorFinal[i][14] = 4
    elif vetorFinal[i][14] == '"5"':
        vetorFinal[i][14] = 5
    elif vetorFinal[i][14] == '"6"':
        vetorFinal[i][14] = 6
    elif vetorFinal[i][14] == '"7"':
        vetorFinal[i][14] = 7
    elif vetorFinal[i][14] == '"8"':
        vetorFinal[i][14] = 8
    elif vetorFinal[i][14] == '"9"':
        vetorFinal[i][14] = 9
    elif vetorFinal[i][14] == '"10"':
        vetorFinal[i][14] = 10
    elif vetorFinal[i][14] == '"11"':
        vetorFinal[i][14] = 11
    elif vetorFinal[i][14] == '"12"':
        vetorFinal[i][14] = 12
    elif vetorFinal[i][14] == '"13"':
        vetorFinal[i][14] = 13
    elif vetorFinal[i][14] == '"14"':
        vetorFinal[i][14] = 14
    elif vetorFinal[i][14] == '"15"':
        vetorFinal[i][14] = 15
    elif vetorFinal[i][14] == '"16"':
        vetorFinal[i][14] = 16
    elif vetorFinal[i][14] == '"17"':
        vetorFinal[i][14] = 17
    elif vetorFinal[i][14] == '"18"':
        vetorFinal[i][14] = 18
    elif vetorFinal[i][14] == '"19"':
        vetorFinal[i][14] = 19
    elif vetorFinal[i][14] == '"20"':
        vetorFinal[i][14] = 20

    # Tratando a ultima coluna
    if vetorFinal[i][15] == '0\n':
        vetorFinal[i][15] = 0
    elif vetorFinal[i][15] == '1\n':
        vetorFinal[i][15] = 1
    elif vetorFinal[i][15] == '2\n':
        vetorFinal[i][15] = 1
    elif vetorFinal[i][15] == '3\n':
        vetorFinal[i][15] = 3
    elif vetorFinal[i][15] == '4\n':
        vetorFinal[i][15] = 4
    elif vetorFinal[i][15] == '5\n':
        vetorFinal[i][15] = 5
    elif vetorFinal[i][15] == '6\n':
        vetorFinal[i][15] = 6
    elif vetorFinal[i][15] == '7\n':
        vetorFinal[i][15] = 7
    elif vetorFinal[i][15] == '8\n':
        vetorFinal[i][15] = 8
    elif vetorFinal[i][15] == '9\n':
        vetorFinal[i][15] = 9
    elif vetorFinal[i][15] == '10\n':
        vetorFinal[i][15] = 10
    elif vetorFinal[i][15] == '11\n':
        vetorFinal[i][15] = 11
    elif vetorFinal[i][15] == '12\n':
        vetorFinal[i][15] = 12
    elif vetorFinal[i][15] == '13\n':
        vetorFinal[i][15] = 13
    elif vetorFinal[i][15] == '14\n':
        vetorFinal[i][15] = 14
    elif vetorFinal[i][15] == '15\n':
        vetorFinal[i][15] = 15
    elif vetorFinal[i][15] == '16\n':
        vetorFinal[i][15] = 16
    elif vetorFinal[i][15] == '17\n':
        vetorFinal[i][15] = 17
    elif vetorFinal[i][15] == '18\n':
        vetorFinal[i][15] = 18
    elif vetorFinal[i][15] == '19\n':
        vetorFinal[i][15] = 19
    elif vetorFinal[i][15] == '20\n':
        vetorFinal[i][15] = 20

#print(f"Vetorfinal: {vetorFinal}")

studensNp = np.array(vetorFinal)
def separarX(data):
    studentsX = []
    for i in range(len(data)):
        studentsX.append(np.delete(data[i], [15]))
    return studentsX

def separarY(data):
    studentsY = []
    for i in range(len(data)):
        studentsY.append(np.delete(data[i], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    studentsY = np.array(studentsY)
    return studentsY

estudantesX = separarX(studensNp)
estudantesY = separarY(studensNp)
estudantesY = estudantesY.ravel()

def studentsTreinoTesteNumerico():
    x_treino, x_teste, y_treino, y_teste = train_test_split(estudantesX, estudantesY, test_size=0.5)
    return x_treino, x_teste, y_treino, y_teste

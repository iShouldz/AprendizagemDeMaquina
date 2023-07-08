"""
Converta todos os atributos da base para numéricos.

"""

def imprimir():
    for i in studentsSplitados:
        print(i)


studentsSplitados = []
students = open("student-mat.csv", "r")
linhasEstudantes = students.readlines()

#Splita pelo ; para poder ter colunas para tratar
for i in linhasEstudantes:
    teste = i.split(";")
    studentsSplitados.append(teste)
print(studentsSplitados[1][31])



for i in studentsSplitados:
    print(i)

for i in range(len(studentsSplitados)):
    # Tratando primeira coluna
    if studentsSplitados[i][0] == '"GP"':
        studentsSplitados[i][0] = 0
    elif studentsSplitados[i][0] == '"MS"':
        studentsSplitados[i][0] = 1

    # Tratando a segunda coluna
    if studentsSplitados[i][1] == '"F"':
        studentsSplitados[i][1] = 0
    elif studentsSplitados[i][1] == '"M"':
        studentsSplitados[i][1] = 1

    # Tratando a terceira coluna
    if studentsSplitados[i][2] == '15':
        studentsSplitados[i][2] = 15
    elif studentsSplitados[i][2] == '16':
        studentsSplitados[i][2] = 16
    elif studentsSplitados[i][2] == '17':
        studentsSplitados[i][2] = 17
    elif studentsSplitados[i][2] == '18':
        studentsSplitados[i][2] = 18
    elif studentsSplitados[i][2] == '19':
        studentsSplitados[i][2] = 19
    elif studentsSplitados[i][2] == '20':
        studentsSplitados[i][2] = 20
    elif studentsSplitados[i][2] == '21':
        studentsSplitados[i][2] = 21
    elif studentsSplitados[i][2] == '22':
        studentsSplitados[i][2] = 22

    # Tratando a quarta coluna
    if studentsSplitados[i][3] == '"U"':
        studentsSplitados[i][3] = 0
    elif studentsSplitados[i][3] == '"R"':
        studentsSplitados[i][3] = 1

    # Tratando a quinta coluna
    if studentsSplitados[i][4] == '"LE3"':
        studentsSplitados[i][4] = 0
    elif studentsSplitados[i][4] == '"GT3"':
        studentsSplitados[i][4] = 1

    # Tratando a sexta coluna
    if studentsSplitados[i][5] == '"T"':
        studentsSplitados[i][5] = 0
    elif studentsSplitados[i][5] == '"A"':
        studentsSplitados[i][5] = 1

    # Tratando a setima coluna
    if studentsSplitados[i][6] == '0':
        studentsSplitados[i][6] = 0
    elif studentsSplitados[i][6] == '1':
        studentsSplitados[i][6] = 1
    elif studentsSplitados[i][6] == '2':
        studentsSplitados[i][6] = 2
    elif studentsSplitados[i][6] == '3':
        studentsSplitados[i][6] = 3
    elif studentsSplitados[i][6] == '4':
        studentsSplitados[i][6] = 4

    # Tratando a oitava coluna
    if studentsSplitados[i][7] == '0':
        studentsSplitados[i][7] = 0
    elif studentsSplitados[i][7] == '1':
        studentsSplitados[i][7] = 1
    elif studentsSplitados[i][7] == '2':
        studentsSplitados[i][7] = 2
    elif studentsSplitados[i][7] == '3':
        studentsSplitados[i][7] = 3
    elif studentsSplitados[i][7] == '4':
        studentsSplitados[i][7] = 4

    # Tratando a nona coluna
    remover1 = studentsSplitados[i][8]
    remover2 = studentsSplitados[i][9]

    if studentsSplitados[i][8] == '"teacher"':
        studentsSplitados[i].insert(8, 1)
    else:
        studentsSplitados[i].insert(8, 0)

    if studentsSplitados[i][9] == '"health"':
        studentsSplitados[i].insert(9, 1)
    else:
        studentsSplitados[i].insert(9, 0)

    if studentsSplitados[i][10] == '"services"':
        studentsSplitados[i].insert(10, 1)
    else:
        studentsSplitados[i].insert(10, 0)

    if studentsSplitados[i][11] == '"at_home"':
        studentsSplitados[i].insert(11, 1)
    else:
        studentsSplitados[i].insert(11, 0)

    if studentsSplitados[i][12] == '"other"':
        studentsSplitados[i].insert(12, 1)
    else:
        studentsSplitados[i].insert(12, 0)
    studentsSplitados[i].remove(remover1)

    # Tratando a decima coluna
    if studentsSplitados[i][13] == '"teacher"':
        studentsSplitados[i].insert(13, 1)
    else:
        studentsSplitados[i].insert(13, 0)

    if studentsSplitados[i][14] == '"health"':
        studentsSplitados[i].insert(14, 1)
    else:
        studentsSplitados[i].insert(14, 0)

    if studentsSplitados[i][15] == '"services"':
        studentsSplitados[i].insert(15, 1)
    else:
        studentsSplitados[i].insert(15, 0)

    if studentsSplitados[i][16] == '"at_home"':
        studentsSplitados[i].insert(16, 1)
    else:
        studentsSplitados[i].insert(16, 0)

    if studentsSplitados[i][17] == '"other"':
        studentsSplitados[i].insert(17, 1)
    else:
        studentsSplitados[i].insert(17, 0)
    #Remover o index 18 e 19, correspondente ao antigo atributo
    studentsSplitados[i].remove(remover2)

    # Tratando a decima primeira coluna
    remover1 = studentsSplitados[i][18]
    if studentsSplitados[i][18] == '"home"':
        studentsSplitados[i].insert(18, 1)
    else:
        studentsSplitados[i].insert(18, 0)

    if studentsSplitados[i][19] == '"reputation"':
        studentsSplitados[i].insert(19, 1)
    else:
        studentsSplitados[i].insert(19, 0)

    if studentsSplitados[i][20] == '"course"':
        studentsSplitados[i].insert(20, 1)
    else:
        studentsSplitados[i].insert(20, 0)

    if studentsSplitados[i][21] == '"other"':
        studentsSplitados[i].insert(21, 1)
    else:
        studentsSplitados[i].insert(21, 0)
    studentsSplitados[i].remove(remover1)

    # Tratando a decima segunda coluna
    remover1 = studentsSplitados[i][22]
    if studentsSplitados[i][22] == '"mother"':
        studentsSplitados[i].insert(22, 1)
    else:
        studentsSplitados[i].insert(22, 0)

    if studentsSplitados[i][23] == '"father"':
        studentsSplitados[i].insert(23, 1)
    else:
        studentsSplitados[i].insert(23, 0)

    if studentsSplitados[i][24] == '"other"':
        studentsSplitados[i].insert(24, 1)
    else:
        studentsSplitados[i].insert(24, 0)
    studentsSplitados[i].remove(remover1)

    # Tratando a decima terceira coluna
    if studentsSplitados[i][25] == '1':
        studentsSplitados[i][25] = 1
    elif studentsSplitados[i][25] == '2':
        studentsSplitados[i][25] = 2
    elif studentsSplitados[i][25] == '3':
        studentsSplitados[i][25] = 3
    elif studentsSplitados[i][25] == '4':
        studentsSplitados[i][25] = 4

    # Tratando a decima quarta coluna
    if studentsSplitados[i][26] == '1':
        studentsSplitados[i][26] = 1
    elif studentsSplitados[i][26] == '2':
        studentsSplitados[i][26] = 2
    elif studentsSplitados[i][26] == '3':
        studentsSplitados[i][26] = 3
    elif studentsSplitados[i][26] == '4':
        studentsSplitados[i][26] = 4

    # Tratando a decima quinta coluna
    if studentsSplitados[i][27] == '0':
        studentsSplitados[i][27] = 0
    elif studentsSplitados[i][27] == '1':
        studentsSplitados[i][27] = 1
    elif studentsSplitados[i][27] == '2':
        studentsSplitados[i][27] = 2
    elif studentsSplitados[i][27] == '3':
        studentsSplitados[i][27] = 3
    elif studentsSplitados[i][27] == '4':
        studentsSplitados[i][27] = 4

    # Tratando a decima sexta coluna
    if studentsSplitados[i][28] == '"no"':
        studentsSplitados[i][28] = 0
    elif studentsSplitados[i][28] == '"yes"':
        studentsSplitados[i][28] = 1

    # Tratando a decima setima coluna
    if studentsSplitados[i][29] == '"no"':
        studentsSplitados[i][29] = 0
    elif studentsSplitados[i][29] == '"yes"':
        studentsSplitados[i][29] = 1

    # Tratando a decima oitava coluna
    if studentsSplitados[i][30] == '"no"':
        studentsSplitados[i][30] = 0
    elif studentsSplitados[i][30] == '"yes"':
        studentsSplitados[i][30] = 1

    # Tratando a decima nona coluna
    if studentsSplitados[i][31] == '"no"':
        studentsSplitados[i][31] = 0
    elif studentsSplitados[i][31] == '"yes"':
        studentsSplitados[i][31] = 1

     # Tratando a vigesima coluna
    if studentsSplitados[i][32] == '"no"':
        studentsSplitados[i][32] = 0
    elif studentsSplitados[i][32] == '"yes"':
        studentsSplitados[i][32] = 1

    # Tratando a vigesima primeira coluna
    if studentsSplitados[i][33] == '"no"':
        studentsSplitados[i][33] = 0
    elif studentsSplitados[i][33] == '"yes"':
        studentsSplitados[i][33] = 1

    # Tratando a vigesima segunda coluna
    if studentsSplitados[i][34] == '"no"':
        studentsSplitados[i][34] = 0
    elif studentsSplitados[i][34] == '"yes"':
        studentsSplitados[i][34] = 1

    # Tratando a vigesima terceira coluna
    if studentsSplitados[i][35] == '"no"':
        studentsSplitados[i][35] = 0
    elif studentsSplitados[i][35] == '"yes"':
        studentsSplitados[i][35] = 1

    # Tratando a vigesima quarta coluna
    if studentsSplitados[i][36] == '1':
        studentsSplitados[i][36] = 1
    elif studentsSplitados[i][36] == '2':
        studentsSplitados[i][36] = 2
    elif studentsSplitados[i][36] == '3':
        studentsSplitados[i][36] = 3
    elif studentsSplitados[i][36] == '4':
        studentsSplitados[i][36] = 4
    elif studentsSplitados[i][36] == '5':
        studentsSplitados[i][36] = 5

    # Tratando a vigessima quinta coluna
    if studentsSplitados[i][37] == '1':
        studentsSplitados[i][37] = 1
    elif studentsSplitados[i][37] == '2':
        studentsSplitados[i][37] = 2
    elif studentsSplitados[i][37] == '3':
        studentsSplitados[i][37] = 3
    elif studentsSplitados[i][37] == '4':
        studentsSplitados[i][37] = 4
    elif studentsSplitados[i][37] == '5':
        studentsSplitados[i][37] = 5

    # Tratando a vigessima sexta coluna
    if studentsSplitados[i][38] == '1':
        studentsSplitados[i][38] = 1
    elif studentsSplitados[i][38] == '2':
        studentsSplitados[i][38] = 2
    elif studentsSplitados[i][38] == '3':
        studentsSplitados[i][38] = 3
    elif studentsSplitados[i][38] == '4':
        studentsSplitados[i][38] = 4
    elif studentsSplitados[i][38] == '5':
        studentsSplitados[i][38] = 5

    # Tratando a vigessima setima coluna
    if studentsSplitados[i][39] == '1':
        studentsSplitados[i][39] = 1
    elif studentsSplitados[i][39] == '2':
        studentsSplitados[i][39] = 2
    elif studentsSplitados[i][39] == '3':
        studentsSplitados[i][39] = 3
    elif studentsSplitados[i][39] == '4':
        studentsSplitados[i][39] = 4
    elif studentsSplitados[i][39] == '5':
        studentsSplitados[i][39] = 5

    # Tratando a vigessima oitava coluna
    if studentsSplitados[i][40] == '1':
        studentsSplitados[i][40] = 1
    elif studentsSplitados[i][40] == '2':
        studentsSplitados[i][40] = 2
    elif studentsSplitados[i][40] == '3':
        studentsSplitados[i][40] = 3
    elif studentsSplitados[i][40] == '4':
        studentsSplitados[i][40] = 4
    elif studentsSplitados[i][40] == '5':
        studentsSplitados[i][40] = 5

    # Tratando a vigessima nona coluna
    if studentsSplitados[i][41] == '1':
        studentsSplitados[i][41] = 1
    elif studentsSplitados[i][41] == '2':
        studentsSplitados[i][41] = 2
    elif studentsSplitados[i][41] == '3':
        studentsSplitados[i][41] = 3
    elif studentsSplitados[i][41] == '4':
        studentsSplitados[i][41] = 4
    elif studentsSplitados[i][41] == '5':
        studentsSplitados[i][41] = 5

   # Tratando a trigessima coluna
    for x in range(92):
        if studentsSplitados[i][42] == str(x):
            studentsSplitados[i][42] = x

   # Tratando a trigessima primeira coluna
    if studentsSplitados[i][43] == '"0"':
        studentsSplitados[i][43] = 0
    elif studentsSplitados[i][43] == '"1"':
        studentsSplitados[i][43] = 1
    elif studentsSplitados[i][43] == '"2"':
        studentsSplitados[i][43] = 1
    elif studentsSplitados[i][43] == '"3"':
        studentsSplitados[i][43] = 3
    elif studentsSplitados[i][43] == '"4"':
        studentsSplitados[i][43] = 4
    elif studentsSplitados[i][43] == '"5"':
        studentsSplitados[i][43] = 5
    elif studentsSplitados[i][43] == '"6"':
        studentsSplitados[i][43] = 6
    elif studentsSplitados[i][43] == '"7"':
        studentsSplitados[i][43] = 7
    elif studentsSplitados[i][43] == '"8"':
        studentsSplitados[i][43] = 8
    elif studentsSplitados[i][43] == '"9"':
        studentsSplitados[i][43] = 9
    elif studentsSplitados[i][43] == '"10"':
        studentsSplitados[i][43] = 10
    elif studentsSplitados[i][43] == '"11"':
        studentsSplitados[i][43] = 11
    elif studentsSplitados[i][43] == '"12"':
        studentsSplitados[i][43] = 12
    elif studentsSplitados[i][43] == '"13"':
        studentsSplitados[i][43] = 13
    elif studentsSplitados[i][43] == '"14"':
        studentsSplitados[i][43] = 14
    elif studentsSplitados[i][43] == '"15"':
        studentsSplitados[i][43] = 15
    elif studentsSplitados[i][43] == '"16"':
        studentsSplitados[i][43] = 16
    elif studentsSplitados[i][43] == '"17"':
        studentsSplitados[i][43] = 17
    elif studentsSplitados[i][43] == '"18"':
        studentsSplitados[i][43] = 18
    elif studentsSplitados[i][43] == '"19"':
        studentsSplitados[i][43] = 19
    elif studentsSplitados[i][43] == '"20"':
        studentsSplitados[i][43] = 20

# Tratando a trigessima segunda coluna
    if studentsSplitados[i][44] == '"0"':
        studentsSplitados[i][44] = 0
    elif studentsSplitados[i][44] == '"1"':
        studentsSplitados[i][44] = 1
    elif studentsSplitados[i][44] == '"2"':
        studentsSplitados[i][44] = 1
    elif studentsSplitados[i][44] == '"3"':
        studentsSplitados[i][44] = 3
    elif studentsSplitados[i][44] == '"4"':
        studentsSplitados[i][44] = 4
    elif studentsSplitados[i][44] == '"5"':
        studentsSplitados[i][44] = 5
    elif studentsSplitados[i][44] == '"6"':
        studentsSplitados[i][44] = 6
    elif studentsSplitados[i][44] == '"7"':
        studentsSplitados[i][44] = 7
    elif studentsSplitados[i][44] == '"8"':
        studentsSplitados[i][44] = 8
    elif studentsSplitados[i][44] == '"9"':
        studentsSplitados[i][44] = 9
    elif studentsSplitados[i][44] == '"10"':
        studentsSplitados[i][44] = 10
    elif studentsSplitados[i][44] == '"11"':
        studentsSplitados[i][44] = 11
    elif studentsSplitados[i][44] == '"12"':
        studentsSplitados[i][44] = 12
    elif studentsSplitados[i][44] == '"13"':
        studentsSplitados[i][44] = 13
    elif studentsSplitados[i][44] == '"14"':
        studentsSplitados[i][44] = 14
    elif studentsSplitados[i][44] == '"15"':
        studentsSplitados[i][44] = 15
    elif studentsSplitados[i][44] == '"16"':
        studentsSplitados[i][44] = 16
    elif studentsSplitados[i][44] == '"17"':
        studentsSplitados[i][44] = 17
    elif studentsSplitados[i][44] == '"18"':
        studentsSplitados[i][44] = 18
    elif studentsSplitados[i][44] == '"19"':
        studentsSplitados[i][44] = 19
    elif studentsSplitados[i][44] == '"20"':
        studentsSplitados[i][44] = 20

    # Tratando a ultima coluna
    if studentsSplitados[i][45] == '0\n':
        studentsSplitados[i][45] = 0
    elif studentsSplitados[i][45] == '1\n':
        studentsSplitados[i][45] = 1
    elif studentsSplitados[i][45] == '2\n':
        studentsSplitados[i][45] = 1
    elif studentsSplitados[i][45] == '3\n':
        studentsSplitados[i][45] = 3
    elif studentsSplitados[i][45] == '4\n':
        studentsSplitados[i][45] = 4
    elif studentsSplitados[i][45] == '5\n':
        studentsSplitados[i][45] = 5
    elif studentsSplitados[i][45] == '6\n':
        studentsSplitados[i][45] = 6
    elif studentsSplitados[i][45] == '7\n':
        studentsSplitados[i][45] = 7
    elif studentsSplitados[i][45] == '8\n':
        studentsSplitados[i][45] = 8
    elif studentsSplitados[i][45] == '9\n':
        studentsSplitados[i][45] = 9
    elif studentsSplitados[i][45] == '10\n':
        studentsSplitados[i][45] = 10
    elif studentsSplitados[i][45] == '11\n':
        studentsSplitados[i][45] = 11
    elif studentsSplitados[i][45] == '12\n':
        studentsSplitados[i][45] = 12
    elif studentsSplitados[i][45] == '13\n':
        studentsSplitados[i][45] = 13
    elif studentsSplitados[i][45] == '14\n':
        studentsSplitados[i][45] = 14
    elif studentsSplitados[i][45] == '15\n':
        studentsSplitados[i][45] = 15
    elif studentsSplitados[i][45] == '16\n':
        studentsSplitados[i][45] = 16
    elif studentsSplitados[i][45] == '17\n':
        studentsSplitados[i][45] = 17
    elif studentsSplitados[i][45] == '18\n':
        studentsSplitados[i][45] = 18
    elif studentsSplitados[i][45] == '19\n':
        studentsSplitados[i][45] = 19
    elif studentsSplitados[i][45] == '20\n':
        studentsSplitados[i][45] = 20
imprimir()

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


imprimir()

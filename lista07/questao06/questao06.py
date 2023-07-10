carrosSplitados = []
carro = open("../car.data", "r")
linhaCarro = carro.readlines()

def imprimir(base):
    for i in base:
        print(i)

#Splita pelo ; para poder ter colunas para tratar
for i in linhaCarro:
    teste = i.split(",")
    carrosSplitados.append(teste)
naoBinaria = []
naoBinaria = carrosSplitados
for i in range(len(carrosSplitados)):
    #primeiro atributo
    if carrosSplitados[i][0] == 'vhigh':
        carrosSplitados[i][0] = 1
    elif carrosSplitados[i][0] == 'high':
        carrosSplitados[i][0] = 2
    elif carrosSplitados[i][0] == 'med':
        carrosSplitados[i][0] = 3
    elif carrosSplitados[i][0] == 'low':
        carrosSplitados[i][0] = 4

    #segundo atributo
    if carrosSplitados[i][1] == 'vhigh':
        carrosSplitados[i][1] = 1
    elif carrosSplitados[i][1] == 'high':
        carrosSplitados[i][1] = 2
    elif carrosSplitados[i][1] == 'med':
        carrosSplitados[i][1] = 3
    elif carrosSplitados[i][1] == 'low':
        carrosSplitados[i][1] = 4

    #terceiro atributo
    if carrosSplitados[i][2] == '2':
        carrosSplitados[i][2] = 1
    elif carrosSplitados[i][2] == '3':
        carrosSplitados[i][2] = 2
    elif carrosSplitados[i][2] == '4':
        carrosSplitados[i][2] = 3
    elif carrosSplitados[i][2] == '5more':
        carrosSplitados[i][2] = 4

    #quarto atributo
    if carrosSplitados[i][3] == '2':
        carrosSplitados[i][3] = 1
    elif carrosSplitados[i][3] == '4':
        carrosSplitados[i][3] = 2
    elif carrosSplitados[i][3] == 'more':
        carrosSplitados[i][3] = 3

    #Quinto atributo
    if carrosSplitados[i][4] == 'small':
        carrosSplitados[i][4] = 1
    elif carrosSplitados[i][4] == 'med':
        carrosSplitados[i][4] = 2
    elif carrosSplitados[i][4] == 'big':
        carrosSplitados[i][4] = 3

    #Sexto atributo
    if carrosSplitados[i][5] == 'low':
        carrosSplitados[i][5] = 1
    elif carrosSplitados[i][5] == 'med':
        carrosSplitados[i][5] = 2
    elif carrosSplitados[i][5] == 'high':
        carrosSplitados[i][5] = 3

    #classe
    if carrosSplitados[i][6] == 'unacc\n':
        carrosSplitados[i][6] = 1
    elif carrosSplitados[i][6] == 'acc\n':
        carrosSplitados[i][6] = 2
    elif carrosSplitados[i][6] == 'good\n':
        carrosSplitados[i][6] = 3
    elif carrosSplitados[i][6] == 'vgood\n':
        carrosSplitados[i][6] = 4
imprimir(carrosSplitados)


baseSplitados = []
novaBaseDados = []
data = open('balance-scale.txt', 'r')
linhas = data.readlines()
for i in linhas:
    teste = i.split(',')
    baseSplitados.append(teste)

#tratando base de dados conforme descrito no arquivo de info da base
for i in baseSplitados:
    classe = i[0]
    balancaEsquerda = int(i[1]) * int(i[2])
    balancaDireita = int(i[3]) * int(i[4])
    novaBaseDados.append([classe, balancaEsquerda, balancaDireita])

print(novaBaseDados)
caracteristica1 = caracteristica2 = caracteristica3 = caracteristica4 = caracteristica5 = 0

for i in range(len(novaBaseDados)):
    if novaBaseDados[i][0] == 'B' and novaBaseDados[i][1] == 1:
        caracteristica1 += 1
    elif novaBaseDados[i][0] == 'B' and novaBaseDados[i][1] == 2:
        caracteristica2 += 1
    elif novaBaseDados[i][0] == 'B' and novaBaseDados[i][1] == 3:
        caracteristica3 += 1
    elif novaBaseDados[i][0] == 'B' and novaBaseDados[i][1] == 4:
        caracteristica4 += 1
    elif novaBaseDados[i][0] == 'B' and novaBaseDados[i][1] == 5:
        caracteristica5 += 1

lista = [caracteristica1, caracteristica2, caracteristica3, caracteristica4, caracteristica5]
print(lista)

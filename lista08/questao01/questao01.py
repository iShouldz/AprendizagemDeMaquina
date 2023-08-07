baseSplitados = []
data = open('balance-scale.txt', 'r')
linhas = data.readlines()
for i in linhas:
    teste = i.split(',')
    baseSplitados.append(teste)
print(baseSplitados)

contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0
arrayF = []

# Tratando primeira caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][1] == '1' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][1] == '2' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][1] == '3' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][1] == '4' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][1] == '5' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][0] == 'R':
        contar5 += 1

atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]
atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando segunda caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][2] == '1' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][2] == '2' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][2] == '3' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][2] == '4' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][2] == '5' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando terceira caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando quarta caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][4] == '1\n' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][4] == '2\n' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][4] == '3\n' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][4] == '4\n' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][4] == '5\n' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)
print('L - B - R (Escolha arbitraria)')
for i in arrayF:
    print(i)

#Raiz - [1] - [cada caracteristica]

contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0
arrayF = []

# Tratando primeira caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][1] == '1' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][1] == '2' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][1] == '3' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][1] == '4' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][1] == '5' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar5 += 1

atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]
atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando segunda caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][2] == '1' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][2] == '2' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][2] == '3' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][2] == '4' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][2] == '5' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando quarta caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '1' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)
print('Seja escolhido como raiz o atributo 2 (coluna 3):\n'
      'Seja Raiz - [1] - [cada caracteristica][1-2-4]')
for i in arrayF:
    print(i)

# Raiz - [2] - [cada caracteristica]

contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0
arrayF = []

# Tratando primeira caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][1] == '1' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][1] == '2' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][1] == '3' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][1] == '4' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][1] == '5' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar5 += 1

atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]
atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando segunda caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][2] == '1' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][2] == '2' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][2] == '3' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][2] == '4' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][2] == '5' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando quarta caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '2' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)
print('Seja escolhido como raiz o atributo 2 (coluna 3):\n'
      'Seja Raiz - [2] - [cada caracteristica][1-2-4]')
for i in arrayF:
    print(i)

# Raiz - [3] - [cada caracteristica]

contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0
arrayF = []

# Tratando primeira caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][1] == '1' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][1] == '2' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][1] == '3' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][1] == '4' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][1] == '5' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar5 += 1

atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]
atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando segunda caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][2] == '1' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][2] == '2' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][2] == '3' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][2] == '4' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][2] == '5' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando quarta caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '3' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)
print('Seja escolhido como raiz o atributo 2 (coluna 3):\n'
      'Seja Raiz - [3] - [cada caracteristica][1-2-4]')
for i in arrayF:
    print(i)

# Raiz - [4] - [cada caracteristica]

contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0
arrayF = []

# Tratando primeira caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][1] == '1' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][1] == '2' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][1] == '3' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][1] == '4' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][1] == '5' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar5 += 1

atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]
atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando segunda caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][2] == '1' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][2] == '2' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][2] == '3' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][2] == '4' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][2] == '5' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

#Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando quarta caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '4' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)
print('Seja escolhido como raiz o atributo 2 (coluna 3):\n'
      'Seja Raiz - [4] - [cada caracteristica][1-2-4]')
for i in arrayF:
    print(i)

# Raiz - [5] - [cada caracteristica]

contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0
arrayF = []

# Tratando primeira caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][1] == '1' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][1] == '1' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][1] == '2' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][1] == '2' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][1] == '3' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][1] == '3' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][1] == '4' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][1] == '4' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][1] == '5' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][1] == '5' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar5 += 1

atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]
atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

# Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando segunda caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][2] == '1' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][2] == '1' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][2] == '2' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][2] == '2' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][2] == '3' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][2] == '3' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][2] == '4' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][2] == '4' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][2] == '5' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][2] == '5' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)

# Reset contador
contal1 = contab1 = contar1 = 0
contal2 = contab2 = contar2 = 0
contal3 = contab3 = contar3 = 0
contal4 = contab4 = contar4 = 0
contal5 = contab5 = contar5 = 0

# Tratando quarta caracteristica
for k in range(len(linhas)):
    if baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab1 += 1
    elif baseSplitados[k][4] == '1\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar1 += 1

    if baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab2 += 1
    elif baseSplitados[k][4] == '2\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar2 += 1

    if baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab3 += 1
    elif baseSplitados[k][4] == '3\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar3 += 1

    if baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab4 += 1
    elif baseSplitados[k][4] == '4\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar4 += 1

    if baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'L':
        contal5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'B':
        contab5 += 1
    elif baseSplitados[k][4] == '5\n' and baseSplitados[k][3] == '5' and baseSplitados[k][0] == 'R':
        contar5 += 1
atributo1 = [contal1, contab1, contar1]
atributo2 = [contal2, contab2, contar2]
atributo3 = [contal3, contab3, contar3]
atributo4 = [contal4, contab4, contar4]
atributo5 = [contal5, contab5, contar5]

atemp = [atributo1, atributo2, atributo3, atributo4, atributo5]
arrayF.append(atemp)
print('Seja escolhido como raiz o atributo 2 (coluna 3):\n'
      'Seja Raiz - [5] - [cada caracteristica][1-2-4]')
for i in arrayF:
    print(i)


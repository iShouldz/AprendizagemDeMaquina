from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

x, y = load_wine(return_X_y=True)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, train_size=0.7)

def holdout():
    return x_treino, y_treino, x_teste, y_teste

def matrizConfusao(y_true, y_pred):
    labels = sorted(list(set(y_true + y_pred)))  # Possui todas as classes
    num_labels = len(labels) - 2
    matrix = [[0] * num_labels for _ in range(num_labels)]  # Starta a matriz

    for true, pred in zip(y_true, y_pred):
        matrix[labels.index(true)][labels.index(pred)] += 1 #Adiciona o elemento a matriz
    return matrix

def exibirMatrizConfusao(y_teste, y_knn, classes):
    cm = matrizConfusao(y_teste, y_knn)
    for k in range(0, 3):
        cm[k].append(classes[k])
    print(classes)
    for row in cm:
        print(row)

def recallByclass(matriz, classe):
    soma = 0
    numerador = matriz[classe][classe]
    for i in range(len(matriz[classe])):
        soma += matriz[classe][i]
    return numerador/soma

def precisaByclass(matriz, classe):
    soma = 0
    numerador = matriz[classe][classe]
    for i in range(len(matriz[classe])):
        soma += matriz[i][classe]
    return numerador / soma

def taxaDeAcerto(matriz, x_teste):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return (soma/len(x_teste)*100).__round__(2)

def medidaFbyClass(precisao, recall):
    return (2 * precisao * recall) / (precisao + recall)

"""
SE CLASSE = 0               SE CLASSE = 1               SE CLASSE = 2
|------||------||------|   |------||------||------|    |------||------||------|
|  vp  ||  fn  ||  fn  |   |  vn  ||  fp  ||  vn  |    |  vn  ||  vn  ||  fp  | 
|______||______||______|   |______||______||______|    |______||______||______| 
|------||------||------|   |------||------||------|    |------||------||------|    
|  fp  ||  vn  ||  vn  |   |  fn  ||  vp  ||  fn  |    |  vn  ||  vn  ||  fp  |
|______||______||______|   |______||______||______|    |______||______||______|
|------||------||------|   |------||------||------|    |------||------||------|
|  fp  ||  vn  ||  vn  |   |  vn  ||  fp  ||  vn  |    |  fn  ||  fn  ||  vp  |
|______||______||______|   |______||______||______|    |______||______||______|
"""
def taxaFP(matriz, classe):
    if classe == 0:
        fp = matriz[1][0] + matriz[2][0]
        vn = matriz[1][1] + matriz[1][2] + matriz[2][1] + matriz[2][2]
    elif classe == 1:
        fp = matriz[0][1] + matriz[2][1]
        vn = matriz[0][0] + matriz[0][2] + matriz[2][0] + matriz[2][2]
    else:
        fp = matriz[0][2] + matriz[1][2]
        vn = matriz[0][0] + matriz[0][1] + matriz[1][0] + matriz[1][1]
    return fp/(fp + vn)


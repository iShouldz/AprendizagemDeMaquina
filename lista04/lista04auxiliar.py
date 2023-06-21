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

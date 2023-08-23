from sklearn.neighbors import KNeighborsClassifier
from lista05.questoes.auxiliar import intervaloDeConfianca, mediaamostra
from sklearn.datasets import load_wine
from statistics import mean
from sklearn.metrics import accuracy_score
import numpy as np
import lista04B.questao02.auxiliar as aux

X, y = load_wine(return_X_y=True)
x_ = aux.carregar_wine()

def dividir_dados_treino_teste(X, y, tamanho_teste=0.2):
    num_amostras = X.shape[0]
    num_amostras_teste = int(num_amostras * tamanho_teste)

    indices_aleatorios = np.random.permutation(num_amostras)
    indices_teste = indices_aleatorios[:num_amostras_teste]
    indices_treino = indices_aleatorios[num_amostras_teste:]

    X_treino, X_teste = X[indices_treino], X[indices_teste]
    y_treino, y_teste = y[indices_treino], y[indices_teste]

    return X_treino, X_teste, y_treino, y_teste

def holdout_estratificado(X, y, tamanho_teste=0.2):
    num_teste = int(len(X) * tamanho_teste)
    # Embaralha os índices das amostras
    indices_embaralhados = np.arange(len(X))
    np.random.shuffle(indices_embaralhados)

    # Separa as amostras
    y_unicos = np.unique(y)
    qtd_amostras_classe = num_teste // len(y_unicos)

    indices_teste = []
    for classe in y_unicos:
        indices_classe = np.where(y == classe)[0]
        indices_classe_teste = indices_classe[:qtd_amostras_classe]
        indices_teste.extend(indices_classe_teste)
    indices_teste_extra = indices_embaralhados[:num_teste - len(indices_teste)]
    indices_teste.extend(indices_teste_extra)
    # índices das amostras de x_treino
    indices_treino = list(set(indices_embaralhados) - set(indices_teste))

    X_treino = X[indices_treino]
    y_treino = y[indices_treino]
    X_teste = X[indices_teste]
    y_teste = y[indices_teste]

    return X_treino, X_teste, y_treino, y_teste

def get_holdout(type, X, y):
    holdout = []
    for i in range(10):
        if type == "aleatorio":
            x_treino, x_teste, y_treino, y_teste = dividir_dados_treino_teste(X, y, tamanho_teste=0.1)
        elif type == 'estratificado':
            x_treino, x_teste, y_treino, y_teste = holdout_estratificado(X, y, tamanho_teste=0.1)
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(accuracy_score(resultado, y_teste))
    return holdout

def somaFold(lista):
    total = 0
    for i in lista:
        total += i
    return total

def leave_one_out(X, y):
    taxaAcerto = []
    for i in range(len(X)):
        # Conjunto de x_teste por partição
        X_teste = X[i:i+1]
        y_teste = y[i:i+1]

        # Conjunto de x_treino, as demais partições
        X_treino = np.delete(X, i, axis=0)
        y_treino = np.delete(y, i)

        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(X_treino, y_treino)
        acuracia = knn.score(X_teste, y_teste)

        taxaAcerto.append(acuracia)
    return taxaAcerto

def cross_validation_estratificado(X, y, num_folds=10, random_state=None):
    tamanho_fold = len(X) // num_folds

    # Embaralha os índices das amostras
    indices_embaralhados = np.arange(len(X))
    if random_state is not None:
        np.random.seed(random_state)
    np.random.shuffle(indices_embaralhados)

    # Inicializa a lista para armazenar as acurácias
    taxaAcerto = []
    for i in range(num_folds):
        inicio_fold = i * tamanho_fold
        fim_fold = (i + 1) * tamanho_fold
        indices_teste = indices_embaralhados[inicio_fold:fim_fold]

        # partições do mesmo tamanho
        if i == num_folds - 1:
            indices_teste = indices_embaralhados[inicio_fold:]
        indices_treino = list(set(indices_embaralhados) - set(indices_teste))

        # divisão dos conjuntos de x_treino e x_teste
        X_treino = X[indices_treino]
        y_treino = y[indices_treino]
        X_teste = X[indices_teste]
        y_teste = y[indices_teste]

        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(X_treino, y_treino)
        acuracia = knn.score(X_teste, y_teste)
        taxaAcerto.append(acuracia)
    return taxaAcerto

holdoutE = get_holdout("estratificado", X, y)
holdout = get_holdout("aleatorio", X, y)

print(f'Holdout aleatorio 90/10\nMedia: {mediaamostra(holdout)}\nTaxas de acerto\n'
      f'{holdout}\n')
print(f'Holdout estratificado 90/10\nMedia: {mediaamostra(holdoutE)}\nTaxas de acerto\n'
      f'{holdoutE}\n')

tenCross = cross_validation_estratificado(X, y, num_folds=10)
print(f'10-fold cross validation estratificado\nMedia:{mediaamostra(tenCross)}'
      f'\nTaxas de acerto: {tenCross}\nTaxa de acerto somada: {somaFold(tenCross)}\n')

leave_one = leave_one_out(X, y)
print(f'Leave-one-out:\nAcerto:{mediaamostra(leave_one)}\n')

####################################################################################################3

print("SEM A ULTIMA COLUNA: ")
holdoutColuna = get_holdout("estratificado", x_, y)
holdoutColuna2 = get_holdout("aleatorio", x_, y)
print(f'Holdout aleatorio 90/10 SEM COLUNA\nMedia: {mean(holdoutColuna)}\nTaxas de acerto\n'
      f'{holdoutColuna}\n')
print(f'Holdout estratificado 90/10 SEM COLUNA\nMedia: {mean(holdoutColuna2)}\nTaxas de acerto\n'
      f'{holdoutColuna2}\n')

tenCross2 = cross_validation_estratificado(x_, y, num_folds=10)
print(f'10-fold cross validation estratificado SEM COLUNA\nMedia:{mean(tenCross)}'
      f'\nTaxas de acerto: {tenCross}\nTaxa de acerto somada: {somaFold(tenCross)}\n')

leave_one2 = leave_one_out(x_, y)
print(f'Leave-one-out:SEM COLUNA\nAcerto:{mean(leave_one)}')

#holdout aleatorio:
intervaloHA = intervaloDeConfianca(aux.calcularDif(holdout, holdoutColuna2))
#holdout estratificado:
intervaloHE = intervaloDeConfianca(aux.calcularDif(holdoutE, holdoutColuna))
#10-cross
intervaloE = intervaloDeConfianca(aux.calcularDif(tenCross, tenCross2))
#leave
intervaloLeave = intervaloDeConfianca(aux.calcularDif(leave_one, leave_one2))

print(f'HOLDOUTS ALEATORIOS: \nIntervalo de confiança: {intervaloHA}\nMedia com coluna: {mean(holdout)}\n'
      f'Media sem coluna: {mean(holdoutColuna2)}\n')
print(f'HOLDOUTS ESTRATIFICADO: \nIntervalo de confiança: {intervaloHE}\nMedia com coluna: {mean(holdoutE)}\n'
      f'Media sem coluna: {mean(holdoutColuna)}\n')

print(f'10-CROSS: \nIntervalo de confiança: {intervaloE}\nMedia com coluna: {mean(tenCross)}\n'
      f'Media sem coluna: {mean(tenCross2)}\n')

print(f'LEAVE ONE OUT: \nIntervalo de confiança: {intervaloLeave}\nMedia com coluna: {mean(leave_one)}\n'
      f'Media sem coluna: {mean(leave_one2)}\n')

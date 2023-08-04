from sklearn.neighbors import KNeighborsClassifier
from lista05.questoes.auxiliar import intervaloDeConfianca, mediaamostra
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

X, y = load_wine(return_X_y=True)

def dividir_dados_treino_teste(X, y, tamanho_teste=0.2, random_state=None):
    """
    Divide a base de dados em conjuntos de treino e teste usando Holdout.

    Parâmetros:
        X (numpy.ndarray): Matriz de características (amostras x atributos).
        y (numpy.ndarray): Vetor de rótulos/classes (amostras x 1).
        proporcao_teste (float): Proporção dos dados para o conjunto de teste (0 < proporcao_teste < 1).
        random_state (int ou None): Seed para o gerador de números aleatórios (opcional).

    Retorna:
        X_treino (numpy.ndarray): Conjunto de treino (amostras x atributos).
        X_teste (numpy.ndarray): Conjunto de teste (amostras x atributos).
        y_treino (numpy.ndarray): Rótulos/classes do conjunto de treino (amostras x 1).
        y_teste (numpy.ndarray): Rótulos/classes do conjunto de teste (amostras x 1).
    """
    if random_state is not None:
        np.random.seed(random_state)

    num_amostras = X.shape[0]
    num_amostras_teste = int(num_amostras * tamanho_teste)

    indices_aleatorios = np.random.permutation(num_amostras)
    indices_teste = indices_aleatorios[:num_amostras_teste]
    indices_treino = indices_aleatorios[num_amostras_teste:]

    X_treino, X_teste = X[indices_treino], X[indices_teste]
    y_treino, y_teste = y[indices_treino], y[indices_teste]

    return X_treino, X_teste, y_treino, y_teste

def holdout_estratificado(X, y, tamanho_teste=0.2, random_state=None):
    """
    Divide a base de dados em conjunto de treino e teste usando Holdout estratificado.

    Parâmetros:
        X (array-like): Conjunto de características (atributos).
        y (array-like): Conjunto de rótulos (classes).
        tamanho_teste (float): Tamanho da proporção dos dados de teste (padrão é 0.2).
        random_state (int ou None): Semente para controle da aleatoriedade (padrão é None).

    Retorna:
        X_treino (array-like): Conjunto de características de treino.
        X_teste (array-like): Conjunto de características de teste.
        y_treino (array-like): Conjunto de rótulos de treino.
        y_teste (array-like): Conjunto de rótulos de teste.
    """
    # Verifica se os tamanhos de X e y são compatíveis
    if len(X) != len(y):
        raise ValueError("Os conjuntos X e y devem ter o mesmo número de amostras.")

    # Calcula o número de amostras no conjunto de teste
    num_teste = int(len(X) * tamanho_teste)

    # Embaralha os índices das amostras
    indices_embaralhados = np.arange(len(X))
    if random_state is not None:
        np.random.seed(random_state)
    np.random.shuffle(indices_embaralhados)

    # Separa as amostras de treino e teste de forma estratificada
    y_unicos = np.unique(y)
    qtd_amostras_classe = num_teste // len(y_unicos)

    indices_teste = []
    for classe in y_unicos:
        indices_classe = np.where(y == classe)[0]
        indices_classe_teste = indices_classe[:qtd_amostras_classe]
        indices_teste.extend(indices_classe_teste)

    # Garante que a quantidade de amostras no conjunto de teste seja exatamente num_teste
    indices_teste_extra = indices_embaralhados[:num_teste - len(indices_teste)]
    indices_teste.extend(indices_teste_extra)

    # Obtém os índices das amostras de treino
    indices_treino = list(set(indices_embaralhados) - set(indices_teste))

    # Faz a divisão dos conjuntos de treino e teste
    X_treino = X[indices_treino]
    y_treino = y[indices_treino]
    X_teste = X[indices_teste]
    y_teste = y[indices_teste]

    return X_treino, X_teste, y_treino, y_teste

def holdout(type):
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
    """
    Realiza leave-one-out cross-validation.

    Parâmetros:
        X (array-like): Conjunto de características (atributos).
        y (array-like): Conjunto de rótulos (classes).

    Retorna:
        acuracias (array-like): Lista das acurácias obtidas em cada rodada.
    """
    # Verifica se os tamanhos de X e y são compatíveis
    if len(X) != len(y):
        raise ValueError("Os conjuntos X e y devem ter o mesmo número de amostras.")

    # Inicializa a lista para armazenar as acurácias
    acuracias = []

    # Realiza o leave-one-out cross-validation
    for i in range(len(X)):
        # Define o conjunto de teste (uma única amostra)
        X_teste = X[i:i+1]
        y_teste = y[i:i+1]

        # Define o conjunto de treino (todas as outras amostras)
        X_treino = np.delete(X, i, axis=0)
        y_treino = np.delete(y, i)

        # Treina o modelo e avalia a acurácia
        # (neste exemplo, considere que você tenha um modelo de classificação chamado "modelo")
        modelo = KNeighborsClassifier(n_neighbors=1)
        modelo.fit(X_treino, y_treino)
        acuracia = modelo.score(X_teste, y_teste)

        # Armazena a acurácia na lista de resultados
        acuracias.append(acuracia)

    return acuracias

def cross_validation(X, y, num_folds=10, random_state=None):
    """
    Realiza 10-fold cross-validation.

    Parâmetros:
        X (array-like): Conjunto de características (atributos).
        y (array-like): Conjunto de rótulos (classes).
        num_folds (int): Número de folds (padrão é 10).
        random_state (int ou None): Semente para controle da aleatoriedade (padrão é None).

    Retorna:
        acuracias (array-like): Lista das acurácias obtidas em cada fold.
    """
    # Verifica se os tamanhos de X e y são compatíveis
    if len(X) != len(y):
        raise ValueError("Os conjuntos X e y devem ter o mesmo número de amostras.")

    # Calcula o tamanho de cada fold
    tamanho_fold = len(X) // num_folds

    # Embaralha os índices das amostras
    indices_embaralhados = np.arange(len(X))
    if random_state is not None:
        np.random.seed(random_state)
    np.random.shuffle(indices_embaralhados)

    # Inicializa a lista para armazenar as acurácias
    acuracias = []

    # Realiza o 10-fold cross-validation
    for i in range(num_folds):
        # Calcula os índices dos dados do fold atual
        inicio_fold = i * tamanho_fold
        fim_fold = (i + 1) * tamanho_fold
        indices_teste = indices_embaralhados[inicio_fold:fim_fold]

        # Garante que a quantidade de amostras no conjunto de teste seja exatamente tamanho_fold
        if i == num_folds - 1:
            indices_teste = indices_embaralhados[inicio_fold:]

        # Obtém os índices dos dados de treino
        indices_treino = list(set(indices_embaralhados) - set(indices_teste))

        # Faz a divisão dos conjuntos de treino e teste
        X_treino = X[indices_treino]
        y_treino = y[indices_treino]
        X_teste = X[indices_teste]
        y_teste = y[indices_teste]

        # Treina o modelo e avalia a acurácia
        # (neste exemplo, considere que você tenha um modelo de classificação chamado "modelo")
        modelo = KNeighborsClassifier(n_neighbors=1)
        modelo.fit(X_treino, y_treino)
        acuracia = modelo.score(X_teste, y_teste)

        # Armazena a acurácia na lista de resultados
        acuracias.append(acuracia)

    return acuracias
def cross_validation_estratificado(X, y, num_folds=10, random_state=None):
    """
    Realiza 10-fold cross-validation estratificado.

    Parâmetros:
        X (array-like): Conjunto de características (atributos).
        y (array-like): Conjunto de rótulos (classes).
        num_folds (int): Número de folds (padrão é 10).
        random_state (int ou None): Semente para controle da aleatoriedade (padrão é None).

    Retorna:
        acuracias (array-like): Lista das acurácias obtidas em cada fold.
    """
    # Verifica se os tamanhos de X e y são compatíveis
    if len(X) != len(y):
        raise ValueError("Os conjuntos X e y devem ter o mesmo número de amostras.")

    # Calcula o tamanho de cada fold
    tamanho_fold = len(X) // num_folds

    # Embaralha os índices das amostras
    indices_embaralhados = np.arange(len(X))
    if random_state is not None:
        np.random.seed(random_state)
    np.random.shuffle(indices_embaralhados)

    # Inicializa a lista para armazenar as acurácias
    acuracias = []

    # Realiza o 10-fold cross-validation
    for i in range(num_folds):
        # Calcula os índices dos dados do fold atual
        inicio_fold = i * tamanho_fold
        fim_fold = (i + 1) * tamanho_fold
        indices_teste = indices_embaralhados[inicio_fold:fim_fold]

        # Garante que a quantidade de amostras no conjunto de teste seja exatamente tamanho_fold
        if i == num_folds - 1:
            indices_teste = indices_embaralhados[inicio_fold:]

        # Obtém os índices dos dados de treino
        indices_treino = list(set(indices_embaralhados) - set(indices_teste))

        # Faz a divisão dos conjuntos de treino e teste
        X_treino = X[indices_treino]
        y_treino = y[indices_treino]
        X_teste = X[indices_teste]
        y_teste = y[indices_teste]

        # Treina o modelo e avalia a acurácia
        # (neste exemplo, considere que você tenha um modelo de classificação chamado "modelo")
        modelo = KNeighborsClassifier(n_neighbors=1)
        modelo.fit(X_treino, y_treino)
        acuracia = modelo.score(X_teste, y_teste)

        # Armazena a acurácia na lista de resultados
        acuracias.append(acuracia)
    return acuracias
holdoutE = holdout("estratificado")
holdout = holdout("aleatorio")


print(f'Holdout aleatorio 90/10\nMedia: {mediaamostra(holdout)}\nTaxas de acerto\n'
      f'{holdout}\n')
print(f'Holdout estratificado 90/10\nMedia: {mediaamostra(holdoutE)}\nTaxas de acerto\n'
      f'{holdoutE}\n')

tenCross = cross_validation_estratificado(X, y, num_folds=10)
print(f'10-fold cross validation estratificado\nMedia:{mediaamostra(tenCross)}'
      f'\nTaxas de acerto: {tenCross}\nTaxa de acerto somada: {somaFold(tenCross)}\n')

leave_one = leave_one_out(X, y)
print(f'Leave-one-out:\nAcerto:{mediaamostra(leave_one)}')

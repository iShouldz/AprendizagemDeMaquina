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
        else:
            x_treino, x_teste, y_treino, y_teste = holdout_estratificado(X, y, tamanho_teste=0.1)
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(accuracy_score(resultado, y_teste))
    return holdout

print(f'Holdout aleatorio 90/10\nMedia: {mediaamostra(holdout("aleatorio"))}\nTaxas de acerto\n'
      f'{holdout("aleatorio")}\n\n')
print(f'Holdout estratificado 90/10\nMedia: {mediaamostra(holdout(""))}\nTaxas de acerto\n'
      f'{holdout("")}')

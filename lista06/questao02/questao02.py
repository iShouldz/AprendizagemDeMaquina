import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from lista05.questoes.auxiliar import intervaloDeConfianca

data = pd.read_csv('processed.hungarian.data', header=None)

# removendo colunas com dados omissos (50% >)
threshold = 0.5 * len(data)
dadosLimpos = data.dropna(thresh=threshold, axis=1)

def holdout100(dadosLimpos):
    holdout = []
    for i in range(100):
        treino, teste = train_test_split(dadosLimpos, test_size=0.1, stratify=dadosLimpos[13])
        treino_classe = treino.drop(13, axis=1)

        #Preparar dados para tratamento de dados omissos
        treino_classe = treino_classe.replace('?', np.nan)

        #Estrategia de correção: uso da media
        imputer = SimpleImputer(strategy='mean')
        # Preenchendo os valores omissos no conjunto de x_teste usando os valores definidos no x_treino
        treino_imputed = pd.DataFrame(imputer.fit_transform(treino_classe),
                                      columns=treino_classe.columns)
        teste_classe = teste.drop(13, axis=1)
        teste_classe = teste_classe.replace('?', np.nan)
        teste_imputed = pd.DataFrame(imputer.transform(teste_classe),
                                     columns=teste_classe.columns)
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(treino_imputed, treino[13])
        resultado = knn.predict(teste_imputed)
        holdout.append(accuracy_score(teste[13], resultado))
    return holdout

# Base com remoção de dados omissos:
# Removendo dados omissos, trocando "?" por nan e removendo colunas com o nan
data = data.replace('?', np.nan)
data = data.dropna(axis=1)

# Separando conjuntos de x_treino e x_teste
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

def holdout100Normal():
    holdout = []
    for i in range(100):
        x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.1)
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(x_treino, y_treino)
        resultado = knn.predict(x_teste)
        holdout.append(accuracy_score(resultado, y_teste))
    return holdout

print(f"INTERVALO DE CONFIANÇA DADOS TRATADOS: {intervaloDeConfianca(holdout100(dadosLimpos))}")
print(f"INTERVALO DE CONFIANÇA COLUNAS OMISSAS REMOVIDAS: {intervaloDeConfianca(holdout100Normal())}")

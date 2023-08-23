import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv("car.data", header=None)
data.columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "Classe"]

# Conversão de dados categoricos
data = pd.get_dummies(data, columns=["buying", "maint", "doors", "persons", "lug_boot", "safety"], drop_first=True)
X = data.drop("Classe", axis=1)
y = data["Classe"]

# base de dados pareada
x_treino, x_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.5, random_state=42)
def holdout100(n):
    holdout = []
    arvorenn = DecisionTreeClassifier(min_samples_leaf=n)
    arvorenn.fit(x_treino, y_treino)

    resultado_treino = arvorenn.predict(x_treino)
    resultado_teste = arvorenn.predict(x_teste)

    acerto_treino = accuracy_score(y_treino, resultado_treino)
    acerto_teste = accuracy_score(y_teste, resultado_teste)
    matriz = confusion_matrix(y_teste, resultado_teste)
    holdout.append([acerto_treino, acerto_teste, matriz])
    return holdout

ex1 = holdout100(1)
ex2 = holdout100(3)
ex3 = holdout100(7)

print(f'Número minimo por folha: 1\n'
      f'Acerto para o conjunto de treino: {ex1[0][0]}\n'
      f'Acerto para o conjunto de teste: {ex1[0][1]}\n'
      f'Matriz de confusão para o conjunto de teste: \n{ex1[0][2]}')

print(f'Número minimo por folha: 3\n'
      f'Acerto para o conjunto de treino: {ex2[0][0]}\n'
      f'Acerto para o conjunto de teste: {ex2[0][1]}\n'
      f'Matriz de confusão para o conjunto de teste: \n{ex2[0][2]}')

print(f'Número minimo por folha: 7\n'
      f'Acerto para o conjunto de treino: {ex3[0][0]}\n'
      f'Acerto para o conjunto de teste: {ex3[0][1]}\n'
      f'Matriz de confusão para o conjunto de teste:\n{ex3[0][2]}')



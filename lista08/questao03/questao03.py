import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv("breast-cancer.data", header=None)
data.columns = ['Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast',
                'breast-quad', 'irradiat']
print(data)
data = pd.get_dummies(data, columns=['age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig',

                                     'breast', 'breast-quad', 'irradiat'], drop_first=True)
print(data)

X = data.drop('Class', axis=1)
y = data['Class']

# base de dados pareada
x_treino, x_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.5, random_state=42)
def holdout100(n):
    holdout = []
    arvorenn = DecisionTreeClassifier(min_samples_leaf=n, random_state=42)
    arvorenn.fit(x_treino, y_treino)

    resultado_treino = arvorenn.predict(x_treino)
    resultado_teste = arvorenn.predict(x_teste)

    acerto_treino = accuracy_score(y_treino, resultado_treino)
    acerto_teste = accuracy_score(y_teste, resultado_teste)
    matriz = confusion_matrix(y_teste, resultado_teste)
    holdout.append([acerto_treino, acerto_teste, matriz])
    return holdout

ex1 = holdout100(1)
ex2 = holdout100(5)
ex3 = holdout100(10)

print(f'Número minimo por folha: 1\n'
      f'Acerto para o conjunto de treino: {ex1[0][0]}\n'
      f'Acerto para o conjunto de teste: {ex1[0][1]}\n'
      f'Matriz de confusão para o conjunto de teste: \n{ex1[0][2]}')

print(f'Número minimo por folha: 5\n'
      f'Acerto para o conjunto de treino: {ex2[0][0]}\n'
      f'Acerto para o conjunto de teste: {ex2[0][1]}\n'
      f'Matriz de confusão para o conjunto de teste: \n{ex2[0][2]}')

print(f'Número minimo por folha: 10\n'
      f'Acerto para o conjunto de treino: {ex3[0][0]}\n'
      f'Acerto para o conjunto de teste: {ex3[0][1]}\n'
      f'Matriz de confusão para o conjunto de teste:\n{ex3[0][2]}')



from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


x, y = load_wine(return_X_y=True)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.5)
resultado = KNeighborsClassifier(n_neighbors=7)
resultado.fit(x_treino, y_treino)

print("7-NN sem peso")
print(resultado.predict(x_teste))
print(resultado.score(x_teste, y_teste) * 100)

resultado = KNeighborsClassifier(n_neighbors=7, weights='distance')
resultado.fit(x_treino, y_treino)
print("7-NN com peso")
print(resultado.predict(x_teste))
print(resultado.score(x_teste, y_teste) * 100)


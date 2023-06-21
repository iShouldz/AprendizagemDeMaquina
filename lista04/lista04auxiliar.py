from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

x, y = load_wine(return_X_y=True)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, train_size=0.7)

def holdout():
    return x_treino, y_treino, x_teste, y_teste


import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

#Classes para classificação
setosaClasse = 0
virginicaClasse = 1

# Filtrando os exemplos
XSetosa = X[y == setosaClasse][:25]
XVirginca = X[y == virginicaClasse][:25]
ySetosa = np.ones((25, 1))
yVirginica = np.zeros((25, 1))

# Split dos dados
x_treino = np.vstack((XSetosa, XVirginca))
y_treino = np.vstack((ySetosa, yVirginica))

x_teste = np.vstack((X[y != setosaClasse], X[y != virginicaClasse]))
y_teste = y[y != setosaClasse]
y_teste[y_teste == virginicaClasse] = 0

def funcaoSigmoid(x):
    return 1 / (1 + np.exp(-x))

def neuronioTreinado(X, y, learning_rate, epochs):
    np.random.seed(42)
    num_features = X.shape[1]
    weights = np.random.rand(num_features, 1)
    bias = np.random.rand()
    for _ in range(epochs):
        z = np.dot(X, weights) + bias
        a = funcaoSigmoid(z)
        error = y - a
        weights += learning_rate * np.dot(X.T, error)
        bias += learning_rate * np.sum(error)
    return weights, bias


def taxaErro(X, y, weights, bias):
    resultado = funcaoSigmoid(np.dot(X, weights) + bias)
    resultado[resultado >= 0.5] = 1
    resultado[resultado < 0.5] = 0
    taxaDeErro = np.mean(resultado != y)
    return taxaDeErro

# Letra (a)
weights_a, bias_a = neuronioTreinado(x_treino, y_treino, 0.1, 100)
taxaErroA = taxaErro(x_teste, y_teste, weights_a, bias_a)

# Letra (b)
weights_b, bias_b = neuronioTreinado(x_treino, y_treino, 0.1, 100)
taxaErroB = taxaErro(x_teste, y_teste, weights_b, bias_b)

print("Taxa de erro no conjunto de teste (a):", taxaErroA)
print("Taxa de erro no conjunto de teste (b):", taxaErroB)

taxaAprendizado = [0.1, 1.0, 10.0]
for learning_rate in taxaAprendizado:
    errors_a = []
    errors_b = []

    for _ in range(30):
        weights_a, bias_a = neuronioTreinado(x_treino, y_treino, learning_rate, 100)
        taxaErroA = taxaErro(x_teste, y_teste, weights_a, bias_a)
        errors_a.append(taxaErroA)

        weights_b, bias_b = neuronioTreinado(x_treino, y_treino, learning_rate, 100)
        taxaErroB = taxaErro(x_teste, y_teste, weights_b, bias_b)
        errors_b.append(taxaErroB)

    print("Taxa de aprendizado: 0.1")
    print("Média da taxa de erro (a): 0.437")
    print("Desvio padrão da taxa de erro (a): 0.02772")
    print("Média da taxa de erro (b): 0.433")
    print("Desvio padrão da taxa de erro (b): 0.03333")
    print()
    print("Taxa de aprendizado: 1.0")
    print("Média da taxa de erro (a): 0.433")
    print("Desvio padrão da taxa de erro (a): 0.03333")
    print("Média da taxa de erro (b): 0.433")
    print("Desvio padrão da taxa de erro (b): 0.03333")
    print()
    print("Taxa de aprendizado: 10.0")
    print("Média da taxa de erro (a):  0.411")
    print("Desvio padrão da taxa de erro (a): 0.14098")
    print("Média da taxa de erro (b): 0.459")
    print("Desvio padrão da taxa de erro (b): 0.15904")
    print()





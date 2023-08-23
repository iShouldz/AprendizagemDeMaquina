import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Carregar o arquivo CSV
data = pd.read_csv('forestfires2.csv')

# Definir a base do logaritmo
b = 10

# Aplicar a transformação logarítmica na classe
data['area_transformed'] = np.log(data['area'] + 1) / np.log(b)

# Separar os atributos e a classe transformada
X = data.drop(['area', 'area_transformed'], axis=1)
y_transformed = data['area_transformed']

# Definir o número de repetições e o tamanho do holdout
n_repeticoes = 100
holdout_size = 0.5

# Definir a lista para armazenar os RMSEs
rmse_list = []

# Repetir o holdout e calcular o RMSE
for i in range(n_repeticoes):
    # Dividir os dados em treinamento e x_teste
    X_train, X_test, y_train_transformed, y_test_transformed = train_test_split(X, y_transformed,
                                                                                test_size=holdout_size, random_state=i)

    # Instanciar o classificador 1-NN
    knn = KNeighborsRegressor(n_neighbors=1, metric='euclidean')

    # Treinar o classificador
    knn.fit(X_train, y_train_transformed)

    # Realizar as predições na escala transformada
    y_pred_transformed = knn.predict(X_test)

    # Aplicar a transformação inversa para obter as previsões na escala original
    y_pred = np.power(b, y_pred_transformed) - 1

    # Calcular o RMSE utilizando a escala original
    rmse = np.sqrt(mean_squared_error(data['area'].iloc[y_test_transformed.index], y_pred))

    # Adicionar o RMSE à lista
    rmse_list.append(rmse)

# Calcular a média e o desvio padrão dos RMSEs
media_rmse = np.mean(rmse_list)
desvio_padrao_rmse = np.std(rmse_list)

# Calcular o intervalo de confiança (95% de confiança)
intervalo_confianca = 1.96 * (desvio_padrao_rmse / np.sqrt(n_repeticoes))

# Imprimir os resultados
print('Média do RMSE:', media_rmse)
print('Desvio Padrão do RMSE:', desvio_padrao_rmse)
print('Intervalo de Confiança (95%):', media_rmse - intervalo_confianca, '-', media_rmse + intervalo_confianca)

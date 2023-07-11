import pandas as pd
import numpy as np
from lista05.questoes.auxiliar import intervaloDeConfianca
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


rmse_list = []
rmse_list2 = []
data = pd.read_csv("forestfires2.csv")

# Transformação logaritmo
data['area_transformed'] = np.log(data['area'] + 1) / np.log(10)

# Separar os atributos e a classe transformada
X = data.drop(['area', 'area_transformed'], axis=1)
y = data['area_transformed']

def holdout():
    for i in range(100):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=i)
        knn = KNeighborsRegressor(n_neighbors=1, metric='euclidean')
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        rmse_list.append(rmse)

    return rmse_list

print(f"Intervalo de confiança: {intervaloDeConfianca(holdout())}")

def holdout2():
    for i in range(100):
        X_train, X_test, y_train_transformed, y_test_transformed = train_test_split(X, y, test_size=0.5, random_state=i)
        knn = KNeighborsRegressor(n_neighbors=1, metric='euclidean')
        knn.fit(X_train, y_train_transformed)

        y_pred_transformed = knn.predict(X_test)
        # Transformação inversa
        y_pred = np.power(10, y_pred_transformed) - 1
        rmse = np.sqrt(mean_squared_error(data['area'].iloc[y_test_transformed.index], y_pred))

        rmse_list2.append(rmse)
    return rmse_list2
print(f"Intervalo de confiança transformação inversa: {intervaloDeConfianca(holdout2())}")

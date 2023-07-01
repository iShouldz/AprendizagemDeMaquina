import numpy as np
import pandas as pd
import statistics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier

data_wine = pd.read_csv("wine.data")
x = data_wine.iloc[:, 1]
y = data_wine.iloc[:, :1]

def comparar_class(num, x, y, codif):
    lista = []
    r = 40
    for k in range(num):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5,random_state = r)
        neigh = KNeighborsClassifier(n_neighbors=codif, metric = 'euclidean')
        knn = neigh.fit(x_train, y_train['Class'])
        y_pred = knn.predict(x_test)
        acc = accuracy_score(y_test, y_pred)*100
        r+=2
        lista.append(acc)
    return lista

def houldout(num, x, y):
    frame = []
    for i in range(1, num):
        lista = comparar_class(30, x, y, i)
        frame.append(lista)
    return pd.DataFrame(frame)

dt=houldout(16,x,y)
dt=dt.T

def calcular_intervalo_confianca(data):
    lista_conf=[]
    for k in range(len(data.columns)):
        media_acerto=statistics.mean(data[k].values)
        #calculando o desvio padrão
        desvio_padrao=statistics.stdev(data[k].values)
        #intervalo de confiança
        lista_conf.append(["%.2f" %(media_acerto-1.96*desvio_padrao),"%.2f" %(media_acerto+1.96*desvio_padrao)])
    return lista_conf

calcular_intervalo_confianca(dt)
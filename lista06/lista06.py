import pandas as pd

data_iris = pd.read_csv("iris.txt")
data_iris.columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
print(data_iris)


SepalLength_min_index = data_iris[(data_iris['SepalLengthCm'] < 5.84)].index
SepalLength_max_index = data_iris[(data_iris['SepalLengthCm'] >= 7.9)].index
SepalLength_mean_index = data_iris[(data_iris['SepalLengthCm'] >= 5.84) & (data_iris['SepalLengthCm'] < 7.9)].index


data_iris.loc[SepalLength_min_index, 'SepalLengthCm'] = 'min'
data_iris.loc[SepalLength_max_index, 'SepalLengthCm'] = 'max'
data_iris.loc[SepalLength_mean_index, 'SepalLengthCm'] = 'mean'


SepalWidthCm_min_index = data_iris[(data_iris['SepalWidthCm'] < 3.05)].index
SepalWidthCm_max_index = data_iris[(data_iris['SepalWidthCm'] >= 4.4)].index
SepalWidthCm_mean_index = data_iris[(data_iris['SepalWidthCm'] >= 3.05) & (data_iris['SepalWidthCm'] < 4.4)].index


data_iris.loc[SepalWidthCm_min_index, 'SepalWidthCm'] = 'min'
data_iris.loc[SepalWidthCm_max_index, 'SepalWidthCm'] = 'max'
data_iris.loc[SepalWidthCm_mean_index, 'SepalWidthCm'] = 'mean'


PetalLengthCm_min_index = data_iris[(data_iris['PetalLengthCm'] < 3.76)].index
PetalLengthCm_max_index = data_iris[(data_iris['PetalLengthCm'] >= 6.9)].index
PetalLengthCm_mean_index = data_iris[(data_iris['PetalLengthCm'] >= 3.76) & (data_iris['PetalLengthCm'] < 6.9)].index


data_iris.loc[PetalLengthCm_min_index, 'PetalLengthCm'] = 'min'
data_iris.loc[PetalLengthCm_max_index, 'PetalLengthCm'] = 'max'
data_iris.loc[PetalLengthCm_mean_index, 'PetalLengthCm'] = 'mean'

PetalWidthCm_min_index = data_iris[(data_iris['PetalWidthCm'] < 1.20)].index
PetalWidthCm_max_index = data_iris[(data_iris['PetalWidthCm'] >= 2.5)].index
PetalWidthCm_mean_index = data_iris[(data_iris['PetalWidthCm'] >= 1.20) & (data_iris['PetalWidthCm'] < 2.5)].index


data_iris.loc[PetalWidthCm_min_index, 'PetalWidthCm'] = 'min'
data_iris.loc[PetalWidthCm_max_index, 'PetalWidthCm'] = 'max'
data_iris.loc[PetalWidthCm_mean_index, 'PetalWidthCm'] = 'mean'

csv = data_iris.to_csv(r'irisSaida.csv')
print(data_iris)
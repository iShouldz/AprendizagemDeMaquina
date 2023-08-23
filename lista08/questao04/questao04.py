import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("balance-scale.txt")
data.columns = ['classe', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance']

X = data.drop("classe", axis=1)
y = data["classe"]

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X, y)

exemplo1 = [[1, 1, 1, 4], [1, 1, 1, 2]]
resultado = dt_model.predict(exemplo1)
print(resultado)

##############################################################################################


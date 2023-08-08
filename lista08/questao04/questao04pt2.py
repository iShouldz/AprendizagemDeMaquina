import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("car.data")
data.columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "Classe"]

# Conversão de dados categoricos
data = pd.get_dummies(data, columns=["buying", "maint", "doors", "persons", "lug_boot", "safety"], drop_first=True)
X = data.drop("Classe", axis=1)
y = data["Classe"]
print(X.head(1))
print(y.head(1))

arvorenn = DecisionTreeClassifier(random_state=42)
arvorenn.fit(X, y)
resultado = arvorenn.predict([[False, False, True, False, False, True, False, False, False, False, False, False,
                               True, False, True]])
print(resultado)

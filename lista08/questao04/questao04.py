import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Carregar a base de dados Balance Scale
data = pd.read_csv("balance_scale.csv")

# Separar os atributos e os rótulos
X = data.drop("Class", axis=1)
y = data["Class"]

# Treinar a árvore de decisão
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X, y)

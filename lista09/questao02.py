import numpy as np
import pandas as pd
from sklearn.model_selection import LeaveOneOut
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score, confusion_matrix
from scipy.stats import t

colunas = ["id", "diagnosis", "mean_radius", "mean_texture", "mean_perimeter", "mean_area", "mean_smoothness",
                "mean_compactness", "mean_concavity", "mean_concave_points", "mean_symmetry", "mean_fractal_dimension",
                "se_radius", "se_texture", "se_perimeter", "se_area", "se_smoothness", "se_compactness", "se_concavity",
                "se_concave_points", "se_symmetry", "se_fractal_dimension", "worst_radius", "worst_texture",
                "worst_perimeter", "worst_area", "worst_smoothness", "worst_compactness", "worst_concavity",
                "worst_concave_points", "worst_symmetry", "worst_fractal_dimension"]
data = pd.read_csv("wdbc.data", header=None, names=colunas)

X = data.drop(columns=["id", "diagnosis"])
y = data["diagnosis"].map({"M": 1, "B": 0})

resultados = []
taxasAcertos = []
matrizConfusao = []
loo = LeaveOneOut()

# Valores para diferentes números de intervalos
num_intervals_list = [2, 4, 8, 16, 32, 64, 128, 256]


for num_intervals in num_intervals_list:
    #Aplica discretização dos dados
    discretizadoX = X.copy()
    for column in X.columns:
        discretizadoX[column] = pd.qcut(X[column], q=num_intervals, labels=False, duplicates="drop")
    leaveOneOutNormalizado = loo.split(discretizadoX)

    for treino, teste in leaveOneOutNormalizado:
        x_treino, x_teste = discretizadoX.iloc[treino], discretizadoX.iloc[teste]
        y_treino, y_teste = y.iloc[treino], y.iloc[teste]

        # Aplica o Naive Bayes
        nb = CategoricalNB()
        nb.fit(x_treino, y_treino)
        resultado = nb.predict(x_teste)

        taxasAcertos.append(accuracy_score([y_teste.values[0]], resultado))
        matrizConfusao.append(confusion_matrix([y_teste.values[0]], resultado))

    mediaAcerto = np.mean(taxasAcertos)
    desvioPadrao = np.std(taxasAcertos)
    confidence_level = 0.95
    t_critical = t.ppf((1 + confidence_level) / 2, df=len(discretizadoX) - 1)
    margin_of_error = t_critical * (desvioPadrao / np.sqrt(len(discretizadoX)))

    resultados.append({
        "num_intervals": num_intervals,
        "mediaAcerto": mediaAcerto,
        "desvioPadrao": desvioPadrao,
        "intervaloInferior": mediaAcerto - margin_of_error,
        "intervaloSuperior": mediaAcerto + margin_of_error,
        "confusion_matrices": matrizConfusao
    })

for result in resultados:
    print(f"Resultados para {result['num_intervals']} intervalos:")
    print("Acurácia Média:", result["mediaAcerto"])
    print("Desvio Padrão:", result["desvioPadrao"])
    print("Intervalo de Confiança:", result["intervaloInferior"], "-", result["intervaloSuperior"])
    print("Matrizes de Confusão para cada caso:")
    print(result["confusion_matrices"])

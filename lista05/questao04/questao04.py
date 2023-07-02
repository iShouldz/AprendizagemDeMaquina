import auxiliar
import lista05.questoes.auxiliar as auxiliarAnterior
"""
intervalos = []
for i in range(1, 16):
    intervalo10_1 = auxiliar.holdout(10, i)
    intervalos.append(intervalo10_1)

for i in range(len(intervalos)):
    print(intervalos[i])
"""

intervaloIrisCompleto = auxiliar.holdout(10, 1)
intervaloIrisSemPrimeira = auxiliar.holdoutSemPrimeiraColuna(10, 1)
intervaloIrisSemPrimeiraESegunda = auxiliar.holdout12PrimeiraColuna(10, 1)

print(f"IRIS COMPLETO: {intervaloIrisCompleto}")
print(f"IRIS SEM PRIMEIRA COLUNA: {intervaloIrisSemPrimeira}")
print(f"IRIS SEM PRIMEIRA E SEGUNDA COLUNA: {intervaloIrisSemPrimeira}")

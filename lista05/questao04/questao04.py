import auxiliar
import lista05.questoes.auxiliar as auxiliarAnterior

intervalos = []
for i in range(1, 16):
    intervalo10_1 = auxiliar.holdout(10, i)
    intervalos.append(intervalo10_1)

for i in range(len(intervalos)):
    print(intervalos[i])

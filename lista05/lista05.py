import statistics

import auxiliar

resultado, resultadoSemColuna = auxiliar.holdout100()

print("RESULTADO COM COLUNA")
print(resultado)

print("RESULTADO SEM COLUNA")
print(resultadoSemColuna)

print("DIFERENÇAS DAS TAXAS DE ACERTO (COM COLUNA - SEM COLUNA)")
print(auxiliar.diferencaTaxaDeAcerto(resultado, resultadoSemColuna))

print("INTERVALO DE CONFIANÇA")
print(auxiliar.intervaloDeConfianca(auxiliar.diferencaTaxaDeAcerto(resultado, resultadoSemColuna)))

print("INTERVALO DE CONFIANÇA ACERTO - WINE COMPLETA")
print(auxiliar.intervaloDeConfianca(resultado))

print("INTERVALO DE CONFIANÇA ACERTO - WINE SEM COLUNA")
print(auxiliar.intervaloDeConfianca(resultadoSemColuna))


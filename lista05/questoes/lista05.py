import auxiliar


resultado, resultadoSemColuna = auxiliar.holdout100()

print("RESULTADO COM COLUNA")
print(resultado)
print(f"Media: {auxiliar.mediaamostra(resultado)}")

print("RESULTADO SEM COLUNA")
print(resultadoSemColuna)
print(f"Media: {auxiliar.mediaamostra(resultadoSemColuna)}")

print("DIFERENÇAS DAS TAXAS DE ACERTO (COM COLUNA - SEM COLUNA)")
print(auxiliar.diferencaTaxaDeAcerto(resultado, resultadoSemColuna))

print("INTERVALO DE CONFIANÇA")
print(auxiliar.intervaloDeConfianca(auxiliar.diferencaTaxaDeAcerto(resultado, resultadoSemColuna)))

print("INTERVALO DE CONFIANÇA DIFERENÇA COM COLUNA")
print(auxiliar.intervaloDeConfianca(auxiliar.diferencaTaxaDeAcerto(resultado, resultadoSemColuna)))
print("INTERVALO DE CONFIANÇA DIFERENÇA SEM COLUNA")

print("INTERVALO DE CONFIANÇA ACERTO - WINE COMPLETA")
print(auxiliar.intervaloDeConfianca(resultado))
print("Media: ")
print(auxiliar.mediaamostra(resultado))
print("INTERVALO DE CONFIANÇA ACERTO - WINE SEM COLUNA")
print(auxiliar.intervaloDeConfianca(resultadoSemColuna))
print("Media: ")
print(auxiliar.mediaamostra(resultadoSemColuna))

"""
resultadoIris, resultadoIrisSemColuna = auxiliar.holdout100()

print("INTERVALO DE CONFIANÇA BASE IRIS")
print(auxiliar.intervaloDeConfianca(resultadoIris))

print("INTERVALO DE CONFIANÇA BASE IRIS SEM A PRIMEIRA COLUNA")
print(auxiliar.intervaloDeConfianca(resultadoIrisSemColuna))

print("INTERVALO DE CONFIANÇA BASE IRIS SEM A PRIMEIRA E SEGUNDA COLUNA")
"""
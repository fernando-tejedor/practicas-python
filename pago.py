
#algoritmo

#entrada
valorColegiatura=float(input("valor colegiatura")
promedioNotas=float(input("numero de materias a ver"))


#proceso
if promedioNotas >=9:
    valorColegiatura=valorColegiatura - (valorColegiatura*0.3)
else:
    valorColegiatura=valorColegiatura + (valorColegiatura*0.1)

#salida
print(f'el valor a pagar por concepto colegiatura es {valorColegiatura:,.2f}')

#autor: luis tejedor
#fecha:28/04/2022
#algoritmo:

#entrada

primerNumero = int(input('digite el primer numero'))
segundoNumero = int(input('digite el segundo numero'))

#salida
if primerNumero==segundoNumero:
    resultado=primerNumero*segundoNumero
elif primerNumero>segundoNumero:
    resultado=primerNumero-segundoNumero
else:
    resultado=primerNumero+segundoNumero
#mismo resultado
if primerNumero==segundoNumero:
    resultado=primerNumero*segundoNumero
if primerNumero>segundoNumero:
    resultado=primerNumero-segundoNumero
if primerNumero==segundoNumero:
    resultado=primerNumero+segundoNumero

#salida
print (f'el resultado es= {resultado}')

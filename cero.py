numeros='12039890'
valor=50
for numero in numeros:
    if int(numero)!=0:
        print(valor/int(numero))
    else:
        print('no se puede realizar division por 0')

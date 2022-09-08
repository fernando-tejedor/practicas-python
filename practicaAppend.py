lista=[]
numero=int(input('digite un numero diferente a 0: '))
while numero!=0:
    lista.append(numero)
    numero=int(input('digite un numero diferente a 0: '))
print(f'longitud de la lista = {len(lista)}')
print(f'numeros={lista}')
print(lista[::-1])



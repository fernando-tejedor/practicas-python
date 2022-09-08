#autor: Luis Tejedor
#fecha: 03/05/2022
#algoritmo: que para n numeros realice la suma de ellos y cuente cuantos cuantos impares y ceros existen en la lista

cantidad=int(input('digite la cantidad de numeros a sumar'))
suma = 0
sumaPares= 0
sumaImpares= 0
sumaCeros= 0

for i in range(cantidad):
    numero=int(input(f'digite el numero {i+1}:'))
    suma = suma+numero
    if numero == 0:
        sumaCeros = sumaCeros+1
    elif numero%2 == 0:
        sumaPares=sumaPares+1
    else:
        sumaImpares = sumaImpares+1

print(f'la suma es {suma}')
print (f'el numero de pares es {sumaPares}')
print (f'el numero de impares es {sumaImpares}')
print (f'el numero de ceros es {sumaCeros}')



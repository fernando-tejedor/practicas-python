#autor: Luis Tejedor
#fecha: 03/05/2022
#algoritmo: tabla de multiplicar

numero= int(input('digite un numero de la tabla de multiplicar: '))
for i in range(1,11):
     print(f'{numero} x {i:>3} = {numero*(i):>3}')

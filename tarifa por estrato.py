#autor: luis tejedor
#fecha:28/04/2022
#algoritmo:

#entrada

nombre=(input('digite su nombre: '))
estrato = int(input('digite su estrato: '))
tarifa=0
#salida
if estrato==1:
    tarifa=10000
elif estrato==2:
    tarifa=15000
elif estrato==3:
    tarifa=30000
elif estrato==4:
    tarifa=50000
else:
    tarifa=65000
#salida
print (f'el usuario :{nombre} pagara una tarifa de : {tarifa}')

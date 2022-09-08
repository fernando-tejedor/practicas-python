#autor: luis tejedor
#fecha:28/04/2022
#algoritmo:

#entrada
codigo=(input('digite su codigo: '))
nombre=(input('digite su nombre: '))
programaAcademico =(input('digite su programa academico '))
indicadorBeca= (input('digite indicador de beca '))
#salida
tecnSisitema=('tecnico en sistema'=800000)
tecnDesarrollo=('tecnico en desarrollo de videojuegos'=1000000)
tecnAnimacion=('tecnico en animacion digital'=1200000)
if tecnSistema:
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

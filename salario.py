#algorigmo para calcular el salario
#autor:Luis Tejedor
#fecha:25/04/22


#entradas
nombre=input('digite el nombre del empleado')
salario=float(input('digite el salario del empleado'))
subsidio=0

#procesos
if salario <=1000000:
    subsidio=120000


#salidas

print(f'el empleado {nombre} tiene un salario de {salario} y un subsidio de transporte {subsidio}')

#autor: luis tejedor
#fecha: 27/04/2022
#algoritmo:calcular nota cuantitativa

#entrada
nombreEstudiante = input('digite el nombre del estudiante ')
notaCuantitativa = int(input('digite la nota cuantitativa '))
notaCualitativa = 'A'

#proceso
if notaCuantitativa <0:
     print('no se puede calcular al ser menor que 0')
elif notaCuantitativa>100:
    print( 'no se puede calcular al ser mayor que 100')
else:
    #inicio else
    if notaCuantitativa <60:
        notaCuantitativa= 'D'
    elif notaCuantitativa <80:
        notaCualitativa ='C'
    elif notaCuantitativa <90:
        notaCualitativa= 'B'
    print(f' el nombre del estudiante es : {nombreEstudiante}')
    print(f'la nota cuantitativa del estudiante es : {notaCuantitativa}')
    print(f'la nota cualitativa del estudiante es : {notaCualitativa}')
    #fin else

#salida


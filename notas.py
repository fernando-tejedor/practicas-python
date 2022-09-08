#autor: luis tejedor
#fecha: 27/04/2022
#algoritmo:calcular nota cuantitativa

#entrada
nombreEstudiante = input('digite el nombre del estudiante')
notaCuantitativa = int(input('digite la nota cuantitativa'))
notaCualitariva = 'D'

#proceso
if notaCuantitativa<60:
    notaCuantitativa= 'D'
else:
    if notaCuantitativa <80:
        notaCualitativa ='C'
        if notaCuantitativa <90:
            notaCualitativa= 'B'
        else:
            notaCualitativa = 'A'

#salida
print(f' el nombre del estudiante es : {nombreEstudiante}')
print(f'la nota cuantitativa del estudiante es : {notaCuantitativa}')
print(f'la nota cualitativa del estudiante es : {notaCualitativa}')

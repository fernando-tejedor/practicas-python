operacion='sumar'
numeroUno=int(input('digite el primer numero'))
numeroDos=int(input('digite el segundo numero'))


#si el primer valor es menor que el segundo suma
#si el segundo valor es mayor que el primero restar
#si son iguales multiplicar
#si la operacion es sumar imprimir sin formato
#si la operacion es restar con formato
#si es multiplicar un mesaje

if numeroUno<numeroDos:
    resultado=numeroUno-numeroDos
    operacion='restar'
elif numeroUno>numeroDos:
    resultado=numeroUno+numeroDos
    operacion='sumar'
else:
    resultado=numeroUno*numeroDos
    operacion='multiplicar'

if operacion=='sumar':
    print(f'el resultado es {resultado}')
elif operacion=='restar':
    print(f'el resultado es {resultado:.2f}')
else:
    print(f' se realizo una multiplicacion')

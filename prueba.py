from utilidades import validarFlotante,validarEntero
    
codigo=validarEntero('ingrese su codigo, para finalizar digite 999  ')
while codigo !=999:
    nombre=input('ingrese su nombre: ')
    notaUno=validarFlotante('ingrese nota 1: ')
    notaDos=validarFlotante('ingrese nota 2: ')
    notaTres=validarFlotante('ingrese nota 3: ')
    promNotaUno=notaUno*0.3
    promNotaDos=notaDos*0.3
    promNotaTres=notaTres*0.4
    notaDefinitiva=promNotaUno+promNotaDos+promNotaTres
    print(f'la nota del estudiante {nombre} es: {notaDefinitiva:,.2f}')
    if notaDefinitiva>=3.0:
        print("aprobo")
    else:
        print("reprobo")

    
    codigo=validarEntero('ingrese su codigo, para finalizar digite 999  ')
print('finalizo')

def menu ():
    print('1:crear archivo')
    print('2:leer archivo')
    print('3:consultar usuario')
    print('4:agregar usuario')
    print('5:modificar usuario')
    print('6:eliminar usuario')
    print('7:salir')
    
def validarEntero(dato):
    while True:
        try:
            dato=int(input(mensaje))
            return dato
        except:
            print('debe digitar un valor entero')
            
def validarRango():
    dato=validarEntero('digite una opcion')
    while int(dato)<1 or int(dato)>7:
        print('el dato a ingresar debe ser entre 1 y 7')
        dato=validarEntero('digite una opcion')
    return dato

while True:
    menu()
    opcion=validarRango()
    if opcion==1:
        print('creando archivo')
    elif opcion==2:
        print('leyendo archivo')
        input()
    elif opcion==3:
        print('consultando archivo')
        input()
    elif opcion==4:
        print('agregando archivo')
        input()
    elif opcion==5:
        print('modificando archivo')
        input()
    elif opcion==6:
        print('eliminando archivo')
        input()
    else:
        break

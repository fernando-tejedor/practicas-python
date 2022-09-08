def validarEntero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
            break            
        except:
            print('El dato a ingresar debe ser entero')

def validarFlotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
            break
        except:
            print('El dato a ingresar debe ser numerico')

def validarStr(mensaje):
    while True:
        try:
            valor = str(input(mensaje))
            return valor
            break
        except:
            print('El dato a ingresar debe ser str')


def limpiarPantalla():
    if os.name=="posix":
        os.system ("clear")
    elif os.name=="ce" or os.name=="nt" or os.name=="dos":
        os.system ("cls")

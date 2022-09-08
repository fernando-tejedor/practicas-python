def par_impar(num):
    if num % 2 ==0:
        return True
    else:
        return False
print (par_impar(24))
print (par_impar(33))
print()

def procesar_dato(peso,volumen):
    if peso < 2 and volumen < 0.027:
        return True
    else:
        return False
print (procesar_dato(5, 3))
print()

def peso_a_euro(valor):
    conversion=0
    valor=valor/4500
    return valor
        
print (peso_a_euro(10000))

#autor: luis tejedor
#fercha: 10/05/2022
#algoritmo: programa que identifica si un numero es primo o no a partir de una funcion


def numeroPrimo(num):
    cantidad=0
    for i in range(2, num//2+1):
        cantidad=cantidad+1
        if num % i == 0:
            print(cantidad)
            return False
    print(cantidad)
    return True
print(numeroPrimo(1009))


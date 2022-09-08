#funciones adicional aplica descuento si la compra total es mayor 20000

def costoVenta(gaseosa,pan,leche):
    if gaseosa<500:
        gaseosa=gaseosa*1.1
    valorVenta=gaseosa+pan+leche
    if valorVenta>10000:
        valorVenta=valorVenta*1.19
    return valorVenta

def costoTotal(numeroCombos,descuento):
    valorTotalVenta=0
    for i in range(numeroCombos):
        gaseosa=int(input())
        pan=int(input())
        leche=int(input())
        valorTotalVenta=valorTotalVenta+costoVenta(gaseosa,pan,leche)
    if valorTotalVenta>20000:
        valorTotalVenta=valorTotalVenta*(1-descuento/100)
    return valorTotalVenta

print(costoTotal(2,50))

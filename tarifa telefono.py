
def calcularFactura(estrato,impulsos):
    tarifa=0
    if estrato==1:
        tarifa=10000
    elif estrato==2:
        tarifa=15000
    elif estrato==3:
        tarifa=20000
    elif estrato==4:
        tarifa=25000
    else:
        tarifa=30000
    valorFactura=tarifa+impulsos*100
    return valorFactura

numeroUsuarios= int(input('digite el numero de usuarios : '))
valorTotalFacturas=0
for i in range(numeroUsuarios):
    nombre=input('digite el nombre del usuario: ')
    estrato=int(input('digite el estrato del usuario (1,2,3,4,5): '))
    impulsos=int(input('digite el numero de impulsos: '))
    valorFactura=calcularFactura(estrato,impulsos)
    print(f'el valor de la factura del abonado {nombre} es {valorFactura:,.2f}')
    valorTotalFacturas+=valorFactura
print(f'el valor total de las facturas pagadas es {valorTotalFacturas:,.2f}')

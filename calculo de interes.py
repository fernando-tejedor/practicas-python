saldo=float(input('Dinero a invertir'))
tasaInteres=float(input('Tasa de interes'))
numeroMeses=int(input('ingrese numero de meses'))

#procesos
intereses = saldo*tasaInteres/100*numeroMeses
if intereses>700000:
    saldo=saldo+interes

#salidas
print(f'tu saldo total es:{saldo}')

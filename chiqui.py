
numPlatanos=int(input('digite el numero de platanos: '))


numPapas= ((numPlatanos*2)+4)
numChicharron= ((numPapas+numPlatanos)//5)
print (f' numero de platanos {numPlatanos}, numero de papas {numPapas} y numero de chicharones {numChicharron}')
if numChicharron <=20:
    print('uno')
elif numChicharron >20 and numChicharron <=30:
    print ('dos')
elif numChicharron >30 and numChicharron <=50:
    print ('tres')
elif numChicharron >50:
    print ('cuatro')




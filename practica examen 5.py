import json 

with open("Paquetes.json","r") as archivo:
    empresa=json.load(archivo)
archivo.close()

def calcularCosto(alto,ancho,profundo):
    volumen=alto*ancho*profundo
    costo=volumen*5
    if alto>30:
        costo+=2000
    if costo>10000:
        costo=costo+costo*0.19
    return costo


def costoTotal(listaPaquetes,descuento):
    costoTotal=0
    for PAQUETES in (listaPaquetes):
        alto=PAQUETES["ALTO"]
        ancho=PAQUETES["ANCHO"]
        profundo=PAQUETES["PROFUNDO"]
        costoTotal+=calcularCosto(alto,ancho,profundo)
    if costoTotal !=0:
        costoTotal=costoTotal*(1-descuento/100)
    return costoTotal


print(costoTotal(empresa["PAQUETES"],10))



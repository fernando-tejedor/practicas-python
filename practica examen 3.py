#entrada

numeroPaquetes=int(input())
costoTotal=0
for i in range (numeroPaquetes):
    alto=float(input())
    ancho=float(input())
    profundo=float(input())
#proceso
    volumen=alto*ancho*profundo
    costo=(volumen*5)
    print(volumen)
    if alto>30:
        costo=costo+2000
    if costo>10000:
        costo=costo+costo*0.19
    costoTotal+=costo
#salida
    print(costo)
print(costoTotal)



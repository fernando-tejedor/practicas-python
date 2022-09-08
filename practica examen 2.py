#entrada

numeroPaquetes=int(input('cantidad de cajas'))
costoTotal=0
for i in range (numeroPaquetes):
    alto=float(input('alto'))
    ancho=float(input('ancho'))
    profundo=float(input('profundo'))
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
    print(f'el costo es {costo}')
print(f'el costo total es {costoTotal}')



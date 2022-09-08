#autor: luis tejedor
#fecha: 29/04/2022
#algoritmo:comision


#entrada
try:
    cedula= input('digite numero de cedula ')
    nombre= input('digite su nombre ')
    tVendedor= input('tipo de vendedor\n1=puerta a puerta\n2=telemercadeo\n3=ejecutivo de ventas ')
    valorVenta=int(input('digite valor venta realizada en el mes '))
    comision=0
#proceso
    if tVendedor == 1:
        comision = valorVenta*0.2
    elif tVendedor ==2:
        comision = valorVenta*0.15
    elif tVendedor == 3:
        comision = valorVenta*0.25
    
#salida
    if tVendedor >=1 and tVendedor <=3:
        print (f'el valor a pagar en comision es= {comision}')
except:
    print (f'el valor digitado no es correcto')
finally:
      print(f'finalizado')

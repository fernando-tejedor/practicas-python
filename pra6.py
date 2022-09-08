#autor: Sindy Cárdenas Romo
#fecha: 29/04/2022
#algoritmo: Control de excepciones

#entrada
try: 
    cedula= input("Digite la cédula de ciudadania : ")
    nombre= input("Digite el nombre : ")
    tipoVendedor= input("Digite el tipo de vendedor: 1= PAP 2= Telemercadeo 3= Ejecutivo de ventas  " )
    valorVentas= int(input("Digite el valor de las ventas realizadas en el mes : "))
    valorComision= 0

    #Proceso
    if tipoVendedor == 1:
        valorComision = valorVentas*0.20
    elif tipoVendedor == 2:
            valorComision = valorVentas*0.15
    else:
        valorComision = valorVentas*0.25
        

    #Salida
    if tipoVendedor>=1 and tipoVendedor<=3:
        print(f'El valor a pagar de comisión es {valorComision} ')

except:
        print (f' se presento un error en los datos ingresados')

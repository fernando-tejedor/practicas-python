#nombre
#fecha
#algoritmo

#entrada
numero=int(input('digite el numero de usuarios a calcular tarifa de agua'))
for i in range(numero):
    estado=int(input('ingrese su estado 1:vigente\n 2:suspendido '))
    if estado==1:
        print('su estado es: {vigente}')
    elif estado==2:
        print('su estado es: {suspendido}')
    else:
        print('el estado es incorrecto')
    codigo=int(input('ingrese su codigo'))
    nombre=input('ingrese su nombre')
    estrato=int(input('ingrese su estrato entre 1 y 6 '))
    consumo=float(input('ingrese su consumo en cm3; '))
    valorConsumo=consumo+200
    

#entradas
hectareaBosque=float(input('cantidad de hectareas a reforestar'))
superficieBosque=(hectareaBosque*10000)
pino=0
oyamel=0
cedro=0


#procesos

if superficieBosque > 1000000:
    pino=int(((superficieBosque*0.7)//10)*8)
    oyamel=int(((superficieBosque*0.2)//15)*15)
    cedro=int(((superficieBosque*0.1)//18)*10)

else:
    pino = int(((superficieBosque*0.5)//10)*8)
    oyamel = int(((superficieBosque*0.3)//15)*15)
    cedro = int(((superficieBosque*0.2)//18)*10)

#Salidas
print (f'El número de pinos a sembrar es {pino}\nEl número de Oyameles a sembrar es {oyamel}\nEl número de cedros a sembrar es {cedro}')



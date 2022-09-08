#Entradas
hectareasBosque = float(input('Digite la superficie a reforestar (ht): '))
superficieBosque = hectareasBosque*10000
numeroPino = 0
numeroOyamel = 0
numeroCedro = 0
#Procesos
if superficieBosque > 1000000:
    numeroPino = int(((superficieBosque*0.7)//10)*8)
    numeroOyamel = int(((superficieBosque*0.2)//15)*15)
    numeroCedro = int(((superficieBosque*0.1)//18)*10)
else:
    numeroPino = int(((superficieBosque*0.5)//10)*8)
    numeroOyamel = int(((superficieBosque*0.3)//15)*15)
    numeroCedro = int(((superficieBosque*0.2)//18)*10)

#Salidas
print (f'El número de pinos a sembrar es {numeroPino}\nEl número de Oyameles a sembrar es {numeroOyamel}\nEl número de cedros a sembrar es {numeroCedro}')

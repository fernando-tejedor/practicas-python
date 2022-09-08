#Entradas
codigo = input('Digite codigo del estudiante: ')
nombre = input('Digite nombre del estudiante: ')
programa = int(input('1=sisitemas,2=video juegos,3=animacion: '))
indicadorBeca = int(input('1=beca por rendimiento,2=beca cutural,3=sin beca: '))
matricula=0
#Procesos
if programa==1:
    matricula=800000
elif programa==2:
    matricula=1000000
elif programa==3:
    matricula=1200000
else:
    print(f'No ingreso un programa correcto')
    
if indicadorBeca==1:
    matricula-=matricula*0.5
elif indicadorBeca==2:
    matricula-=matricula*0.4
elif indicadorBeca==3:
    matricula=matricula
else:
    print(f'No ingreso un programa correcto')
    
#Salidas
if programa>=1 and programa<=3 and indicadorBeca>=1 and indicadorBeca<=3:
    print(f'El valor de matricula para {nombre} es {matricula}')

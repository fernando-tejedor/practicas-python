for i in range(1,11):
    for j in range(1,11):
        print(f'{i*j:>3}',end='')
    print()

print('------------')

var=int(input('dijita un valor para construir la tabla: '))
for i in range(1,var+1):
    for j in range(1,var+1):
        print(f'{i*j:>5}',end='')
    print()

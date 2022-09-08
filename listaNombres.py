nombre=input('ingrese su nombre para terminar fin:  ')
listaNombres=[]
listaPalabras=[]
while nombre.upper() !='FIN':
    numero=0
    listaNombres.append(nombre)
    lista=nombre.split(' ')
    listaPalabras.append(len(lista)-lista.count(''))
    nombre=input('ingrese su nombre para terminar fin:  ')
print(listaNombres3)
print(listaPalabras)
print('finalizo')

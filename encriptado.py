from io import open

def encritar(cadena,diccionario):
    lista=[]
    for letra in cadena:
        try:
            lista.append(dicionario[letra.lower()])
        except:
            lista.append(letra)
    archivo=open("salida.txt","w")
    for i in lista:
        archivo.write(i)
    archivo.close

def desencritar(cadena,diccionario):
    numeros='0123456789'
    lista=[]
    indice=0
    
encriptado={'a':'00','e':'01','i':'02','o':'03','u':'04'}
desencriptado={'00':'a','01':'e','02':'i','03':'o','04':'u'}
archivo = open("C:/Users/jhon/Documents/mision tic/python/cadena.txt","r")
encritar(archivo.read(),encriptado)
archivo.close()

archivo=open("C:/Users/jhon/Documents/mision tic/python/salida.txt","r")
desencritar(archivo.read(),desencriptado)
archivo.close()

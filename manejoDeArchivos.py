#importar la libreria
from io import open

# creacion y apertura
archivo = open("C:/Users/jhon/Documents/mision tic/python/archivoPrueba.txt","w")

#manipulacion
variable="creacion\napertura\nmanipulacion\ncierre"
archivo.write(variable)

#cierre del archivo
archivo.close()

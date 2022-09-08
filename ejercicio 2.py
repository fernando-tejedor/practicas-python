
#entrada

#leer notas
notaReto1=float(input("digite nota reto 1 = "))
notaReto2=float(input("digite nota reto 2 = "))
notaReto3=float(input("digite nota reto 3 = "))
notaReto4=float(input("digite nota reto 4 = "))
notaReto5=float(input("digite nota reto 5 = "))
notaIngles=float(input("digite nota ingles = "))

#proceso
#calcular
calificacionDefinitiva=(notaReto1*0.1)+(notaReto2*0.1)+(notaReto3*0.2)+(notaReto4*0.2)+(notaReto5*0.2)+(notaIngles*0.2)

#salida

print(f'tu calificacion es {calificacionDefinitiva:,.2f}')

valorCompra=int(input('ingrese valor de su compra: '))



if valorCompra>1000:
    valorCompra = valorCompra-(valorCompra*0.2)
  

print (f' el valor total de la compra es {valorCompra:.2f}')

usuarios={"Marta","David","Elvira","Juan","Marcos"}
administradores={"Juan","Marta"}
administradores.discard("Juan")
administradores.add("Marcos")
grupo=usuarios-administradores
for usuario in grupo:
    if(usuario==administradores):
        print (administradores)
    else:
        print(f'usuarios={usuario}')
for i in usuarios:
    for j in administradores:
        if(i==j):
            print(f'administradores= {i}')

print()
#codigo ejercicio
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}

administradores.discard("Juan")
administradores.add("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "es admin")
    else:
        print(usuario, "no es admin")

print()
numero_magico=12345679 
numero_usuario=int(input("ingresar un numero entre el 1 y 9\n"))
if (numero_usuario<1 or numero_usuario>9):
  print("debes ingresar un numero entero enre 1 y 9")
else:
  numero_magico*=numero_usuario*9
  print(numero_magico)

print()
print("Hola Mundo")
print(type("Hola Mundo")) 
print([1, 10, 100])
print(type([1, 10, 100]))
print(-25)          
print(type(-25))
print(1.167)
print(type(1.167))       
print(["Hola", "Mundo"])
print(type(["Hola", "Mundo"]))  
print(' ')
print(type(' '))
print(True)
print(type(True)) 
print({'Uno':"uno", 'Dos':"dos"}) 
print(type({'Uno':"uno", 'Dos':"dos"}))

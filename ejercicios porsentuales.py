#entrada
cantidadMujeres=float(input("dijite cantidad de mujeres = "))
cantidadHombres=float(input("dijite cantidad de hombres = "))

#proceso
totalEstudiantes=(cantidadMujeres+cantidadHombres)
porcentajeMujeres=((cantidadMujeres*100)/totalEstudiantes)
porcentajeHombres=((cantidadHombres*100)/totalEstudiantes)
#salida
print(f'el porcentaje de mujeres es {porcentajeMujeres:,.2f}')
print(f'el porcentaje de hombres es {porcentajeHombres:,.2f}')

#Autor:Fernando Tejedor
#Fecha:20/04/2022
#Algoritmo:xxxxx

#Entradas

#leer notas de Matematicas
notaExamenM=float(input("dijite la nota de examen de matematicas"))
notaTarea1M=float(input("dijite la nota de tarea 1 de matematicas"))
notaTarea2M=float(input("dijite la nota de tarea 2 de matematicas"))
notaTarea3M=float(input("dijite la nota de tarea 3 de matematicas"))

#leer notas de Fisica
notaExamenF=float(input("dijite la nota de examen de Fisica"))
notaTarea1F=float(input("dijite la nota de tarea 1 de Fisica"))
notaTarea2F=float(input("dijite la nota de tarea 2 de Fisica"))


#leer notas de Quimica
notaExamenQ=float(input("dijite la nota de examen de Quimica"))
notaTarea1Q=float(input("dijite la nota de tarea 1 de Quimica"))
notaTarea2Q=float(input("dijite la nota de tarea 2 de Quimica"))
notaTarea3Q=float(input("dijite la nota de tarea 3 de Quimica"))

#Proseso
#calcular notas materias
notaMatematicas=notaExamenM*0.9+((notaTarea1M+notaTarea2M+notaTarea3M)/3)*0.1
notaFisica=notaExamenM*0.8+((notaTarea1F+notaTarea2F)/2)*0.2
notaQuimica=notaExamenM*0.85+((notaTarea1Q+notaTarea2Q+notaTarea3Q)/3)*0.15
#calcular promedio general
promedioGeneral=(notaMatematicas+notaFisica+notaQuimica)/3

#salidas
print(f'la nota de matematicas es {notaMatematicas:,.2f}')
print(f'la nota de fisica es {notaMatematicas:,.2f}')
print(f'la nota de quimica es {notaMatematicas:,.2f}')

#imprimir promedio general
print(f'el promedio general es {promedioGeneral:,.2f}')

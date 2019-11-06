"""
    @naludena1
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""

import csv

def lineas(archivo):
	return csv.reader(archivo, delimiter=";")

with open("data/data-estudiantes.csv") as midata:

	result = map(lambda x: x[1], lineas(midata))

	result1 = filter(lambda x: x != "email", result1)


	# Funcion en una sola linea de codigo
	print(list(map(lambda x: x[1], filter(lambda x: x != "email")))

	# result = filter(lambda x: x != "email", lineas(midata))

	# result1 = map(lambda x: x[1], result)

	print(list(result1))

	





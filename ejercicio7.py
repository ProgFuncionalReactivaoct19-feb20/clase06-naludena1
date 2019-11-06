"""
    @naludena1
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""

import csv 


def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")

with open("data/trabajadores.csv") as midata:
	lista = (list(lineasDiccionario(midata)))

	#Ordenar por nombre con longitud mayor a 10
	result = filter(lambda x: len(x.items())[2][1] > 10, lista)
	print("Nombres con longitud mayor a 10\n", list(result), "  ")

	result1 = list(filter(lambda x: list(x.items(), lista)))
	# Ordenar por dia de nacimiento
	result2 = sorted(result, key = lambda x: list(x.items())[1][1].split("-")[2])

	print("Orden en base al dia de nacimiento", result2)
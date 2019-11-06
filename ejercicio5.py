"""
    @naludena1
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""


import csv 

# def lineas(archivo):
#	  return csv.reader(archivo, delimiter =";")

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")

with open("data/data-estudiantes.csv") as midata:
	lista = (list(lineasDiccionario(midata)))

# Presentar funcion en una sola linea de codigo
print(list(map(lambda x: list(x.items())[0][1], lista)))




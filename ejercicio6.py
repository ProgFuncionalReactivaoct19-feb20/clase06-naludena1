"""
    @naludena1
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""
import csv 


def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")

with open("data/data-estudiantes.csv") as midata:
	lista = (list(lineasDiccionario(midata)))


	result = map(lambda x: "%s - %s" % (list(x.items())[0][1].split(" ")[1], \
		list(x.items())[1][1].split(".")[0]), lista)
	print(list(result))

"""
result1 = (list(map(lambda x: list(x.items())[0][1], lista)))
funcion = map(lambda x: x.split(" "), result1)
result1Funcion = map(lambda x: x[1], funcion )
print(list(result1Funcion))


result2 = (list(map(lambda x: list(x.items())[1][1], lista)))
funcion2 = map(lambda x: x.split(" "), result2)
result2Funcion = map(lambda x: x[0], funcion2)

print(list(result2Funcion))

"""








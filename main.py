from sys import argv
from random import random

def main():
	n_dimensiones = int(argv[1])
	n_individuos = int(argv[2])
	n_evaluaciones = 10
	res = []
	inicializacion(n_dimensiones, n_individuos, res)
	for i in range(n_evaluaciones):
		iteracion()
	for vector in res:
		print(vector)
	return res 

def iteracion():
	agrupar_vecindades()
	reproduccion()
	evaluacion()
	actualizacion_solucion()
	actualizacion_vecindades()

def inicializacion(n_dimensiones, n_individuos, res):
	for i in range(n_individuos):
		res.append([])
		for j in range(n_dimensiones):
			res[i].append(random())
	for elem in res:
		print(elem)
	
		

def agrupar_vecindades():
	pass

def reproduccion():
	pass

def evaluacion():
	pass

def actualizacion_solucion():
	pass

def actualizacion_vecindades():
	pass

main()

from sys import argv
from random import random
import zdt3_aux as zdt3

class AlgoritmoGenetico():
	
	def __init__(self):
		self.algoritmo = argv[1]
		self.n_dimensiones = int(argv[2])
		self.n_individuos = int(argv[3])
		self.n_funciones_objetivo = 2
		self.n_evaluaciones = int(argv[4])
		self.res = []
		self.pesos_funciones_objetivo = [float(argv[5]), float(argv[6])]
		self.indice_cruce = float(argv[7])
		self.indice_mutacion = float(argv[8])
		self.maximo_generaciones = int(argv[9])
		self.indice_llamada = float(argv[10])
		self.mejor_individuo = None
	
	def main(self):
		self.inicializacion()
		for i in range(self.n_evaluaciones):
			print('---------- Iteración ' + str(i) + ' ----------')
			self.iteracion()
		print('Resultado ' + str(self.mejor_individuo.value))
		print('Fitness ' + str(self.mejor_individuo.fitness))		
		return self.res

	def iteracion(self):
		self.agrupar_vecindades()
		self.reproduccion()
		self.evaluacion()
		self.actualizacion_solucion()
		self.actualizacion_vecindades()
		self.actualizar_generaciones()
		self.seleccion_natural()
		self.llamada()
		print('fitness : ' + str(self.mejor_individuo.fitness))
		print('edad  : ' + str(self.mejor_individuo.numero_generaciones))

	def inicializacion(self):
		for i in range(self.n_individuos):
			individuo = Individuo()
			for j in range(self.n_dimensiones):
				individuo.value.append(random())
			self.res.append(individuo)
			
	def agrupar_vecindades(self):
		pass

	def reproduccion(self):
		temp_res = self.res
		annadidos_cruce = []
		annadidos_mutacion = []
		for individuo in temp_res:
			if(random() <= self.indice_mutacion):
				annadidos_mutacion.append(Individuo.mutar(individuo))
		for individuo_1 in temp_res:
			for individuo_2 in temp_res:
				if(random() <= self.indice_cruce):
					annadidos_cruce.append(Individuo.cruzar(individuo_1, individuo_2))
		temp_res = temp_res + annadidos_cruce + annadidos_mutacion
		self.res = temp_res
		print('Tamaño poblacion : ' + str(len(self.res)))

	def evaluacion(self):
		if self.algoritmo == 'zdt3':
			for individuo in self.res:
				individuo.fitness_1 = zdt3.f1(individuo.value)
				individuo.fitness_2 = zdt3.f2(self.n_dimensiones, individuo.value)
				individuo.fitness = self.pesos_funciones_objetivo[0] * individuo.fitness_1 + self.pesos_funciones_objetivo[1] * individuo.fitness_2
		
	def actualizacion_solucion(self):
		temp_res = sorted(self.res, key = Individuo.getFitness)
		self.res = temp_res
		self.mejor_individuo = self.res[0]

	def actualizacion_vecindades(self):
		pass

	def seleccion_natural(self):
		temp_res = self.res[0:self.n_individuos]
		self.res = temp_res

	def actualizar_generaciones(self):
		temp_res = sorted(self.res, key = Individuo.getEdad, reverse = True)
		while len(temp_res) > 100 and temp_res[0].numero_generaciones >= self.maximo_generaciones:		
			del temp_res[0]
		for individuo in temp_res:
			individuo.numero_generaciones = individuo.numero_generaciones + 1
		self.res = temp_res

	def llamada(self):
		temp_res = self.res
		for individuo in temp_res:
			for i in range(self.n_dimensiones):
				individuo.value[i] = individuo.value[i] + (self.mejor_individuo.value[i] - individuo.value[i]) * self.indice_llamada
		self.res = temp_res


class Individuo():

	def __init__(self):
		self.value = []
		self.fitness = None
		self.fitness_1 = None
		self.fitness_2 = None
		self.numero_generaciones = 0

	@staticmethod
	def getFitness(individuo):
		return individuo.fitness

	@staticmethod
	def getEdad(individuo):
		return individuo.numero_generaciones
	
	@staticmethod
	def mutar(individuo):
		nuevo_individuo = Individuo()
		muta_pares = False
		posicion = 0
		if random() >= 0.5:
			muta_pares = True
		for element in individuo.value:
			if muta_pares and posicion % 2 == 0:
				nuevo_individuo.value.append(random())
			elif not muta_pares and posicion % 2 != 0:
				nuevo_individuo.value.append(random())
			else:
				nuevo_individuo.value.append(element)
		return nuevo_individuo

	@staticmethod
	def cruzar(individuo_1, individuo_2):
		nuevo_individuo = Individuo()
		muta_pares = False
		if random() >= 0.5:
			muta_pares = True
		for posicion in range(len(individuo_1.value)):
			if muta_pares and posicion % 2 == 0:
				nuevo_individuo.value.append(individuo_1.value[posicion])
			elif not muta_pares and posicion % 2 != 0:
				nuevo_individuo.value.append(individuo_1.value[posicion])
			else:
				nuevo_individuo.value.append(individuo_2.value[posicion])
		return nuevo_individuo



		
ag = AlgoritmoGenetico()
ag.main()

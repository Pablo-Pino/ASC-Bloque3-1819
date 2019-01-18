from math import sqrt, sin , pi

def f1(x):
	return x[0]

def f2(n, x):
	return g(n, x) * h(n, f1(x), g(n, x))

def g(n, x):
	sumatorio = 0.
	for i in range(1, n-1):
		sumatorio = sumatorio + x[i]
	return 1 + (9./(n-1)) * sumatorio

def h(n, f1, g):
	return 1 - sqrt(f1 / g) - f1 / g - (f1 / g) * sin(10*pi*f1)

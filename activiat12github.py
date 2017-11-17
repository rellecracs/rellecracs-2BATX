# -*- coding: utf-8 -*-
operacion = []
def suma (a,b):
	resultado = a+b
	return resultado
	
def resta (a,b):
	resultado = a-b
	return resultado
	
def multi (a,b):
	resultado = a*b
	return resultado
	
def divi (a,b):
	resultado = a/b
	return resultado

global resultado
resultado=0

operacion = raw_input('¿Qué operación desea realizar?¿Suma (S), resta (R), multiplicación (M) o división(D)?')

a = int(input('Escriu el primer nombre que vol operar'))
b = int(input('Escriu elsegon nombre que vol operar'))
if operacion == 'S':
	resultado=suma(a,b)
	print resultado
if operacion == 'R':
	resultado = resta(a,b)
	print resultado
if operacion == 'M':
	resultado = multi(a,b)
	print resultado
if operacion == 'D':
	resultado = divi(a,b)
	print resultado
	
	

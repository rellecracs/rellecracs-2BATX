# -*- coding: utf-8 -*-
def crealista(lista):
	cantidad = int(input('Quants elements vols sumar?'))
	if cantidad < 0:
		print 'És impossible!'
	else: 
		for i in range(cantidad):
			num = int(input('Introdueix un numero'))
			lista+= [num]
		print lista
def sumalista(lista):
		suma = 0
		for i in lista:
			suma+=i
		print suma
numero = 0
lista = []
crealista(lista)
sumalista(lista)

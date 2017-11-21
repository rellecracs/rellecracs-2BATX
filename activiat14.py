# -*- coding: utf-8 -*-
def crealista(lista):
	cantidad = int(input('Quants elements vols sumar per fer la mitjana?'))
	if cantidad < 0:
		print 'És impossible!'
	else: 
		for i in range(cantidad):
			num = int(input('Introdueix un numero'))
			lista+= [num]
		print lista
	return 
	
def mitjanalista(lista):
	suma = 0
	for i in (lista):
		suma+=i
	mitjana = suma/len(lista)
	print mitjana
	return 
lista = []
crealista(lista)
mitjanalista(lista)

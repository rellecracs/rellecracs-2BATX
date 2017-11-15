# -*- coding: utf-8 -*-
def bisiesto(fecha):
	print("Comprobador de anos bisiestos")
	if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
		print("El ano", fecha, "es un ano bisiesto.")
	else:
		print("El ano", fecha, "no es un ano bisiesto.")
		
		
fecha = int(input("Escriba un ano y le diré si es bisiesto: "))
bisiesto(fecha)

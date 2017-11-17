
def rectangle(param1, param2, caracter):
	for i in range(param1):
		for j in range(param2):
			print caracter,
		print " "

altura = int(input("Indroduix l'amplaria del rectangle que vol crear"))
amplaria = int(input("Quina altura vol per al rectangle?"))
caracter = raw_input("En quin caracter vol realitzar el rectangle?")
rectangle(amplaria,altura,caracter)

with open("clientes.csv", "r", encoding="utf-8") as arquivo:
	for linha in arquivo:
		tokens = linha.strip().split(",")
		print(tokens)


#^ Numa forma onde o cenário são muitos dados, podes realizar a leitura de outra
#^ forma:
import csv

with open("clientes.csv", newline="", encoding="utf-8") as csvfile:
	leitor = csv.reader(csvfile, delimiter=",")
	print('Com import csv ===>')
	for linha in leitor:
		print(linha)

# =====================================
#^ => linhas e colunas
#^ => matrizes (linhas aninhadas)
# =====================================
#! Criando uma matriz 3x3 usando listas aninhadas
matriz = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]


#^ Acessando um elemento específico (linha 1, coluna 2)
print(matriz[1][2]) # Saída: 6



# Percorrendo a matriz linha por linha for linha in matriz:
for linha in matriz: 
	print("linha", linha, end=" ") # Imprime os elementos da linha separados por espaço
	print()	# Nova linha para organizar a saída
	for coluna in linha: 
		print("coluna", coluna, end=" | ") # Imprime os elementos da coluna separados por barra vertical
	print()	# Nova linha para organizar a saída

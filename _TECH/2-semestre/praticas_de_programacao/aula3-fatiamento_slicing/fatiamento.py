#
#^ lista[início:fim:passo]

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sublista  =  numeros[2:7]	# Do índice 2 ao 6
print(sublista)	# Saída: [2, 3, 4, 5, 6]


numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = numeros[::2]	# Pegando elementos com passo 2
print(pares)	# Saída: [0, 2, 4, 6, 8]


numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
invertida  =  numeros[::-1]	# Passo negativo para inverter
print(invertida)	# Saída: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros[2:5] = [20, 30, 40]	# Substituindo elementos
print(numeros)	# Saída: [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]


numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del numeros[2:5] # Remove os elementos do índice 2 ao 4
print(numeros) # Saída: [0, 1, 5, 6, 7, 8, 9]


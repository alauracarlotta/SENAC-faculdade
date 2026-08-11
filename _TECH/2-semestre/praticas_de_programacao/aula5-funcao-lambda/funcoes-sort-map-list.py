#
#* .sort() e .sorted()
#^ Exemplo 1
numeros = [5, 2, 9, 1, 5, 6]

# Ordenando a própria lista numeros.sort()
print(numeros)	# [1, 2, 5, 5, 6, 9]

# Ordenando sem modificar a lista original 
nova_lista = sorted(numeros, reverse=True) 
print(nova_lista)  # [9, 6, 5, 5, 2, 1]


#^ Exemplo 2
pessoas = [("Alice", 25), ("Bob", 30), ("Carol", 20)] 
pessoas.sort(key=lambda x: x[1])	# Ordena pela idade 
print(pessoas)	# [("Carol", 20), ("Alice", 25), ("Bob", 30)]


#--------------------------

#* .map()
#^ Exemplo 1
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros)) 
print(dobrados)	# [2, 4, 6, 8, 10]


#^ Exemplo 2
nomes = ["alice", "bob", "carol"] 
nomes_maiusculos = list(map(str.upper, nomes))
print(nomes_maiusculos)	#  ["ALICE",  "BOB",  "CAROL"]


#--------------------------

#* .list() -> útil ao trabalhar com iteradores, map(), filter(), zip(), entre outros.
#^ Exemplo 1
numeros = list(range(5))
print(numeros)	# [0, 1, 2, 3, 4]


#^ Exemplo 2
valores = map(lambda x: x**2, [1, 2, 3, 4]) 
valores_lista = list(valores) 
print(valores_lista)	# [1, 4, 9, 16]


#^ Exemplo 3
# Suponha que você recebeu uma lista de temperaturas em graus Celsius e precisa
# convertê-las para Fahrenheit usando Python.
# Primeiramente, vamos resolver este problema utilizando um código imperativo e
# tradicional, sem o uso de funções.

# Lista de temperaturas em Celsius 
celsius = [0, 10, 20, 30, 40, 100]

# Criando uma lista vazia para armazenar os resultados 
fahrenheit = []

# Iterando sobre a lista e convertendo cada valor 
for temp in celsius:
	f = (temp * 9/5) + 32	# Aplicando a fórmula de conversão 
	fahrenheit.append(f)	# Adicionando o resultado à nova lista

# Exibindo a lista de temperaturas em Fahrenheit
print(fahrenheit)


#* podemos refatorar esse código para o uso de funções tradicionais

# Função para converter Celsius para Fahrenheit 
def celsius_para_fahrenheit(c):
	return (c * 9/5) + 32

# Lista de temperaturas em Celsius
celsius = [0, 10, 20, 30, 40, 100]

# Criando uma lista vazia para armazenar as temperaturas convertidas
fahrenheit = []

# Percorrendo a lista celsius elemento por elemento
for temp in celsius:
	# Convertendo a temperatura atual de Celsius para Fahrenheit
	temp_fahrenheit = celsius_para_fahrenheit(temp)
	# Adicionando a temperatura convertida à lista fahrenheit
	fahrenheit.append(temp_fahrenheit)

# Exibindo a lista final de temperaturas convertidas
print(fahrenheit)


#! Ainda no exemplo 3 => COM FUNÇÃO LAMBDA, MAP() E LIST()
# Lista de temperaturas em Celsius
celsius = [0, 10, 20, 30, 40, 100]

# Aplicando a conversão com map() e lambda
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

# Exibindo o resultado 
print(fahrenheit)

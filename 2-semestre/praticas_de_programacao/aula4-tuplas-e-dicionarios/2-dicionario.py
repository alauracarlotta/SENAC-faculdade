#
#^ DICIONÁRIOS

# Criando um dicionário de uma pessoa 
pessoa = {
	"nome": "João da Silva",
	"idade": 35,
	"email": "joao.silva@email.com",
	"telefone": "+55 11 99999-8888"
}

print(pessoa) #saida {‘nome’: ‘João da Silva’, ‘idade’: 35, ‘email’: ‘joao.silva@email.com’, ‘telefone’: ‘+55 11 99999-8888’}


pessoa = {
	"nome": "João da Silva",
	"idade": 35,
	"email": "joao.silva@email.com",
	"telefone": "+55 11 99999-8888",
	"endereco": {
		"rua": "Av. Paulista",
		"numero": 1234,
		"cidade": "São Paulo",
		"estado": "SP",
		"cep": "01311-200"
	},
	"documentos": {
		"cpf": "123.456.789-00",
		"rg": "12.345.678-9"
	}
}

# Exemplo de acesso aos dados 
print(pessoa["nome"])	# Saída: João da Silva
print(pessoa["endereco"]["cidade"])	# Saída: São Paulo
print(pessoa["documentos"]["cpf"])	# Saída: 123.456.789-00

pessoa["idade"] = 36	# Atualizando um valor existente 
pessoa["cidade"] = "São Paulo"	# Adicionando uma nova chave


del pessoa["telefone"]	# Remove uma chave específica print(pessoa)

telefone = pessoa.pop("email")	# Remove e retorna o valor associado
print(telefone)	# Saída: joao.silva@email.com


# Percorrendo chaves e valores
for chave, valor in pessoa.items(): 
	print(f"{chave}: {valor}")

print(pessoa.keys())	# Retorna todas as chaves 
print(pessoa.values()) # Retorna todos os valores 
print(pessoa.items())	# Retorna pares chave-valor


if "email" in pessoa:
	print("E-mail cadastrado:", pessoa["contato"]["email"])


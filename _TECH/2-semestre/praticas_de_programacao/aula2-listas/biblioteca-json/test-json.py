import json

dados = {
	'nome': "Laura",
	'idade': 32,
	'cidade': "Jundiaí"
}

with open("dados.json", "w") as arquivo:
	json.dump(dados, arquivo, indent=4)

print('Dados salvos com sucesso!')

with open("dados.json", "r") as arquivo:
	dados_carregados = json.load(arquivo)

print(f'Dados carregados: {dados_carregados}')

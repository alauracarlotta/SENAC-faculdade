dados = [' João ', 'Maria', ' Carlos', 'Ana ', 'Paulo ']
telefones = ['(11)98765-4321', '98765-4321', '98765-4321', '(41)98765-4321', '98765-4321']

dados_limpos = [nome.strip() for nome in dados]  # Remove espaços em branco
print(dados_limpos)  # Saída: ['João', 'Maria', 'Carlos', 'Ana', 'Paulo']


iniciais = [nome[:3] for nome in dados_limpos]  # Pega as três primeiras letras
print(iniciais)  # Saída: ['Joã', 'Mar', 'Car', 'Ana', 'Pau']


telefones_padronizados = []
for tel in telefones:
	if tel.startswith('('):
		telefones_padronizados.append(tel[4:])  # Remove o DDD
	else:
		telefones_padronizados.append(tel)  # Mantém o telefone como está

print(telefones_padronizados)  # Saída: ['98765-4321', '98765-4321', '98765-4321', '98765-4321', '98765-4321']

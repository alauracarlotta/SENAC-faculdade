#
#^ Exemplo 1
arquivo = open("exemplo.txt", "r")	# abre para leitura
conteudo = arquivo.read()
print(conteudo)
arquivo.close()


#^ Exemplo 2
with open("exemplo.txt", "r") as arquivo: 
	conteudo = arquivo.read()
	print(conteudo)
# Arquivo é fechado automaticamente aqui quando o bloco fecha


#^ Exemplo 3
with open("exemplo.txt", "r") as arquivo:
	linha1 = arquivo.readline()
	linhas = arquivo.readlines()
	print(linha1)
	print(linhas)


#^ Exemplo 4
# Sobrescreve o conteúdo
with open("saida.txt", "w") as arquivo:
	arquivo.write("Primeira linha.\n")
	arquivo.write("Segunda linha.\n")

# Adiciona ao final do arquivo
with open("saida.txt", "a") as arquivo:
	arquivo.write("Linha adicionada.\n")


#^ Exemplo 5
#? Outros dois pontos importantes na manipulação de arquivos estão na escolha da
#? codificação e no tratamento de erros. 
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
	print(arquivo.read())

#? Para evitar encerramentos desnecessários na aplicação, as funções e os
#? objetos de manipulação de arquivos geram exceções para algumas situações; 
#? por exemplo, quando o arquivo não é encontrado ou quando a aplicação não 
#? possui autorização para acesso.
try:
	with open("inexistente.txt", "r") as arquivo:
		conteudo = arquivo.read()
except FileNotFoundError:
	print("Arquivo não encontrado.")

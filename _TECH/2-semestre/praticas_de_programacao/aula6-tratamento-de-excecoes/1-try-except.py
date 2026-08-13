#
#^ Try - Except
#^ Tratamento de exceções
try:
    # Código que pode gerar uma exceção
    pass
except ExceptionType:
    # Código a ser executado se a exceção ocorrer
    pass


#^ Exemplo 1
try:
	x = 1 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero não permitida!")


#^ Exemplo 2
try:
	num = int(input("Digite um número: ")) 
	resultado = 10 / num
except ValueError:
	print("Erro: você deve digitar um número inteiro válido.")
except ZeroDivisionError:
	print("Erro: divisão por zero não é permitida.") 
else:
	print(f"Resultado: {resultado}")


#^ Exemplo 3
try:
	arquivo = open("dados.txt", "r") 
	conteudo = arquivo.read()
except FileNotFoundError: 
	print("Arquivo não encontrado.")
else:
	print("Arquivo lido com sucesso!") 
finally:
	print("Encerrando o processo.")


import time

# Lista principal para armazenar os dicionários dos produtos
stock = []

# Lista com mensagens de erro
error_message = {
	"menu_error": "⚠️  Por favor, escolha uma das opções válidas do menu.\n",
    "calculate_total_stock_error_message": "Não há produtos cadastrados.\n",
	"code_error_product": "⚠️  Informe um código válido para o produto.\n",
	"name_error_product": "⚠️  Informe corretamente o nome do produto.\n",
	"price_error_product": "⚠️  Informe o valor correto do produto.\n",

""" new_product = {
		"codigo": 123,
		"nome": 'test1',
		"preco": 50.00,
		"quantidade": 10
"""


#* ok
#& * - Mensagens de erro
def incorrect_option(code_error):
	print("\n⚠️  OPÇÃO INVÁLIDA ou DIGITAÇÃO INCORRETA.")
	print(code_error)


def display_menu() :
	"""Exibe o menu de opções e retorna a escolha do usuário."""
	print('================== MENU =================')
	print('1 - Cadastrar Produto')
	print('2 - Calcular Total de Produtos em Estoque')
	print('0 - SAIR')
	print('=========================================')
	try:
		value_option = int(input('Informe a opção desejada: '))
		return value_option
	except ValueError:
		return -1


# ok
def incorrect_option(code_error):
	print("\n⚠️  OPÇÃO INVÁLIDA ou DIGITAÇÃO INCORRETA.")
	print(code_error)


# ok
def calculate_total_stock():
    """Função que fará a soma de todas as quantidades."""
    print("\n--- Total de Produtos em Estoque ---")
    stock_total = sum(map(lambda x: x["quantidade"], stock))
    return stock_total


# TODO: Implementar lógica de cadastro, validação de código duplicado
# e validação de preço/quantidade não negativos!
def register_product():
    """Função que será responsável pelo cadastro e validações."""
    print("\n--- Cadastrar Produto ---")
    code = code_product()
    new_product = {
		"codigo": code
	}
    stock.append(new_product)
    print(stock)




#* ok
#& 3 - Calcula total de estoque
def calculate_total_stock():
    """Função que fará a soma de todas as quantidades."""
    print("\n--- Total de Produtos em Estoque ---")

    if len(stock) > 0:
        stock_total = sum(map(lambda x: x["quantidade"], stock))
        print(f'Valor total: {stock_total} itens. \n')
        return
    else:
        print(error_message["calculate_total_stock_error_message"])


#* ok
#& * - codigo
def code_product():
	"""Implementa validação de código do produto duplicado"""
	print('entrei no code product')
	while True:
		try:
			entry = input('Informe o código de barras do produto: ').strip()
			new_code = int(entry)

			if new_code < 0:
				incorrect_option(error_message["code_error_product"])
			elif not new_code in list(map(lambda x: x['codigo'], stock)):
				return new_code
			else:
				print(f'\nO código {new_code} é de um produto já registrado. Adicione um novo código!\n')
		except ValueError:
			incorrect_option(error_message["code_error_product"])

#* ok
#& * - nome
def name_product():
	print('entrei no NAME product')
	"""
    Valida se a entrada atende aos requisitos mínimos de formato.

    Regras de validação:
    - Comprimento mínimo de 3 caracteres (aceita qualquer caractere).
    - Exige pelo menos 2 letras em qualquer posição (suporta acentuação, cedilha e caracteres Unicode via \p{L}).

    Exemplos válidos:   'açó', 'a1b', 'café', 'pão1'
    Exemplos inválidos: 'ab' (< 3 caracteres), 'a12' (< 2 letras), '123' (sem letras)
    """

	valid_name_regex = r"^(?=(?:.*\p{L}){2,}).{3,}$"
	while True:
		try:
			new_name = input('Informe o nome do produto: ')
			if regex.search(valid_name_regex, new_name):
				return new_name
			else:
				print('else name')
				incorrect_option(error_message["name_error_product"])
		except ValueError:
			print('except')
			incorrect_option(error_message["name_error_product"])


#! TODO: Implementar lógica de validação de preço não negativos!
#& - preço
def price_product():
	print('entrei no PRICE product')
	while True:
		try:
			# Troca vírgula por ponto para aceitar entradas como 10,50
			entry = input('Informe o preço do produto: R$ ').strip().replace(',', '.')
			new_price = float(entry)
			
			if new_price < 0:
				incorrect_option(error_message["price_error_product"])
				continue # Volta para o início do loop em caso de preço negativo

			return f"R$ {new_price:.2f}".replace('.', ',')
		except ValueError:
			incorrect_option(error_message["price_error_product"])


while True:
	value_menu = display_menu()
	if value_menu == 1:
		print('cadastrar produto')
		register_product()

	# ok
	elif value_menu == 2:
		print(f'Valor total: {calculate_total_stock()} itens. \n')

	# ok
	elif value_menu == 0:
		break
	
	# ok
	else:
		incorrect_option(error_message["menu_error"])


print('\n...ENCERRANDO O SISTEMA:')
time.sleep(2)
print('Obrigado(a) por usar o nosso programa! ✨')

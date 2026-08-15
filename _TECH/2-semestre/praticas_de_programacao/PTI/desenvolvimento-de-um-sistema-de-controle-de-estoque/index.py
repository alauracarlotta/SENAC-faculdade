import time

# Lista principal para armazenar os dicionários dos produtos
stock = [
	{
		"codigo": 1234,
		"nome": 'test1',
		"preco": 50.00,
		"quantidade": 10
	},
	{
		"codigo": 1235,
		"nome": 'test1',
		"preco": 50.00,
		"quantidade": 10
	},
	{
		"codigo": 1236,
		"nome": 'test1',
		"preco": 50.00,
		"quantidade": 10
	},
	{
		"codigo": 1237,
		"nome": 'test1',
		"preco": 50.00,
		"quantidade": 10
	}
]

# Lista com mensagens de erro
error_message = {
	"menu_error": "⚠️  Por favor, escolha uma das opções válidas do menu.\n",
	"code_error_product": "⚠️  Informe um código válido para o produto.\n",

""" new_product = {
		"codigo": 123,
		"nome": 'test1',
		"preco": 50.00,
		"quantidade": 10
	}

    stock.append(new_product) """

# ok
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


# TODO: Implementar lógica de validação de código duplicado
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


# TODO: Implementar lógica de validação de preço não negativos!
def price_product(price):
	return price


# TODO: Implementar lógica de validação de quantidade não negativos!
def quantity_product(quantity):
	return quantity


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

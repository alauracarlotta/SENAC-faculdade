"""
Sistema de Gerenciamento de Estoque (CLI)

Este script gerencia o cadastro, exibição e cálculo de produtos em estoque
utilizando uma interface baseada em terminal (CLI).
"""


import regex

#? [ ] Remover prints
#? [ ] Remover comentários
#? [ ] Verificar 'docstrings' de cada função.
#? [ ] Add README.md 

# Lista principal para armazenar os dicionários dos produtos
stock = []

# Lista com mensagens de erro
error_message = {
	"menu_error": "⚠️  Por favor, escolha uma das opções válidas do menu.\n",
    "calculate_total_stock_error_message": "Não há produtos cadastrados.\n",
	"code_error_product": "⚠️  Informe um código válido para o produto.\n",
	"name_error_product": "⚠️  Informe corretamente o nome do produto.\n",
	"price_error_product": "⚠️  Informe o valor correto do produto.\n",
	"quantity_error_product": "⚠️  Informe a quantidade correta do produto.\n",
}

	"""Exibe no terminal uma mensagem padronizada para entradas e opções inválidas.

    Args:
        code_error (str): Mensagem de erro específica a ser apresentada ao usuário.
    """
	print("\n⚠️  OPÇÃO INVÁLIDA ou DIGITAÇÃO INCORRETA.")
	print(code_error)


	"""Exibe o menu principal de navegação e captura a escolha do usuário.

    Returns:
        int: O número da opção selecionada pelo usuário ou -1 em caso de entrada inválida.
    """
	print('================== MENU =================')
	print('1 - Cadastrar Produto')
	print('2 - Visualizar Estoque (Tabela)') # <--- Nova opção!
	print('3 - Calcular Total de Produtos em Estoque')
	print('0 - SAIR')
	print('=========================================')
	try:
		menu_option = int(input('Informe a opção desejada: '))
		return menu_option
	except ValueError:
		return -1


#! TODO: Padronizar variáveis? pt ou en?
    """Gerencia o fluxo completo de cadastro de um novo produto no estoque.

    Solicita e valida código, nome, preço e quantidade antes de armazenar
    o item no dicionário global de estoque.
    """
    print("\n--- Cadastrar Produto ---")
    code = get_product_code()
    name = get_product_name()
    price = get_product_price()
    quantity = get_product_quantity()
    
    # TODO: verificar a ebição do está cadastrado.
    new_product = {
		"code": code,
		"name": name,
		"price": price,
		"quantity": quantity
	}

    stock.append(new_product)
    print(stock) # TODO: Adicionar msg de 'item cadastrado com sucesso'


#! TODO: Adicionar Tabela de apresentação de estoque
#& 2 - Apresentar tabela de estoque
def display_stock():
	return

    """Calcula e exibe a quantidade total somada de itens presentes no estoque via função lambda.

    Soma as quantidades de todos os produtos cadastrados e exibe o resultado.
    """
    print("\n--- Total de Produtos em Estoque ---")

    if len(stock) > 0:
        stock_total = sum(map(lambda x: x["quantidade"], stock))
        print(f'Valor total: {stock_total} itens. \n')
        return
    else:
        print(error_message["calculate_total_stock_error_message"])


    """Solicita e valida o código de barras do produto.

    Garante que a entrada contenha apenas dígitos (até 13 caracteres),
    preenche com zeros à direita até atingir 13 dígitos (`ljust`) e
    verifica a ausência de duplicatas na lista de estoque.

    Returns:
        int: Código de barras validado e convertido para número inteiro.
    """

			if new_code < 0:
				incorrect_option(error_message["code_error_product"])
			elif not new_code in list(map(lambda x: x['codigo'], stock)):
				return new_code
			else:
				print(f'\nO código {new_code} é de um produto já registrado. Adicione um novo código!\n')
		except ValueError:
			incorrect_option(error_message["code_error_product"])

	"""Solicita e valida o nome do produto através de expressões regulares (Regex).

    Exige no mínimo 3 caracteres no total e pelo menos 3 letras (suportando Unicode/acentuação).

    Returns:
        str: Nome do produto validado.
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


	"""Solicita e valida o preço unitário do produto.

    Garante que o valor digitado não seja negativo e o converte para o formato
    monetário brasileiro (R$ X,XX).

    Returns:
        str: Preço formatado em string como moeda brasileira.
    """
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


def get_product_quantity() -> int:
	"""Solicita e valida a quantidade de itens do produto.

    Garante que a entrada seja um número inteiro positivo.

    Returns:
        int: Quantidade de itens em estoque.
    """

	while True:
		try:
			entry = input('Informe a quantidade de itens do produto: ').strip()
			print('----------------------------------------')

			new_quantity = int(entry)
			
			if new_quantity <= 0:
				incorrect_option(error_message["quantity_error_product"])
				continue
			return new_quantity
		except ValueError:
			incorrect_option(error_message["quantity_error_product"])


# Loop principal de execução do menu
while True:
	value_menu = display_menu()
	if value_menu == 1:
		register_product()

# TODO: Adicionar Tabela de apresentação de estoque
	elif value_menu == 2:
		display_stock()

	elif value_menu == 3:
		calculate_total_stock()

	elif value_menu == 0:
		break

	else:
		incorrect_option(error_message["menu_error"])


print('\n...ENCERRANDO O SISTEMA:')
time.sleep(2)
print(f'{ITALIC}{BOLD}Obrigado(a) por usar o nosso programa! ✨{RESET}')

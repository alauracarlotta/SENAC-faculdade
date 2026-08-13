import time
# stock = []
inventory = []

""" new_product = {
	"codigo": int(input('Informe o código de barras do produto: ')),
	"nome": input('Informe o nome do produto: '),
	"preco": float(input('Informe o preço do produto: R$ ')),
	"quantidade": int(input('Informe a quantidade de itens do produto: '))
} """

def display_menu() :
	print('============= MENU =============')
	print('1 - Cadastrar Produto')
	print('2 - Calcular Total de Produtos em Estoque')
	print('0 - SAIR')
	print('================================')
	try:
		value_option = int(input('Informe a opção desejada: '))
		return value_option
	except ValueError:
		return -1


def incorrect_option():
	print("\n⚠️  OPÇÃO INVÁLIDA ou DIGITAÇÃO INCORRETA.")
	print("Por favor, escolha uma das opções válidas do menu.")


def register_product():
    """Função que será responsável pelo cadastro e validações."""
    print("\n--- Cadastrar Produto ---")
    # TODO: Implementar lógica de cadastro, validação de código duplicado
    # e validação de preço/quantidade não negativos!


def calculate_total_stock():
    """Função que fará a soma de todas as quantidades."""
    print("\n--- Total de Produtos em Estoque ---")
    # TODO: Implementar a soma das quantidades dos itens no 'inventory'


while True:
	value_menu = display_menu()
	if value_menu == 1:
		print('cadastrar produto')
		register_product()
	
	elif value_menu == 2:
		print('o estoque é')
		value_menu = display_menu()
	
	elif value_menu == 0:
		break
	else:
		incorrect_option()


print('\n...ENCERRANDO O SISTEMA:')
time.sleep(2)
print('Obrigado(a) por usar o nosso programa! ✨')

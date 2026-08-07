def menu () :
	print('-------------------------')
	print('********* MENU **********')
	print('-------------------------')
	print('DIGITE [1] para pgmnto à vista, com 10% de desconto;')
	print('DIGITE [2] para pgmnto parcelado;')
	print('-------------------------')


def parcelamento(valor, opcao):
	valor += (valor * opcao["valor_acrescimo"]/100)
	parcela = valor / opcao["parcelas"]
	resultado = f'\nPara pagamento em {opcao["parcelas"]}x, cada parcela será de R$ {parcela:.2f} reais. \n(Valor total com acréscimo de {opcao["valor_acrescimo"]}%, será de R$ {valor:.2f} reais).'
	return resultado


qtde_parcelas = {
	1: {
		'valor_acrescimo': 5,
		'parcelas': 2
	},
	2: {
		'valor_acrescimo': 10,
		'parcelas': 3
	},
}

valor = float(input('Digite o valor do produto: R$ '))

menu()

opcao_pagamento = int(input('Digite a forma de pagamento desejada: [1/2] '))

if opcao_pagamento == 1:
	valor -= (valor * 10/100)
	resultado = f'\nPara pagamento à vista, com 10% de desconto: \nValor total de R$ {valor:.2f} reais.'

elif opcao_pagamento == 2:
	parcelas = int(input(
		'\nDIGITE [1]: 2x -> Acréscimo de 5% \nDIGITE [2]: 3x -> Acréscimo de 10%\n \nOPÇÃO [1/2]: '
	))
	
	resultado = parcelamento(valor, qtde_parcelas[parcelas])

else:
	resultado = '\nOpção não encontrada!'

resultado += '\n\n>>>>>>>>>>>>>>> Obrigada por usar nosso sistema.'

print(resultado)

'''
Uma loja oferece 2 tipos de pagamento:
* À vista, com 10% de desconto;
* Parcelado em 3x com 5% de acréscimo no valor total para cada parcela;

Escreva um programa que leia o valor de uma compra e exiba:
* O valor final com desconto (pagamento à vista);
* O valor de cada parcela com o acréscimo (pagamento parcelado)
'''

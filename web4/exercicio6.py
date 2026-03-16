'''
Desenvolva um programa que leia números inteiros positivos (incluindo
zero) inseridos pelo usuário. A leitura deve continuar até que um número
negativo seja informado. O número negativo não deve ser incluído nos
cálculos. Ao final, exiba a soma e a média dos números lidos. Caso
nenhum número válido tenha sido informado, exiba uma mensagem
apropriada.
'''

result = 0
cont = 0

number_list = list()
number = int(input('Informe um número inteiro positivo: '))
print('[Digite um número inteiro negativo pra sair]')

while number >= 0:
	result += number
	number_list.append(number)
	number = int(input('Informe um número inteiro positivo: '))
	print('[Digite um número inteiro negativo pra sair]')
	cont += 1

if cont == 0:
	print('Não foi informado nenhum número válido!')

else:
	print(f'A soma dos números {number_list} é {result}.')
	print(f'A média desses números {number_list} é {(result / cont):.1f}')

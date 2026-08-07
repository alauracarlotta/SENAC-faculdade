'''
Escreva um programa que leia a altura e o sexo de uma pessoa (M ou F) e
apresente o seu peso ideal, utilizando as seguintes fórmulas:
• Para homens: (72.7 * altura) – 58.0
• Para mulheres: (62.1 * altura) – 44.7
'''
def calcula_peso_ideal(altura, sexo):
	resultado = ((sexo['param1'] / 100) * altura) - sexo['param2']
	print(f'Você, medindo {altura / 100}m e sendo do sexo {sexo['nome_sexo']}, o seu peso ideal é {resultado:.2f}kg.')

valores_sob_sexo = {
	'F': {
		'param1': 62.1,
		'param2': 44.7,
		'nome_sexo': 'Feminino'
	},
	'M': {
		'param1':72.7,
		'param2': 58.0,
		'nome_sexo': 'Masculino'
	}
}

altura = float(input('\nInforme a sua altura (em cm): '))
sexo = input('\nInforme o seu sexo: [F/M] ').upper()

calcula_peso_ideal(altura, valores_sob_sexo[sexo])
print('\n>>>>>>>>>>>>>>>>>>> Obrigada por usar o nosso sistema!!!')

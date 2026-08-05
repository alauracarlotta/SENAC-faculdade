'''
Crie um algoritmo que calcule o IMC de uma pessoa.
Siga a seguinte tabela:

Classificação 		IMC(kg/m²)
Magresa Grau III	< 16
Magresa Grau II		16 a 16,9
Magresa Grau I		17 a 18,4
Peso Normal 		18,5 a 24,9
Excesso de Peso 	25 a 29,9
Obesidade Grau I 	30 a 34,9
Obesidade Grau II 	35 a 39,9
Obesidade Mórbida 	≥ 40

Fórmula:
IMC = peso/(altura)²
'''

peso = float(input('Informe o seu peso: kg '))
altura = float(input('Informe a sua altura em cm: '))

imc = peso / altura ^ 2

print(f'Seu IMC é de {imc}.')
if imc < 16:
	resultado = 'Equivale a Magresa Grau III. \nCONSULTE UM MÉDICO!'

elif imc >= 16 and imc <= 16.9:
	resultado = 'Equivale a Magresa Grau I.'

elif imc >= 17 and imc <= 18.4:
	resultado = 'Equivale a Magresa Grau I.'

elif imc >= 18.5 and imc <= 24.9:
	resultado = 'Peso normal. \nPARABÉNSSS! \o/ \o/ \o/'

elif imc >= 25 and imc <= 29.9:
	resultado = 'Excesso de peso! FIQUE ATENTO!'

elif imc >= 30 and imc <= 34.9:
	resultado = 'Equivale a Obesidade Grau I.'

elif imc >= 35 and imc <= 39.9:
	resultado = 'Equivale a Obesidade Grau II.'

elif imc > 40:
	resultado = 'Equivale a Obesidade Mórbida! \nProcure um médico!'

print(resultado)

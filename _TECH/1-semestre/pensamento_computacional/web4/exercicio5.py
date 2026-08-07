'''
Desenvolva um programa que leia um número inteiro e apresente a sua
tabuada.
'''

num = int(input('Digite o número da tabuada que você deseja vizualizar: '))
result = 0

print('\n==================================')
print(f'Veja a tabuada do número {num}: ')
print('==================================')

for cont in range(1, 11):
	result = num * cont
	print(f'  {num} x {cont} = {result}')

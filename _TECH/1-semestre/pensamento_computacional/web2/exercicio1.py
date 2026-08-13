''''
Escreva um programa que leia uma temperatura em grau Celsius e converta para 
Fahrenheit, usando a fórmula:

F = (C x 9/5) + 32
'''

graus_celsius = int(input('Informe o valor de graus Celsius: '))

graus_fahrenheit = (graus_celsius * 9/5) + 32

print(f'{graus_celsius} ˚C convertidos para graus Fahrenheit fica {graus_fahrenheit:.1f} ˚F.')

#
#^ Operações com Strings + * 

s1 = 'Olá'
s2 = 'Mundo'
resultado = s1 + ' ' + s2
print(resultado)	# Saída: Olá Mundo


s = 'Python '
print(s  *  3)	# Saída: Python Python Python


s = 'Python'
print(len(s))	# Saída: 6


s = 'Python'
print(s[0]) # Saída: P  (primeiro  caractere)
print(s[-1]) # Saída: n (último caractere)


s = 'Python'
print(s[0:4])	# Saída: Pyth (pega do índice 0 ao 3)
print(s[:4])	# Saída: Pyth (começa no início por padrão)
print(s[2:])	# Saída: thon (vai do índice 2 até o final)
print(s[-4:])	# Saída: thon (pega os últimos quatro caracteres)
print(s[::2])	# Saída: Pto (pula de 2 em 2)


s = 'Python'
print(s[::-1])	# Saída: nohtyP


s = 'Python é incrível'
print('Python'  in  s)	# True
print('Java' not in s) # True

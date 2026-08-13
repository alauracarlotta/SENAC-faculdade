# =============================================================================
#^ Adicionar / Inserir
# =============================================================================
#* .append() - Adiciona um elemento ao final do array.
numeros = [10, 20, 30]
numeros.append(40) # Adiciona 40 no final 
print(numeros)


#* .insert() - Insere um elemento em uma posição específica.
numeros = [10, 20, 30]
numeros.insert(1, 15)	# Insere 15 na posição 1 
print(numeros)


#* .extend() - Adiciona elementos de outra lista ao final do array.
numeros = [10, 20, 30]
numeros.extend([40, 50, 60])	# Adiciona múltiplos valores ao final
print(numeros)

# =============================================================================
#^ Remover / Deletar
# =============================================================================
#* .remove() - Remove a primeira ocorrência de um valor específico.
numeros = [10, 20, 30, 40, 30, 50]
numeros.remove(30)	# Remove a primeira ocorrência de 30
print(numeros)


#* del() - Remove um elemento em uma posição específica.
numeros = [10, 20, 30, 40, 50]
del  numeros[1]	# Remove o elemento no índice 1 (20)
print(numeros)


#* clear() - Remove todos os elementos do array.
numeros = [10, 20, 30, 40, 50]
numeros.clear()	# Esvazia a lista
print(numeros)


# =============================================================================
#^ Alterar / Modificar
# =============================================================================
#* Com índice - Altera o valor de um elemento em uma posição específica.
numeros = [10, 20, 30, 40, 50]
# Alterar o elemento no índice 2 (de 30 para 35)
numeros[2] = 35
print(numeros)


# =============================================================================
#^ Procurar / Pesquisar
# =============================================================================
#* in - Verifica se um valor está presente no array.
numeros = [10, 20, 30, 40, 50]
# Verifica se 30 está na lista
if 30 in numeros:
    print("30 está na lista")


#* in range() - Verifica se um valor está dentro de um intervalo específico.
numeros = [10, 20, 30, 40, 50]
# Buscar manualmente
for i in range(len(numeros)):
	if numeros[i] == 30:
		print("Encontrado no índice:", i)
	break

# ===================================
#* listas são passadas por referência
# ===================================

def adicionar_elemento(lista):
	lista.append(100)	# Modifica a lista original

numeros = [10, 20, 30]
adicionar_elemento(numeros)
print("Lista após a função:", numeros)


# ===================================
#* .copy() - copia da lista original 
# ===================================
def adicionar_elemento_sem_modificar(lista):
	nova_lista = lista.copy()	# Cria uma cópia
	nova_lista.append(100)
	return nova_lista	# Retorna a lista modificada sem alterar a original

numeros = [10, 20, 30]
nova_lista  =  adicionar_elemento_sem_modificar(numeros)
print("Lista original:", numeros)
print("Nova lista modificada:", nova_lista)


# ===================================
#* Retorno da lista sem a arealização de uma cópia.
#^ Os efeitos na lista original podem não ser os esperados.
# ===================================
def adicionar_elemento(lista):
	lista.append(100)	# Modifica a lista original
	return lista	# Retorna a referência da lista original

numeros = [10, 20, 30]
nova_lista  =  adicionar_elemento(numeros)

print("Lista  original:",  numeros)	# Foi modificada
print("Lista retornada:", nova_lista)	# Mesmo endereço na memória


# ===================================
#* O programador pode optar pelo retorno da cópia de uma lista, realizando as modificações que desejar sem afetar a lista original:
# ===================================
def adicionar_elemento_sem_modificar(lista):
	nova_lista = lista.copy()	# Cria uma cópia da lista
	nova_lista.append(100)	# Modifica apenas a cópia
	return nova_lista	# Retorna a cópia modificada

numeros = [10, 20, 30]
nova_lista  =  adicionar_elemento_sem_modificar(numeros)
print("Lista  original:",  numeros)	# Permanece inalterada
print("Lista retornada:", nova_lista)	# Cópia com modificação

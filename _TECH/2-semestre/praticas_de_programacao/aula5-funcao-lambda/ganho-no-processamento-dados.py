#
#* Uma loja precisa aplicar um desconto de 10% em todos os produtos de uma lista.
#^ Forma tradicional

def aplicar_desconto(preco):
	return preco * 0.9

precos = [50, 225, 24, 32, 100, 60]
precos_com_desconto = list(map(aplicar_desconto, precos))
print(precos_com_desconto)


#^ Com função lambda
precos_com_desconto = list(map(lambda preco: preco * 0.9, precos))
print(precos_com_desconto)


#-----------------------------

#* Um bancário quer filtrar transações acima de 100,00
#^ Forma tradicional
def filtrar_transacoes(transacao):
	return transacao > 100

transacoes = [50, 225, 24, 32, 100, 60]
transacoes_filtradas = list(filter(filtrar_transacoes, transacoes))
print(transacoes_filtradas)


#^ Com função lambda
transacoes_filtradas = list(filter(lambda transacao: transacao > 100, transacoes))
print(transacoes_filtradas)

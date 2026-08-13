#
#?  O código define a função verificar_idade(idade), que verifica se a idade 
#?  fornecida é menor que 18; caso seja, a função dispara uma exceção ValueError com
#?  a mensagem “Idade deve ser maior ou igual a 18”. No bloco try, a função é
#?  chamada com o valor 16, o que aciona a exceção. O bloco except captura essa
#?  exceção e imprime a mensagem de erro formatada com o texto “Erro: Idade deve
#?  ser maior ou igual a 18”, evitando que o programa seja interrompido
#?  abruptamente.

#?  Para um uso eficaz de exceções em Python, é fundamental evitar capturas 
#?  genéricas com except Exception, pois isso pode mascarar erros inesperados e 
#?  dificultar a depuração, tornando o código menos previsível. Em vez disso, é 
#?  recomendável capturar exceções específicas para lidar com cada situação de 
#?  maneira apropriada. Além disso, fornecer mensagens de erro claras e 
#?  informativas é essencial para facilitar a identificação e correção do 
#?  problema, indicando exatamente o que aconteceu e, se possível, sugerindo 
#?  uma solução.


#^ Exceções manualmente
#^ Exemplo 4
def verificar_idade(idade):
	if idade < 18:
		raise ValueError("Idade deve ser maior ou igual a 18.")
	return "Acesso permitido."

try:
	print(verificar_idade(16))
except ValueError as e:
	print(f"Erro: {e}")


#^ Exemplo 5
import logging 

logging.basicConfig(level=logging.ERROR) 

try:
	x = 1 / 0
except ZeroDivisionError as e:
	logging.error(f"Erro detectado: {e}")


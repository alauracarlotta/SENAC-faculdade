# Invocando Exceções Manualmente

## Exemplo 4
```python
def verificar_idade(idade):
	if idade < 18:
		raise ValueError("Idade deve ser maior ou igual a 18.")
	return "Acesso permitido."

try:
	print(verificar_idade(16))
except ValueError as e:
	print(f"Erro: {e}")
```

O código define a função verificar_idade(idade), que verifica se a idade fornecida é menor que 18; caso seja, a função dispara uma exceção ValueError com a mensagem “Idade deve ser maior ou igual a 18”. No bloco try, a função é chamada com o valor 16, o que aciona a exceção. O bloco except captura essa exceção e imprime a mensagem de erro formatada com o texto “Erro: Idade deve ser maior ou igual a 18”, evitando que o programa seja interrompido abruptamente.

Para um uso eficaz de exceções em Python, é fundamental evitar capturas genéricas com except Exception, pois isso pode mascarar erros inesperados e dificultar a depuração, tornando o código menos previsível. Em vez disso, é recomendável capturar exceções específicas para lidar com cada situação de maneira apropriada. Além disso, fornecer mensagens de erro claras e informativas é essencial para facilitar a identificação e correção do problema, indicando exatamente o que aconteceu e, se possível, sugerindo uma solução.

* Para saber mais

Em Python é possível personalizar a geração de exceções! Para elaborar classes personalizadas de exceção em Python, é necessário criar uma classe que herde da classe base Exception, permitindo definir erros específicos para um contexto particular da aplicação. Isso é útil quando os erros padrão não representam adequadamente uma situação ou quando se deseja adicionar lógica personalizada ao tratamento de exceções. Dentro da classe, pode-se sobrescrever o método de inicialização para aceitar mensagens de erro personalizadas ou outros parâmetros relevantes. Ao utilizá-la, a exceção pode ser lançada com uma mensagem clara e capturada de forma específica, melhorando a legibilidade do código, facilitando a depuração e permitindo um tratamento mais preciso dos erros.

Outra boa prática é utilizar logs em vez de print(), pois a biblioteca logging permite armazenar erros com diferentes níveis de gravidade (DEBUG, INFO, WARNING, ERROR, CRITICAL), além de possibilitar o envio dessas informações para arquivos ou sistemas externos, garantindo um melhor monitoramento e rastreamento de falhas no código. O código a seguir (exemplo 5) apresenta um exemplo do uso de logs em Python.

## Exemplo 5
```python

import logging 

logging.basicConfig(level=logging.ERROR) 

try:
	x = 1 / 0
except ZeroDivisionError as e:
	logging.error(f"Erro detectado: {e}")

```

O código utiliza a biblioteca logging para registrar erros em vez de simplesmente imprimir mensagens na tela. Primeiro, o módulo logging é importado, e a configuração logging.basicConfig(level=logging.ERROR) define que apenas mensagens de nível ERROR ou superior serão registradas. No bloco try, o programa tenta dividir 1 por 0, o que gera uma exceção ZeroDivisionError. O bloco except captura essa exceção e usa logging.error(f”Erro detectado: {e}”) para registrar a mensagem de erro, em que {e} contém a descrição da exceção (“division by zero”). Isso permite que o erro seja tratado de maneira estruturada e registrado em logs, facilitando a depuração sem interromper a execução do programa.

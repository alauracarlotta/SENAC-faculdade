import time

def finalizar_pedido(numero_pedido, callback):
	print(f'processando pedido {numero_pedido}...')

	time.sleep(5)

	print(f'Pedido {numero_pedido} finalizado!')

	callback(numero_pedido)

def notificar_usuario(numero_pedido):
	print(f'Notificação: Pedido {numero_pedido} finalizado com sucesso!')

finalizar_pedido(188945, notificar_usuario)

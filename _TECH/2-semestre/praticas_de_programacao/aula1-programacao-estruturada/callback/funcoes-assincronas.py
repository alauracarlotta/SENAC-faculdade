import asyncio

async def tarefa_principal(callback):
	print('Executando tarefa principal...')

	await asyncio.sleep(5)
	callback()

def meu_callback():
	print('Callback chamado após a execução assíncrona!')

asyncio.run(tarefa_principal(meu_callback))

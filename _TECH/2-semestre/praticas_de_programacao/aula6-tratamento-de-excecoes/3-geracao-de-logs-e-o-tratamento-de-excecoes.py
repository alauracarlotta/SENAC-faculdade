import logging

#! logging terá a info printada no terminal.
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#! logging terá a info salva no arquivo de nome "app.log".
logging.basicConfig(
	filename='app.log', 
	level=logging.INFO, 
	format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Iniciando o programa corretamente.")
logging.debug("Este é um log de depuração.")
logging.warning("CUIDADO! Algo pode estar errado...")
logging.error("Um erro foi detectado!")
logging.critical("Erro crítico! O programa será encerrado.")

#* try - except aplicado
try:
	x = 10 / 0
except ZeroDivisionError as e:
	logging.error(f"Erro detectado: {e}", exc_info=True)

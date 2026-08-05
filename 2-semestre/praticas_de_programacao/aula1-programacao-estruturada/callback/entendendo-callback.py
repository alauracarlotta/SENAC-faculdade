def welcome(name):
	print(f"Bem-vindo(a), {name}!")

def user_process(callback):
	user = 'Laura'
	callback(user)

user_process(welcome)

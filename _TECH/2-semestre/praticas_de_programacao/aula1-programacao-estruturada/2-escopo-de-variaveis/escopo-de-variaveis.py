# Definição de uma variável global
mensagem_global = "Olá, bem-vindo ao programa!"

def saudacao(nome):
    """Função que usa uma variável global e uma variável local."""
    mensagem_local = f"Olá, {nome}! Tenha um ótimo dia!"
    # Variável local
    print(mensagem_global)  # Acessando a variável global
    print(mensagem_local)  # Acessando a variável local

# Chamando a função
saudacao("Lucas")

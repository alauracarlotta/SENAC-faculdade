# Código otimizado com funções
def calcular_media(n1, n2, n3):
    #Calcula a média de três notas.
    return (n1 + n2 + n3) / 3

def verificar_aprovacao(media, media_aprovacao=7.0):
    #Verifica se a média é suficiente para aprovação.
    return "Aprovado" if media >= media_aprovacao else "Reprovado"

def exibir_resultado(nome, media, resultado):
    #Exibe o nome do aluno, sua média e o status de aprovação.
    print(f"Aluno:  {nome}")
    print(f"Média: {media:.2f}")
    print(f"Resultado: {resultado}")

# Variáveis
nome = "João"
nota1 = 8.0
nota2 = 7.5
nota3 = 6.0

# Processamento
media = calcular_media(nota1, nota2, nota3)
resultado = verificar_aprovacao(media)
exibir_resultado(nome, media, resultado)

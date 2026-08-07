# Código sem modularização (bloco único)
nome = "João"
nota1 = 8.0
nota2 = 7.5
nota3 = 6.0
media = (nota1 + nota2 + nota3) / 3
if media >= 7.0:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"
print(f"Aluno:  {nome}")
print(f"Média: {media:.2f}")
print(f"Resultado: {resultado}")

# Trabalhando com arquivos-texto delimitados

#* TOKEN - é uma unidade de dados extraída de uma sequência de texto,
#* normalmente com base em um delimitador - como uma vírgula, um ponto e vírgula,
#* uma tabulação ou um espaço.abs

#^ Delimitadores previsiveis!

linha = 'Laura, laura@email.com, 32'
token = linha.split(',')
print(token)

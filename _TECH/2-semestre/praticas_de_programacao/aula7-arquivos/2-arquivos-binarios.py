#
#* Manipulação de arquivos binários é mais refinada.

#^ Exemplo 6
with open("audio.mp3", "rb") as arquivo:
	dados = arquivo.read(1024)	# lê os primeiros 1024 bytes

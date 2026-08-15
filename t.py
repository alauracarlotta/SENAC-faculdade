import unicodedata
test = "Geração de logs e o tratamento de exceções".lower().replace(" ", "-")

def sem_acento(texto):
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        ch for ch in texto
        if unicodedata.category(ch) != "Mn"
    )
    return texto.encode("ascii", "ignore").decode("ascii")

print(sem_acento(test))

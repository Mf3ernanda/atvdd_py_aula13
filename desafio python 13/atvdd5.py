def encontra_palavras(lista_palavras, letra):
    palavras_iniciais = [palavra for palavra in lista_palavras if palavra[0] == letra]

    return palavras_iniciais

lista = ["vestido", "blusa", "sapato", "joia", "casaco", "short"]
letra = input("Digite uma letra: ")

resultado = encontra_palavras(lista, letra)
print(f"Palavras que começam com '{letra}': {resultado}")
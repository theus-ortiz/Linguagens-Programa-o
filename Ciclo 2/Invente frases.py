def inverte(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    nova_frase = ' '.join(palavras_invertidas)
    return nova_frase

frase = str(input("Digite a sua frase aqui: "))
frase = inverte(frase)
print(frase)
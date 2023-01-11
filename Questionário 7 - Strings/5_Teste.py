texto = input()
textolist = texto.split()

while len(textolist) > 1:
    inicio = texto.find(textolist[0]) #
    fim = texto.find(textolist[1])
    vazio = texto.find(' ', inicio, fim)

    resultado = fim - vazio - 2

    texto = texto[fim:]
    textolist.pop(0)

    if resultado < 0:
        print(0)
    else:
        print(resultado)

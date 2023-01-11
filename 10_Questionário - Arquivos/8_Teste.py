import os

arquivo = input()[22:]

if os.path.isfile(arquivo):
    with open(arquivo,'r') as f:
        linhas = f.read().split('\n')
        tuplas = []
        for i in linhas:
            nome_num = i.split()
            tuplas += [(nome_num[0],int(nome_num[1]))]
        tuplas.sort(reverse=True,key=lambda t: t[1])
    print('da pra abrir')
    for i in tuplas:
        print(i)
else:
    print('nao da pra abrir')

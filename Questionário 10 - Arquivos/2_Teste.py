with open(input(), 'r') as arquivo:
    linhas = arquivo.read().split('\n')
    for i in linhas:
        linha_str = ''.join(i)
        elementos = linha_str.split(',')
        print(elementos[1])

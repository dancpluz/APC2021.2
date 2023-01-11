with open(input(),'r') as f:
    text = f.read().split('\n')
    count_linha = 0
    for i in text:
        count_linha += 1
        linha = ''.join(i)
        if 'wally' in linha:
            print(count_linha, linha.find('wally')+1, 'horizontal')
            exit()

    colunas = {}
    for i in text:
        for n in range(0,len(i)):
            try:
                colunas[n] += [i[n]]
            except:
                colunas[n] = [i[n]]
    for c in colunas:
        letras = colunas.get(c)
        str = ''.join(letras)
        if 'wally' in str:
            print(str.find('wally')+1, c+1, 'vertical')
            exit()

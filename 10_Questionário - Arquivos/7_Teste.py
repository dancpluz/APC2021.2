with open(input(),'r') as vetor:
    linhas = vetor.read().split('\n')
    numeros = [int(i) for i in linhas[1].split()]
    k = int(linhas[0])
    lista_segmentos = []

    for i in range(len(numeros)):
        try:
            segmento = []
            count = k
            while count > 0:
                segmento += [numeros[i]]
                i += 1
                count -= 1
            lista_segmentos += [segmento]
        except:
            break

    primo = 0
    primo_i = 0

    for i in lista_segmentos:
        n_maior = max(i)
        if 2 * k <= n_maior:
            primo += 1

    for i in lista_segmentos:
        n_menor = min(i)
        if n_menor <= k / 2:
            primo_i += 1

    print(primo,primo_i)

linhas = int(input())

with open('poema.txt', 'r') as poema:
    poema_lista = poema.read().split('\n')

    for i in range(linhas):
        try:
            print(poema_lista[i])
        except:
            pass

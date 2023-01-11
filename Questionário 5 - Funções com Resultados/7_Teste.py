def media(n, cont, soma):
    if n == 0:
        return 0
    elif cont != n:
        i = int(input())
        return media(n, cont+1, soma+i)
    else:
        return soma/n

print(media(3, 0, 0))

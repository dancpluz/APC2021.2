nome = input()
lista = []
fim = 'fim'

while nome != fim:
    lista.append([nome])
    nome = input()

lista.sort()
lista.append(' ')
temp = lista[0]
conta = 0

for i in lista:
    if i == temp:
        conta += 1
    else:
        if conta > 1:
            print(' '.join(temp), conta)
            conta = 1
    temp = i

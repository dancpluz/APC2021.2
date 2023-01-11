#t = quanto calças
#n = tenis disponiveis
#fazer lista de n e outra lista ordenada
#achar o primeiro que é do tamanho certo ou maior que o t
#usar .find para descobrir a posição da lista original

t = input()
n = input().split()
n.sort()

for i in n:
    if int(i) >= int(t):
        print(n.index(i))
        exit()

print(-1)

estudantes = int(input())
roupas = [int(i) for i in input().split()]


for i in roupas:
    if roupas.count(i) > 1:
        print('WOW')
        exit()

print('MEH')

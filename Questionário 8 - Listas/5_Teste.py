n_x = input().split()
n = int(n_x[0]) + 1
x = int(n_x[1])
lista_num = input().split()
''.join(lista_num)
soma = 0

for i in lista_num:
    n -= 1
    soma += int(i) * x ** n

print(soma)

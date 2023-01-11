def fibonacci(n):
    n1 = 0
    n2 = 1
    cont = 2

    if n == 1:
        return 0
    elif n == 2:
        return 1
    while cont <= n:
        n1, n2 = n2, n1 + n2
        cont += 1
    return n1


entrada = input()
lista_index = [int(i) for i in input().split()]
result = []

for i in lista_index:
    result += [fibonacci(i)]

print(tuple(result))

string = input()
elementos = {}

for s in string:
    if s in elementos:
        elementos[s] += 1
    else:
        elementos[s] = 1

impares = []
pares = []

for n in elementos.values():
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

result = sum(pares)
if impares != []:
    result += max(impares)
    for i in impares:
        if i == max(impares):
            continue
        else:
            result += i-1

print(result)

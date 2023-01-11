dicio = {}
dicio_reverso = {}

for _ in range(5):
    chave = input()
    valor = int(input())

    dicio[chave] = valor
    dicio_reverso[valor] = chave

print(dicio)
print(dicio_reverso)

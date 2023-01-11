#dicionario até o input
#1 caso = inteiro par -> chave[chave elevado a 2]
#2 caso = qualquer num -> chave[chave * 5]
dicio = {}

for i in range(1,int(input())+1):
    if i % 2 == 0:
        dicio[i] = i ** 2
    else:
        dicio[i] = i * 5

print(dicio)

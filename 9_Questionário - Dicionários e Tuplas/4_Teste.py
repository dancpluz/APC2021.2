lista1 = []
lista2 = []

for _ in range(5):
    lista1 += [int(input())]

for _ in range(5):
    lista2 += [int(input())]

lista_final = list(zip(lista1,lista2))
lista_medias = []

for i in lista_final:
    lista_medias += [(i[0] + i[1]) / 2]

print(lista_final)
print(lista_medias)

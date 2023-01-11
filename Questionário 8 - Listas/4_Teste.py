nome = input()
lista = []

while nome != 'EOF':
    lista += [nome]
    nome = input()

lista.sort()
print(len(lista))
print(lista)

q = int(input()) #quantas strings pedir, deve ser int
cont = 0 #contador para regular o loop while
lista = [] #lista vazia para colocar os inputs

while cont < q: #loop até o contador passar da quantidade de loops
    str = input() #recebe a string
    lista.append(str) #coloca a string na lista
    cont += 1 #aumenta o contador

print(max(lista, key=len)) #printa o elemento da lista com o maior len

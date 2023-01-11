q = int(input()) #quantas strings pedir, deve ser int
cont = 0 #contador para regular o loop while

while cont < q: #loop até o contador passar da quantidade de loops
    lrs = input().split() #recebe o valor de l, r e string em um input e divide em listas
    l = int(lrs[0]) #separa o l do input, deve ser int
    r = int(lrs[1]) #separa o r do input, deve ser int
    str = lrs[2] #separa a string do input
    print(str[l:r+1]) #printa o resultado da substring no intervalo
    cont += 1 #aumenta o contador

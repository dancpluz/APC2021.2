#separar palavras da string com split e imprimir
#imprimir somente palavras da lista com len() > 6

list = input().split()

print(list)

for palavra in list:
    if len(palavra) > 6:
        print(palavra)

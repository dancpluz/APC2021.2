#n quantidade de numeros
#numeros
#testar se a soma do primeiro numero com os outros da 42
#testar isso para o segundo e assim por diante
#se algum der, para o loop e printar sim

n = int(input())
numeros = input().split()
numeros = [int(i) for i in numeros]

for primeiro in numeros:
    for segundo in numeros:
        if primeiro == segundo:
            pass
        elif primeiro + segundo == 42:
            print('sim')
            exit()

print('nao')

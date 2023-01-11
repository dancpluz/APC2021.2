qnt_gatos = int(input())
num_sorteados = input().split() #['1','2','3','4','5','6']
num_sorteados = ' '.join(num_sorteados) #'1 2 3 4 5 6'
gatos = {}
ganhador = ''

for _ in range(qnt_gatos):
    nome_numeros = input().split('-')
    gatos[nome_numeros[0]] = nome_numeros[1]
    if nome_numeros[1] == num_sorteados:
        ganhador = nome_numeros[0]

if ganhador == '':
    print('não foi dessa vez /:')
else:
    print('deu bom!')
    print(ganhador)

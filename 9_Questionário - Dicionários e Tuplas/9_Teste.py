#C aluno nota: Cria um novo aluno com nome aluno e com nota.
#R aluno: Imprime uma linha com a nota do aluno de nome aluno.
#U aluno nota: Atualiza a nota do aluno com a nova nota.

dic_inicial = {
    'João' : 10,
    'Maria' : 10,
    'Jorge' : 4,
    'Marta' : 5,
    'Mário' : 6,
    'Mikael' : 9
}

qnt_entradas = int(input())

for _ in range(qnt_entradas):
    comando = input().split()
    operacao = comando[0]
    aluno = comando[1]

    if operacao == 'C':
        nota = int(comando[2])
        dic_inicial[aluno] = nota
    elif operacao == 'R':
        print(aluno,dic_inicial[aluno])
    elif operacao == 'U':
        nota = int(comando[2])
        dic_inicial[aluno] = nota

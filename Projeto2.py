#Comandos:
#[carga DOCENTE] carga horária do docente
#disciplinas e turmas em ordem alfabética do nome da disciplina.
#apresenta a carga horária total de aulas do docente e a média de horas por aluno
#considerando apenas as disciplinas com pelo menos 6 discentes matriculados.

#[disciplina D] lista as disciplinas (item) com turmas que têm pelo menos D (≥0) docentes como responsáveis.
#Mostra apenas as turmas que atendem esta condição, e as lista em ordem alfabética
#indicando quantos docentes estão efetivamente registrados.

#[leia ARQ] carrega na memória as informações no arquivo ARQ para processamento.
#O arquivo é um CSV (codificado em UTF-8) que lista a oferta de turmas de um departamento.

#[matriculas COD1 COD2 ... CODN] calcula a quantidade total de matriculados em cada turma
#das disciplinas fornecidas (COD) e as mostra em ordem decrescente
#(a ordem alfabética do nome da disciplina deve ser usada para desempate).
#Há um espaço entre cada elemento do comando.

#[FIM] interrompe a execução do programa.

#Entrada:
#A entrada consiste de uma quantidade indeterminada de instruções,
#dentre as 4 primeiras descritas acima, apresentadas uma por linha,
#seguidas da instrução de finalização do processamento.

#separar em um dicionario com código e turma

#Código,Nome,Turma,Ano-Período,Docente,Horário,Qtde Vagas Ofertadas,Qtde Vagas Ocupadas,Local
#{'Código': 'CIC0203', 'Nome': 'COMPUTAÇÃO EXPERIMENTAL', 'Turma': 'A', 'Ano-Período': '2021.1', 'Docente': 'JORGE HENRIQUE CABRAL FERNANDES (60h)', 'Horário': '35T23', 'Qtde Vagas Ofertadas': '50', 'Qtde Vagas Ocupadas': '30', 'Local': 'REMOTO'}

def remover_repetidos(lista):
    result = []
    for i in lista:
        if i not in result:
            result += [i]
    return result

def horas_docente(dicio):
    index = dicio['Docente'].find('(')+1
    index_f = dicio['Docente'].find(')')-1
    hora = dicio['Docente'][index:index_f]
    return hora

def carga(doc,info):
    result_dicios = []

    for dicio in info:
        if doc in dicio['Docente']:
            result_dicios += [dicio]

    if result_dicios == []:
        print(f'No hay {doc}...')
        return

    passados = []

    result_dicios.sort(key=lambda x: x['Turma'])
    result_dicios.sort(key=lambda x: x['Nome'])

    print(f'{doc}:')
    for d in result_dicios:
        if d['Nome'] in passados:
            print(f'     Turma {d["Turma"]}: {horas_docente(d)}h ({d["Qtde Vagas Ocupadas"]} alunos)')
        else:
            print(f' * {d["Nome"]} ({d["Código"]}):\n     Turma {d["Turma"]}: {horas_docente(d)}h ({d["Qtde Vagas Ocupadas"]} alunos)')
            passados += [d['Nome']]

    carga_horaria_total = 0
    total_alunos = 0

    for d in result_dicios:
        if int(d['Qtde Vagas Ocupadas']) >= 6:
            carga_horaria_total += int(horas_docente(d))
            total_alunos += int(d['Qtde Vagas Ocupadas'])

    media_horas = float(carga_horaria_total) / float(total_alunos)
    print(f'[Carga total considerada: {carga_horaria_total}h ({media_horas:.2f}h/aluno)]')
    return

def disciplina(n,info):
    codigos_turmas = [(d['Código'],d['Turma']) for d in info]
    repetidos = []

    for d in info:
        if codigos_turmas.count((d['Código'],d['Turma'])) >= n:
            lista = [d['Código'],d['Nome'],d['Turma']]
            repetidos += [lista]

    repetidos.sort(key=lambda x: x[1])
    repetidos += [['','','']]

    lista_result = []
    cdg = []
    #código:nome, Turma:[x,y,z]
    for r in repetidos:
        if r[0] not in cdg:
            if cdg != []:
                dicio['Turmas'] = turmas
                lista_result += [dicio]
            dicio = {}
            turmas = []
            cdg += [r[0]]
            turmas += [r[2]]
            dicio[r[0]] = r[1]
        else:
            turmas += [r[2]]

    if lista_result == []:
        print(f'No hay {n}...')
        return

    print(f'Turmas com pelo menos {n} docentes:')

    for i in lista_result:
        codigo = list(i.keys())[0]
        nome = i[codigo]
        turmas = remover_repetidos(i['Turmas'])
        turmas.sort()
        turmas_num = [i['Turmas'].count(x) for x in turmas]
        turmas_str = [f'{turmas[index]} ({turmas_num[index]})' for index in range(len(turmas))]
        turmas_str = ', '.join(turmas_str)

        print(f' * {nome} ({codigo}): {turmas_str}')
    return

def matriculas(lista,info):#ordenar por nome tbm
    result = []
    nome_dic = {}

    for d in info: #bota no dicionario Código:Nome
        nome_dic[d['Código']] = d['Nome']

    lista_filtro = []

    for t in lista: #filtra a lista removendo as matricula q n tem
        for k in nome_dic:
            if t == k:
                lista_filtro += [t]
                break

    for f in lista:#se n estiver no filtro printa o erro
        if f not in lista_filtro:
            print(f'No hay {f}...')

    for i in lista_filtro:
        numeros = []
        passados = []
        for d in info:
            if i == d['Código'] and d['Turma'] not in passados:
                numeros += [int(d['Qtde Vagas Ocupadas'])]
                passados += [d['Turma']]
        result += [(nome_dic[i],i,sum(numeros))]

    result.sort(key=lambda x: x[0])
    result.sort(reverse=True,key=lambda x: x[2])


    for t in result:
        print(f'{t[2]} matriculados em {t[0]} ({t[1]})')
    return

def guardar_info():
    global lista_dicios
    with open(arquivo,'r') as f:
        linhas = f.read().split('\n')
        tags = linhas[0].split(',')

        for i in linhas[1:]:
            if i == '':
                break
            else:
                dicio = {}
                info = i.split(',')
                for t in range(len(tags)):
                    dicio[tags[t]] = info[t]
                lista_dicios += [dicio]
        return

def main(com,ent):
    global lista_dicios
    if com == 'carga':
        doc = ' '.join(ent)
        carga(doc,lista_dicios)
        return
    elif com == 'disciplina':
        n = int(''.join(ent))
        disciplina(n,lista_dicios)
        return
    elif com == 'matriculas':
        lista = ent
        matriculas(lista,lista_dicios)
        return

leia_passados = []
lista_dicios = []
arquivo = ''
fim = False
while not fim: #temp
    comando = input().split()

    if comando == ['FIM']:
        fim = True
    elif 'leia' in comando:
        arquivo = comando[1]
        if arquivo not in leia_passados:
            leia_passados += [arquivo]
            guardar_info()
    else:
        if arquivo == '':
            if 'carga' in comando:
                entrada = comando[1:]
                entrada = ' '.join(entrada)
                print(f'No hay {entrada}...')
            elif 'matriculas' in comando:
                entrada = comando[1:]
                for e in entrada:
                    print(f'No hay {e}...')
            elif 'disciplina' in comando:
                entrada = comando[1]
                print(f'No hay {entrada}...')
        else:
            com = comando[0]
            ent = comando[1:]
            main(com,ent)

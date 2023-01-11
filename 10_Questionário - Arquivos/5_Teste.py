import csv

cursos = { '127' : 'Bacharelado em Ciência da Computação',
'132' : 'Arquitetura e Urbanismo',
'136' : 'Engenharia Civil',
'137' : 'Engenharia Elétrica',
'139' : 'Engenharia Florestal',
'158' : 'Licenciatura em Física',
'159' : 'Licenciatura em Química',
'160' : 'Licenciatura em Ciências Biológicas',
'161' : 'Licenciatura em Matemática',
'162' : 'Licenciatura em Lígua Portuguesa'
}

filename = input()
f = open(filename, 'r', encoding='latin_1', newline='')
reader = csv.reader(f, delimiter=';')
soma = 0
cont = 0
total = 0
total_M = 0
total_F = 0
soma_F = 0
soma_M = 0
for row in reader:
    total += 1
    if row[4]=="555":
        curso = row[1]
        cont += 1
        if row[3] == 'M':
            total_M += 1
            soma += float(row[5].replace(',','.'))
            soma_M += float(row[5].replace(',','.'))
        elif row[3] == 'F':
            total_F += 1
            soma += float(row[5].replace(',','.'))
            soma_F += float(row[5].replace(',','.'))
    else:
        pass

media = soma / cont
media_M = soma_M/total_M
media_F = soma_F/total_F
print(f'Relatório ENADE 2017')
print(f'Curso: {cursos[curso]}')
print(f'Total de alunos inscritos: {total-1}') #não conta a primeira linha que é o sigla dos campos
print(f'Total de alunos que realizaram o Enade: {cont}')
print(f'Média d@s alun@s do sexo masculino do curso que fizeram o ENADE: {media_M:.2f}')
print(f'Média d@s alun@s do sexo feminino do curso que fizeram o ENADE: {media_F:.2f}')
print(f'Média geral dos alunos que realizaram o ENADE: {media:.2f}')

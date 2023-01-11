ano = input()
ano_int = int(ano) + 1
cont = 0

while cont < len(ano):
    ano_list = list(str(ano_int))
    ano_list_sem = list(str(ano_int))
    ano_list_sem.pop(cont)

    if ano_list[cont] in ano_list_sem:
        ano_int += 1
        cont = 0
    else:
        cont += 1

print(ano_int)

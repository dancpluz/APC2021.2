#simbolos: + (adicionar) - (retirar) ? (mostrar grade semanal) 'Hasta la vista, beibe!' (exit)
#simbolo + materia + horarios
#materia -> padrão: XXX(unidade responsável pela oferta)####(código)Y(turma do horario) = CIC0004B
#horario -> padrão: D(dias da semana)T(turno)H(horas das aulas) = 35M12
#caso não seja possível atualizar a grade, apresente a mensagem: '!(instrução fornecida)'
#não permitir adição de disciplinas com choque de horário e remover disciplina que não ta na grade

def linha():
    return ('+'+'-'*15)+('+'+'-'*10)*6+'+'

def print_tabela_cima():

    print(linha())

    print('|'+' '*15,end='')
    print('|'+' '+'Seg'+' '*6,end='')
    print('|'+' '+'Ter'+' '*6,end='')
    print('|'+' '+'Qua'+' '*6,end='')
    print('|'+' '+'Qui'+' '*6,end='')
    print('|'+' '+'Sex'+' '*6,end='')
    print('|'+' '+'Sab'+' '*6+'|')

    print(linha())

    return

def juntar_horarios(d):
    for i in range(len(d)):
        for f in range(len(d)):
            if i == f:
                pass
            else:
                if d[i]['h'] == d[f]['h']:
                    for b in range(2,8):
                        b = str(b)
                        if d[i][b] == 0 and d[f][b] == 0:
                            pass
                        elif d[i][b] != 0:
                            d[f][b] = d[i][b]
                        elif d[f][b] != 0:
                            d[i][b] = d[f][b]
    return remover_repetidos(d)

def ordenar_instr(list_i):
    list_f = []
    for i in list_i:
        l = list(i[1])
        l = ''.join(sorted(l))
        list_f += [(i[0],l,sorted(i[2]))]
    return list_f

def tabela_baixo(list_i):
    lista_dic = []
    list_i = ordenar_instr(list_i)

    for i in list_i:
        dias_semana = {'h':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
        for hora in i[2]:
            for dia in i[1]:
                dias_semana[dia] = f' {i[0]} '
            dias_semana['h'] = hora
            lista_dic.append(dias_semana)
            dias_semana = {'h':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
    return juntar_horarios(lista_dic)

def print_tabela_baixo(dicios):
    numeros = '234567'

    for i in dicios:
        print(tabela_horario(i['h']),end=''
        for n in numeros
            if i[n] == 0
                print(' '*10+'|',end=''
            else:
                print(i[n]+'|',end='')
        print('\n'+linha())
    return

def tabela_horario(h):
    horarios = {1:'08:00 - 08:55',2:'08:55 - 09:50',3:'10:00 - 10:55',4:'10:55 - 11:50',5:'12:00 - 12:55'
                ,6:'12:55 - 13:50',7:'14:00 - 14:55',8:'14:55 - 15:50',9:'16:00 - 16:55',10:'16:55 - 17:50',11:'18:00 - 18:55'
                ,12:'19:00 - 19:50',13:'19:50 - 20:40',14:'20:50 - 21:40',15:'21:40 - 22:30'}
    return f'| {horarios[h]} |'

def print_erros():
    global erros

    if erros == []:
        return
    else:
        for e in erros:
            print(f'!({e})')
        return

def separar(dth):
    dias_list = []
    horas_list = []
    dias_str = ''

    for i in dth:
        if 'M' in i:
            dias_horas = i.split('M')
            horas_list += [int(i) for i in dias_horas[1]]
        if 'T' in i:
            dias_horas = i.split('T')
            horas_list += [int(i)+5 for i in dias_horas[1]]
        if 'N' in i:
            dias_horas = i.split('N')
            horas_list += [int(i)+11 for i in dias_horas[1]]
        dias_list += [dias_horas[0]]

    dias_list = remover_repetidos(dias_list)
    horas_list = remover_repetidos(horas_list)

    for i in dias_list:
        dias_str += i
    return (dias_str,horas_list)

def remover_repetidos(lista):
    final = []
    for i in lista:
        if i in final:
            pass
        else:
            final.append(i)
    return final

def arquivar(codigo,dias,horas):
    lista = []

    for i in dias:
        for h in horas:
            lista.append((codigo,i,h))
    return lista

def juntar(arq):
    final_cod = []
    final_d = []
    final_h = []
    result = []
    result_um = []

    for e in arq: #('CIC0004F', '2', 7)
        if e[0] not in final_cod and final_cod != []:
            final_cod = ''.join(final_cod)
            final_d = ''.join(final_d)
            result_um = [final_cod,final_d,final_h]
            result += [tuple(result_um)]
            final_cod = []
            final_d = []
            final_h = []
        for i in e:
            if i not in final_cod and type(i) == str and len(i) > 2:
                final_cod += [i]
            elif i not in final_d and type(i) == str and len(i) < 2:
                final_d += [i]
            elif i not in final_h and type(i) == int:
                final_h += [i]

    final_cod = ''.join(final_cod)
    final_d = ''.join(final_d)
    result_um = [final_cod,final_d,final_h]
    result += [tuple(result_um)]
    return result

def checar_erro():
    global arquivo
    list = []
    for i in arquivo:
        diahora = i[1] + str(i[2])
        if diahora in list:
            for e in arquivo:
                if i[0] == e[0]:
                    achei = arquivo.index(e)
                    arquivo = arquivo[:achei]
                    break
            return False
        else:
            list.append(diahora)
    return True

def primeiro(instr):
    return instr[2][0]

def organizar_instr():
    global instr
    instr.sort(key=primeiro)
    return

def checar_remover(t):
    global instr

    if t[0] in instr:
        return True
    else:
        return False


arquivo = []
erros = []
instr = []
while True:
    entrada = input().split()
    if ''.join(entrada) == '?':
        print_erros()
        erros = []
        print_tabela_cima()
        if arquivo == [] and erros == []:
            pass
        else:
            l_dicios = tabela_baixo(instr)
            print_tabela_baixo(l_dicios)
    elif ' '.join(entrada) == 'Hasta la vista, beibe!':
        exit()
    else:
        if entrada[0] == '+':
            dias,horas = separar(entrada[2:])
            codigo = entrada[1]
            arquivo += arquivar(codigo,dias,horas)
            if checar_erro():
                instr = juntar(arquivo)
                organizar_instr()
            else:
                erros += [' '.join(entrada)]
                erros = remover_repetidos(erros)
        elif entrada[0] == '-':
            dias,horas = separar(entrada[2:])
            codigo = entrada[1]
            arquivo_rem = arquivar(codigo,dias,horas)
            instr_rem = juntar(arquivo_rem)
            if checar_remover(instr_rem):
                instr.pop()
                index = arquivo.index(arquivo_rem[0])
                arquivo = arquivo[:index]
            else:
                erros += [' '.join(entrada)]
                erros = remover_repetidos(erros)

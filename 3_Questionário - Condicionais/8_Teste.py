def jogadas(a,b):
    falta = faltam(a,b)

    if falta == 0:
        print(0)
    elif falta > 10:
        divisao = int(falta / 10)
        if falta % 10 > 0:
            print(divisao+1)
        else:
            print(divisao)
    else:
        print(1)

def faltam(a,b):
    if a > b:
        return a - b
    elif b > a:
        return b - a
    else:
        return 0

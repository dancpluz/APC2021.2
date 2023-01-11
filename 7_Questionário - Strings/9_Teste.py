#dividir a len string no meio
#verificar se a divisao teve resto
#if sim verificar começo e final, sem o meio
#else verificar começo e final e se algum pode ser trocado

str = input()
div = len(str) / 2
count = 1
a = -1

if div == int(div):
    while count > 0:
        for i in range(0,int(div)+1):
            if str[i] != str[a]:
                count -= 1
            a -= 1
        print('ON')
        break
    if count > 0:
        print('OFF')
else:
    while count > 0:
        for i in range(0,int(div)+1):
            if str[i] != str[a]:
                count -= 1
            a -= 1
        count = 0
    if count < 0:
        print('OFF')
    else:
        print('ON')

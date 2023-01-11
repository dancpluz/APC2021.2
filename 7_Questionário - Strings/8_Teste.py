#split com WUB
#remover os espaços vazios

str = input().split('WUB')

while '' in str:
    str.remove('')

print(' '.join(str))

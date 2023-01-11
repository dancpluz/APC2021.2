linha = int(input())

with open('/etc/passwd','r') as senha:
    tudo = senha.read().split('\n')
    users = []
    for l in tudo:
        l = l.split(':')
        users += [l[0]]
    print(users[linha-1])

#numero de jogadores
#habilidade de cada jogador
#lista em int com a habilidade, sort
#cortar os 11 jogadores da lista e sum
#oq sobrou sum
#diferença entre somas

jogadores = int(input())
habilidade = input().split()
habilidade = [int(i) for i in habilidade]
habilidade.sort(reverse=True)

soma_titular = sum(habilidade[:11])
if jogadores > 22:
    soma_reserva = sum(habilidade[11:22])
else:
    soma_reserva = sum(habilidade[11:])

print(soma_titular - soma_reserva)

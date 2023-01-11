#m = numero de fileiras
#n = quantidade de cadeiras em cada fileira
#input cadeiras na fileira, 0 vazio, 1 ocupado
#contar os zeros seguidos de uma fileira

m_n = input().split()
m = int(m_n[0])
n = int(m_n[1])
cadeiras = []

for i in range(m):
    temp = input().split()
    temp = [int(i) for i in temp]
    cadeiras.append(temp)

cont = 0

for list in range(m):
    cont = 0
    while cont < len(cadeiras[list]+1):
        if cadeiras[list][cont] > 0:
            cont += 1
        elif cadeiras[list][cont] == 0:
            if cont == 0:
                if cadeiras[list][cont+1] == 1:
                    cadeiras[list].insert(cont,2)
                    cont += 3
                else:
                    cadeiras[list].insert(cont+1,2)
                    cadeiras[list].insert(cont,2)
                    cont += 3
            elif cadeiras[list][cont-1] == 2 and cadeiras[list][cont+1] == 2:
                cont += 3
            elif cadeiras[list][cont-1] == 2 or cadeiras[list][cont-1] == 1:
                cadeiras[list].insert(cont+1,2)
                cont += 3
            elif cadeiras[list][cont+1] == 2 or cadeiras[list][cont+1] == 1:
                cadeiras[list].insert(cont,2)
                cont += 3
            else:
                cadeiras[list].insert(cont+1,2)
                cadeiras[list].insert(cont,2)
                cont += 3

print(cadeiras)

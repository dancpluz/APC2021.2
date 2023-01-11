st = input().split() #recebe a banda desejada e as bandas que vão e divide em lista
s = st[0] #separa a banda desejada no s
t = st[1] #separa as bandas que vão no t

if s in t: #se a banda desejada estiver nas que vão
    print(f"A banda {s} ira se apresentar na RIR!")
else: #se não tiver
    print("por que o jimin nao vai vir pro brasil? ;-;")

import math

def TwoDSpace(deslocamento, amplitude, espaço):
    dicionario = {}
    for i in range(40):
            j = int(deslocamento - amplitude*math.sin(10*i*math.pi/180))
            dicionario[(i, j)] = "*"
    for j in range(20):
        if j != 0:
            print()
        for i in range(40):
            if (i,j) in dicionario.keys():
                print(dicionario[i,j],end='')
            else:
                print(espaço,end='')

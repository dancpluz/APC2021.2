peso1 = 1
peso2 = 2
peso3 = 3

def calcular_media(nota1, nota2, nota3):

    nota_final = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1+peso2+peso3)
    print(f'Sua nota final é {nota_final:.2f}')

n1, n2, n3 = map(float, input().split())

calcular_media(n1, n2, n3)

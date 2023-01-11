def caixa(n,p):
    if p == 1:
        return f"Voce ganhou um desconto de {desconto(n)} reais, volte sempre!"
    else:
        return f"Cada parcela é de {parcelamento(n,p)} reais, volte sempre!"

def desconto(n):
    return n * 0.15

def parcelamento(n,p):
    return n/p

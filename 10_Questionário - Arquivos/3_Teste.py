pedido = input()
tem_no_cardapio = False

with open('cardapio.txt','r') as cardapio:
    cardapio_lista = cardapio.read().split('\n')
    for i in cardapio_lista:
        comida = i.lower()
        if pedido in comida:
            tem_no_cardapio = True
            print(i)
    if not tem_no_cardapio:
        print('Infelizmente não temos este prato')

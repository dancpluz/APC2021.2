dolar = float(input())
tamanho_lote = int(input())
quant_lote = int(input())
taxa = dolar * tamanho_lote * 0.025
n = 1

while quant_lote > 0:
    print(f'Lote: {n} - Total da venda: R$ {dolar * tamanho_lote + taxa:.2f}')
    n += 1
    quant_lote -= 1

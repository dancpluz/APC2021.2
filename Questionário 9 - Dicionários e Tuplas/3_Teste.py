biblioteca = {}

for i in range(5):
    livro = input()
    num = int(input())

    biblioteca[livro] = num

busca = input()

if busca not in biblioteca:
    print('Poxa, não temos esse livro')
else:
    print(f'Achei! Temos {str(biblioteca[busca])} exemplar(es)!')

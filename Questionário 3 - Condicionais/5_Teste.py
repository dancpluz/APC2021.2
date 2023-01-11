def multiple(a,b):
    if a % b == 0:
        print(f'{a} eh multiplo de {b}')
    elif b % a == 0:
        print(f'{b} eh multiplo de {a}')
    else:
        print("nao multiplos")
